#!/usr/bin/env python3
import os
import logging
import sys

from PIL import ImageFont

try:
    from matplotlib import font_manager
    logging.getLogger("matplotlib").setLevel(logging.INFO)
except:
    font_manager = None

class NonProportional:
    """A dummy class used for text-mode/console rendering"""
    @classmethod
    def getlength(cls, string):
        return len(string)

class Font:
    """Tries to lookup the specified font, either as a TTF/OTF file
    or an OS-installed font family. Looks for bold, italic, and 
    bold-italic variants, and loads them all; handles finding metrics
    for strings/characters."""
    def __init__(self, filename, size="12pt", linespacing=1.4, boldfilename=None, italicfilename=None, bolditalicfilename=None):
        if size.endswith("pt"):
            size = round(4 * float(size[:-2])/3)
        elif size.endswith("px"):
            size = round(float(size[:-2]))
        else:
            raise Exception("Size must specify px or pt, e.g. 12pt or 16px")

        self.size = size
        self.space_cache = {}
        self.linespacing = linespacing

        self.filename = filename

        if filename is not NonProportional:
            def find_replace(fname, look_for_list):
                """Seek out Bold, Italic, and, BoldItalic equivalents if the primary is -Regular or -Medium.
                If the font is Times-Regular.ttf, look for Times-Bold.ttf, Times-Italic.ttf, and such
                If times-regular.ttf, look for times-bold.ttf etc. Return a match, or None if not found.

                This tries all sorts of permutations: '-Bold-Italic', 'Bold-Italic', ' Bold Italic', etc."""

                dirname, filename = os.path.split(fname)
                for template in "Regular", "Medium":
                    for part in ("-"+template, " "+template, template):
                        for look_template in look_for_list:
                            for look_for in (look_template, look_template.replace("-", " "), look_template.lstrip("-")):
                                if part in filename:
                                    test = filename.replace(part, look_for)
                                elif part.lower() in filename:
                                    test = filename.replace(part.lower(), look_for.lower())
                                else:
                                    continue
                                test = os.path.join(dirname, test)
                                if os.path.isfile(test):
                                    return test

                # Now try Times.ttf -> TimesBold.ttf, Times Bold.ttf, etc.
                if "." in filename:
                    base, ext = filename.rsplit(".", 1)
                    for look_for in look_for_list:
                        for look_for_case in (look_for, look_for.lower(), look_for[1:], look_for[1:].lower(), " "+look_for[1:], " "+look_for[1:].lower()):
                            test = os.path.join(dirname, "%s%s.%s"%(base, look_for_case, ext))
                            if os.path.isfile(test):
                                return test
                        
                return None

            # Filename t
            replacements = {
                "boldfilename": ("-Bold",),
                "italicfilename": ("-Italic",),
                "bolditalicfilename": ("-BoldItalic", "-Bold-Italic", "-Bold Italic"),
            }

            if filename is None and font_manager is None:
                logging.warning("Cannot load default font; falling back to PIL default. 'pip install matplotlib' to upgrade font handling.")
                self.font = ImageFont.load_default()
            else:
                if filename is None:
                    for name in ('Liberation Sans', 'Calibri', 'Lucida Grande', 'Helvetica', 'Verdana', 'Arial', 'Noto Sans', 'Ubuntu', 'DejaVu Sans', 'sans-serif'):
                        try:
                            font = font_manager.FontProperties(family=name)
                            self.filename = font_manager.findfont(font, fallback_to_default=False)
                            break
                        except:
                            logging.debug("No font %s", name)
                    else:
                        logging.error("No font found, not even sans-serif. Use --font NAME with an installed font or TTF/OTF font filename.")
                    logging.info("Using font: %s", self.filename)

                if not os.path.isfile(self.filename):
                    if font_manager is None:
                        logging.warning("Font is not a filename and no font manager available. 'pip install matplotlib' to find fonts by family.")
                        logging.error("Not a file: %s", self.filename)
                        sys.exit(-1)
                    else:
                        try:
                            font = font_manager.FontProperties(family=self.filename, weight='regular') 
                            self.filename = font_manager.findfont(font, fallback_to_default=False, rebuild_if_missing=True)
                        except ValueError as e:
                            try:
                                # rebuild_if_missing doesn't rebuild the cache. This is gross
                                # but actually forces a rebuild.
                                self.filename = font_manager._load_fontmanager(try_read_cache=False).findfont(font, fallback_to_default=False)
                            except:
                                logging.error("Unable to find font %s: %s", filename, e.args)
                                sys.exit(-1)



                self.font = ImageFont.truetype(self.filename, size=self.size)
                for replacement, value in replacements.items():
                    setattr(self, replacement, locals()[replacement] or find_replace(self.filename, value))
                    fname = getattr(self, replacement, None)
                    if fname:
                        setattr(self, replacement.replace("filename", "font"), ImageFont.truetype(fname, size=self.size))

                logging.debug("Using font: %s", self.filename)
                logging.debug("Using bold font: %s", self.boldfilename)
                logging.debug("Using italic font: %s", self.italicfilename)
                logging.debug("Using bolditalic font: %s", self.bolditalicfilename)

            try:
                hyphen_box = self.font.getbbox("‐")
            except:
                hyphen_box = (0,0,0,0)
            if hyphen_box[1] == hyphen_box[3]:
                self.hyphen = "-"
            else:
                self.hyphen = "‐" # Could be "‐" if font supports it.

        else:
            self.font = NonProportional
            self.boldfont = NonProportional
            self.bolditalicfont = NonProportional
            self.italicfont = NonProportional
            self.hyphen="‐"

    def get_space_width(self, space, bold=False, italic=False):
        return self.get_cached_width(space, bold, italic)

    def get_cached_width(self, character, bold=False, italic=False):
        """Return the width of a specified space, caching it for future use.
        Do not call this for non-spaces, or the cache will explode."""
        if character not in self.space_cache:
            self.space_cache[(character, bool(bold), bool(italic))] = self.get_word_width(character, bold, italic)
        return self.space_cache[(character, bool(bold), bool(italic))]

    def get_space_stretch(self, space, bold=False, italic=False):
        """How much is a space allowed to stretch?"""
        return self.get_space_width(space, bold, italic)*3/6

    def get_space_shrink(self, space, bold=False, italic=False):
        """How much is a space allowed to shrink?"""
        return self.get_space_width(space, bold, italic)*3/9

    def get_hyphen_width(self, bold=False, italic=False):
        return self.get_cached_width(self.hyphen, bold, italic)

    def get_word_width(self, string, bold=False, italic=False):
        return self.font.getlength(string)
