#!/usr/bin/env python3
import os
from locale import getlocale, getdefaultlocale, setlocale
import locale
import copy
import logging
import argparse
from collections import namedtuple

from PIL import Image, ImageDraw
import langcodes

from .font import Font, NonProportional
from .linebreak import BasicWordSplitter, RichWordSplitter, HBox, Glue
from .wordwrap import KnuthPlassWrap, GreedyWrap, is_newline

"""
   There are 3 different kinds of classes:

   Word-breaker: Breaks a word into HBoxes/Glue/Penalties. This may involve parsing HTML or other rich text
   tags. BasicWordSplitter is plain text. RichWordSplitter is mostly text, but allows <b> and <i>
   tags for bold/italic text.

   Wrapper: Handles laying out broken-down boxes into lines. GreedyWrap does naïve greedy wrapping: cram
   as much as you can onto a line, then break. KnuthPlassWrap implements the Knuth-Plass wrapping algorithm
   used by TeX/LaTeX.

   Font: Handles font loading and metrics.
"""

class TextWrap():
    @classmethod
    def text_wrapper(self, arg_dict, line_widths=None):
        if "image" not in arg_dict:
            arg_dict["image"] = "/dev/null"
        arglist = []
        for k, v in arg_dict.items():
            arglist.append(f"--{k}")
            if v is not None:
                arglist.append(f"{v}")
        args  = parse_arguments(args=arglist)
        tw = TextWrap(args, line_widths=line_widths)
        return tw

    def __init__(self, args, line_widths=None):

        if args.image:
            self.font = Font(args.font, size=args.font_size, linespacing=args.line_spacing)
        else:
            self.font = Font(NonProportional)

        splitter = globals().get(args.splitter+"Splitter")
        logging.info("Using splitter %s", splitter)
        self.splitter = splitter(font=self.font, args=args)

        self.width = args.width
        if self.width is None:
            if not args.image:
                self.width = 80
            else:
                self.width = 600

        line_max = self.width
        self.args = {"line_max": line_max, "font": self.font, "line_widths": line_widths}
        self.line_offset = round(self.font.size*self.font.linespacing)

        wrapper = globals().get(args.wrapper+"Wrap")
        logging.info("Using wrapper %s", wrapper)
        self.wrapper=wrapper(**self.args)
        self.wrapper.splitter = self.splitter
        self.wrapper.args = self.args

    def render_text(self, text):
        nodes = self.splitter.split(text)
        rv = []

        for paragraph in nodes:
            lines = self.wrapper.wrap_nodes_to_lines(paragraph, lines_processed = len(rv))
            rv = rv + lines

        return rv

    def split_and_wrap(self, text):
        paragraphs = self.splitter.split(text)
        lines_processed = 0
        for i, nodes in enumerate(paragraphs):
            paragraphs[i] = self.wrapper.wrap_nodes(nodes, lines_processed=lines_processed)
            lines_processed += len(paragraphs[i])
        return paragraphs

    def calculate_paragraph_height(self, lines):
        print(self.line_offset, self.font.size, self.font.linespacing)
        if len(lines)==1 and is_newline(lines[0].nodes[0]):
            return self.line_offset//3
        return len(lines) * self.line_offset

    def calculate_total_height(text):
        return sum(calculate_paragraph_height(paragraph) for paragraph in text)

    def render_image_to_file(self, text, filename, where=(0,0), margin=(0,0,0,0), fg=(0,0,0,255), bg=(255,255,255,255)):
        """Write out an image file of the rendered text. .png filenames are 
        best, but it'll render .jpg and .gif (and potentially others; it's
        up to PIL and RGB/RGBA foibles)."""
        img = self.render_image(text, img=None, where=where, margin=margin, fg=fg, bg=bg)
        if filename.endswith(".jpg"):
            background = Image.new("RGB", img.image.size, (255, 255, 255))
            background.paste(img.image, mask=img.image.split()[3]) # 3 is the alpha channel
            background.save(filename, quality=90)
        else:
            img.image.save(filename)
        return img.height

    def render_image(self, text, img=None, where=(0,0), margin=(0,0,0,0), fg=(0,0,0,255), bg=(255,255,255,255)):
        paragraphs = self.split_and_wrap(text)
        font = self.font

        if isinstance(margin, int):
            margin = (margin,)*4

        in_img = img
        if img is None:
            height = sum(self.calculate_paragraph_height(paragraph) for paragraph in paragraphs)
            width = self.width
            where = (margin[0], margin[1])
            img = Image.new("RGBA", (width+margin[0]+margin[2], height+margin[1]+margin[3]), bg)

        v_origin = where[0]
        h_origin = where[1]

        line_offset = 0
        for paragraph in paragraphs:
            self._render_image_part(paragraph, img, where=(v_origin, h_origin), fg=fg, line_offset=line_offset)
            line_offset += len(paragraph)
            v_origin += self.calculate_paragraph_height(paragraph)

        ImageData = namedtuple("ImageData", ["image", "height"])

        return ImageData(img, v_origin)

    def _render_image_part(self, lines, img, where=(0,0), fg=(0,0,0,255), line_offset=0):
        """Render to a PIL Image img, writing with foreground color fg. 

        If img is None, render to a newly allocated correctly sized image 
        with margins of (top, right, bottom,left) and background color bg.

        If img is not None, write text to that image, beginning at offset where.

        If filename is not None, save the img to filename."""

        draw = ImageDraw.Draw(img)
        draw.fontmode="L" #Anti-alias; "1" to turn off

        v_origin = where[0]
        h_origin = where[1]

        self.wrapper._lines_processed = 0
        for i, line in enumerate(lines):
            h_offset = h_origin + self.wrapper.calc_line_length(i + 1 + line_offset).offset
            ratio = line.ratio
            for j, item in enumerate(line.nodes):
                if isinstance(item, HBox):
                    draw.text( (h_offset, i*self.line_offset + v_origin), item.value, font=item.font, fill=fg)
                    h_delta = item.font.getlength(item.value)
                    h_offset += h_delta
                elif isinstance(item, Glue):
                    h_offset += item.width + (item.stretch* 0 if ratio>0 else item.shrink*ratio)
        return self.calculate_paragraph_height(lines)


