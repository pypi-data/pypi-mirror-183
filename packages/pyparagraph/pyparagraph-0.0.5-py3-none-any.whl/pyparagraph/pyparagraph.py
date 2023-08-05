#!/usr/bin/env python3
import os
from locale import getlocale, getdefaultlocale, setlocale
import locale
import copy
import logging
import argparse

from PIL import Image, ImageDraw
import langcodes

from .font import Font, NonProportional
from .linebreak import BasicWordSplitter, RichWordSplitter, HBox, Glue
from .wordwrap import KnuthPlassWrap, GreedyWrap

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
    def text_wrapper(self, arg_dict):
        if "image" not in arg_dict:
            arg_dict["image"] = "/dev/null"
        arglist = []
        for k, v in arg_dict.items():
            arglist.append(f"--{k}")
            arglist.append(f"{v}")
        print(arglist)
        args  = parse_arguments(args=arglist)
        print(args)
        tw = TextWrap(args)
        return tw

    def __init__(self, args, line_widths=None):

        if args.image:
            self.font = Font(args.font, size=args.font_size)
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

        wrapper = globals().get(args.wrapper+"Wrap")
        logging.info("Using wrapper %s", wrapper)
        self.wrapper=wrapper(**self.args)
        self.wrapper.splitter = self.splitter
        self.wrapper.args = self.args

    def render_text(self, text):
        nodes = self.splitter.split(text)
        lines = self.wrapper.wrap_nodes_to_lines(nodes)
        return lines

    def split_and_wrap(self, text):
        nodes = self.splitter.split(text)
        lines = self.wrapper.wrap_nodes(nodes)
        return lines

    def render_image(self, text, filename=None, img=None, where=(0,0), margin=(0,0,0,0), fg=(0,0,0,255), bg=(255,255,255,255)):
        """Render to a PIL Image img, writing with foreground color fg. 

        If img is None, render to a newly allocated correctly sized image 
        with margins of (top, right, bottom,left) and background color bg.

        If img is not None, write text to that image, beginning at offset where.

        If filename is not None, save the img to filename."""

        if (filename is None and img is None) or (filename is not None and img is not None):
            raise ValueError("render_image must specify one of filename or img")
        

        lines = self.split_and_wrap(text)
        font = self.font

        line_offset = round(self.font.size*self.font.linespacing)
        if isinstance(margin, int):
            margin = (margin,)*4

        in_img = img
        if img is None:
            height = line_offset*len(lines) + margin[0]+margin[2]
            width = self.width + margin[1] +margin[3]
            where = (margin[0], margin[1])
            img = Image.new("RGBA", (width,height), bg)

        draw = ImageDraw.Draw(img)
        draw.fontmode="L" #Anti-alias; "1" to turn off

        v_origin = where[0]
        h_origin = where[1]

        for i, line in enumerate(lines):
            h_offset = h_origin
            ratio = line.ratio
            for j, item in enumerate(line.nodes):
                if isinstance(item, HBox):
                    draw.text( (h_offset, i*line_offset + v_origin), item.value, font=item.font, fill=fg)
                    h_delta = item.font.getlength(item.value)
                    h_offset += h_delta
                elif isinstance(item, Glue):
                    h_offset += item.width + (item.stretch* 0 if ratio>0 else item.shrink*ratio)

        if filename is not None:
            img.save(filename)
        if not in_img:
            return img
        return len(lines)*line_offset + v_origin


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
    parser.add_argument("--wrapper", choices=["KnuthPlass", "Greedy"], default="KnuthPlass", help="Which word-wrapping algorithm to use; KnuthPlass is the TeX algoritm, Greedy is simple greedy-matching")
    parser.add_argument("--file", "-f", help="Pull text to wrap from FILE")
    parser.add_argument("--image", "-i", help="Generate image in file named IMAGE. Image filename must end with .png", default=None)
    parser.add_argument("--margin", help="Have a margin of width MARGIN around the text (image mode only)", default=5, type=int)
    parser.add_argument("--hyphenate", "-H", action="store_true", help="Attempt to hyphenate words with PyHyphen.")
    parser.add_argument("--width", "-w", type=int, default=None, help="Width to render. This is in pixels in image mode, or in characters in text mode.")
    parser.add_argument("--font", "-F", help="Font to use. Can be a font face (Calibri, Lucida Grande, Liberation Sans, etc) or a full path to a .ttf or .otf file. If you pass it a regular/normal weight, it'll try to find the bold/italic variants in the same location.", default=None)
    parser.add_argument("--font-size", help="Font size, either points or pixels, e.g. 12pt or 16px", default="12pt")

    less_common = parser.add_argument_group("Advanced Options")
    less_common.add_argument("--splitter", choices=["RichWord", "BasicWord"], default="RichWord", help="Which text splitter to use. RichWord treats <b> and <i> as bold/italic and <nb> for non-breaking runs. BasicWord is a simple plaintext splitter (splits at breaking whitespace only).")
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