def parse_arguments(args=None):
    warn_locale = False
    try:
        locale.setlocale(locale.LC_CTYPE, '')
    except locale.Error:
        warn_locale = True
    mylocale = getlocale(locale.LC_CTYPE)[0]
    if mylocale is None:
        mylocale = 'en_US' # Default to US english if we can't figure out the user's preference

    parser = argparse.ArgumentParser("Lay out specified text")
    parser.add_argument("--file", "-f", help="Pull text to wrap from FILE")
    parser.add_argument("--image", "-i", help="Generate image in file named IMAGE. Image filename must end with .png", default=None)
    parser.add_argument("--margin", help="Have a margin of width MARGIN around the text (image mode only)", default=5, type=int)
    parser.add_argument("--hyphenate", "-H", action="store_true", help="Attempt to hyphenate words with PyHyphen.")
    parser.add_argument("--width", "-w", type=int, default=None, help="Width to render. This is in pixels in image mode, or in characters in text mode.")
    parser.add_argument("--font", "-F", help="Font to use. Can be a font face (Calibri, Lucida Grande, Liberation Sans, etc) or a full path to a .ttf or .otf file. If you pass it a regular/normal weight, it'll try to find the bold/italic variants in the same location.", default=None)
    parser.add_argument("--font-size", help="Font size, either points or pixels, e.g. 12pt or 16px", default="12pt")
    parser.add_argument("--line-spacing", help="Font line spacing, default 1.2", default=1.2, type=float)

    less_common = parser.add_argument_group("Advanced Options")
    less_common.add_argument("--splitter", choices=["RichWord", "BasicWord"], default="RichWord", help="Which text splitter to use. RichWord treats <b> and <i> as bold/italic and <nb> for non-breaking runs. BasicWord is a simple plaintext splitter (splits at breaking whitespace only).")
    less_common.add_argument("--wrapper", choices=["KnuthPlass", "Greedy"], default="KnuthPlass", help="Which word-wrapping algorithm to use; KnuthPlass is the TeX algoritm, Greedy is simple greedy-matching")
    less_common.add_argument("--no-warn-locale", "-W", action="store_false", dest="warn_locale", help="Suppress warnings about being unable to set locale")
    less_common.add_argument("--verbose", "-v", action="store_true", help="Print extra info")
    less_common.add_argument("--debug", action="store_true", help="Print debugging info")
    less_common.add_argument("--test", "-t", action="store_true", help="Run on test data with text and image output")
    less_common.add_argument("--language", "-l", default=mylocale, help="Language to use for hyphenation (e.g. en_GB, ja_JP, de_DE, fr_FR, zh_HANS, es_ES, etc); defaults to platform locale, you can often set the LC_ALL environment variable or change system configuration to set that.")
    less_common.add_argument("--hyphen-penalty", type=int, default=100, help="Penalty factor for hyphenation (lower results in more hyphenation; default 100)")
    less_common.add_argument("--midbreak-penalty", type=int, default=25, help="Penalty factor for breaking after a hard - or — (lower results in more breaks; default 25)")
    args = parser.parse_args(args)

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s|%(levelname)s - %(message)s")
    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s|%(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.WARNING, format="%(asctime)s|%(levelname)s - %(message)s")

    if warn_locale and args.warn_locale and args.hyphenate:
        logging.warning(f"Unable to set locale (bad LC_CTYPE or LANG environment variable?), using {mylocale}. Consider --language if needed. Use --no-warn-locale/-W to suppress this warning.")

    logging.info("Args: %s", str(args))

    if args.hyphenate:
        try:
            import hyphen
        except:
            logging.error("Cannot import hyphen; try 'pip install pyhyphen' if you need hyphenation support")
            sys.exit(-1)

        try:
            hyphen.Hyphenator(args.language)
        except IOError:
            standard = langcodes.standardize_tag(args.language).replace("-", "_")
            try:
                hyphen.Hyphenator(standard)
                args.language = standard
            except IOError:
                logging.error(f"Unable to hyphenate {args.language}")
                sys.exit(-1)

        try:
            human_language = ": " + langcodes.Language.get(args.language).display_name()
        except:
            human_language = ""
        logging.info(f"Using hyphenation language {args.language}{human_language}")

    return args

