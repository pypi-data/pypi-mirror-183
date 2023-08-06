#!/usr/bin/env python3
import re
import sys

try:
    from hyphen import Hyphenator
    have_hyphenate = True
except:
    have_hyphenate = False

def pairwise(iterable):
    """list(pairwise([1,2,3,4,5,6])) --> [(1,2), (3,4), (5,6)]"""
    a = iter(iterable)
    return zip(a, a)

class HBox:
    def __init__(self, value, font):
        self.value = value
        self.font = font
        self.width = self.font.getlength(value)
    def __repr__(self):
        return f'HBox(value={repr(self.value)})'

class Penalty:
    def __init__(self, width, penalty, flagged):
        self.width = width
        self.penalty = penalty
        self.flagged = flagged
    def __repr__(self):
        return f'Penalty(width={repr(self.width)}, penalty={repr(self.penalty)}, flagged={repr(self.flagged)})'

class Glue:
    def __init__(self, width, stretch, shrink):
        self.width = width
        self.stretch = stretch
        self.shrink = shrink
    def __repr__(self):
        return f'Glue(width={repr(self.width)}, stretch={repr(self.stretch)}, shrink={repr(self.shrink)})'
    def __add__(self, other):
        return Glue(self.width+other.width, self.stretch+other.stretch, self.shrink+other.shrink)

Infinity = 10**10   # 10000 fails on some not uncommonly cramped sizes

def fix_hyphenation(words):
    rv = []
    for word in words:
        if not word[0].isalpha() and rv:
            rv[-1]+= word
        else:
            rv.append(word)
    return rv

# Handle a few characters that we want to be able to break after,
# even mid-word.  We don't break cases where the latter part is a number. 
# So "1/2" and "1-2" will not be split, but "3-part" and "Frost/Nixon" 
# may be split after the punctuation symbol.
#
# And there's a look-before to prevent breaking if the previous character
# is a <, so we don't break "</" "span>" mid-tag and similar.

wordbreak_chars = "-—–/>"
wordbreak_char_re = re.compile("(?<!<)([%s]+)(?!$|[0-9])"%wordbreak_chars)

#
# Breaking spaces: the whitespace spaces that should break words.
#

breaking_spaces = " \u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u200B"
breaking_re = re.compile(f"([{breaking_spaces}])")

class BaseWordSplitter:
    def __init__(self, args, font=None):
        self.font = font
        self.hyphen_penalty = args.hyphen_penalty
        self.midbreak_penalty = args.midbreak_penalty
        self.hyphenate = args.hyphenate
        self.nobreak = 0  # Do not create breaks if > 0
        if self.hyphenate:
            self.hyphenator = Hyphenator('en_US')

    def split(self, text):
        # Canonicalize DOS and old Macintosh line endings to \n
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")
        # Strip a single trailing \n if needed
        if text and text[-1] == "\n":
            text = text[:-1]
        paragraphs = text.split("\n")
        rv = []
        for paragraph in paragraphs:
            rv.append(self.split_paragraph(paragraph))
        return rv

    def add_space(self, space=" "):
        """Depending on nobreak, adds a breaking or non-breaking space"""
        if self.nobreak:
            self.nodes.append(Penalty(0, Infinity, 0))
        self.nodes.append(Glue(0, self.font.get_space_width(space), 0))
        self.nodes.append(Penalty(0, Infinity if self.nobreak else 0, 0))
        self.nodes.append(Glue(self.font.get_space_width(space), self.font.get_space_stretch(space), self.font.get_space_shrink(space)))

    def add_newline(self):
        """Adds the newline nodes"""
        self.nodes.append(Glue(0, Infinity, 0))
        self.nodes.append(Penalty(0, -Infinity, 1))

    def add_nodes_from_part(self, part):
        """Handle a few characters that we want to be able to break after,
        even mid-word. self.midbreak_penalty is used to minimize these, but
        mid-morning could be split at mid-, for instance. See wordbreak_char_re
        comment above."""

        parts = wordbreak_char_re.split(part)
        *head, tail = parts
        for p, c in pairwise(head):
            self.nodes.append(HBox(p+c, self.active_font))
            self.nodes.append(Penalty(0, Infinity if self.nobreak else self.midbreak_penalty, 1))
        self.nodes.append(HBox(tail, self.active_font))

    def add_nodes_from_word(self, word):
        """Split out the nodes from a (possibly hyphenated) word, including
        splitting it further than the original whitespace splitting if
        needed."""

        if len(word)==1 and breaking_re.match(word):
            self.add_space(word)
            return

        if self.hyphenate and len(word)>6:
            words = self.hyphenator.syllables(word)
            words = fix_hyphenation(words)
        else:
            words = [word]

        *head, tail = words
        
        for part in head:
            self.add_nodes_from_part(part)
            self.nodes.append(Penalty(self.font.get_hyphen_width(), Infinity if self.nobreak else self.hyphen_penalty, 1))

        self.add_nodes_from_part(tail)

    def check_newlines(self, text):
        text = text.rstrip("\r\n")

        if "\n" in text or "\r" in text:
            print("Paragraphs cannot contain newlines. Call split() to handle multiple paragraphs.", file=sys.stderr)
            sys.exit(-1)
        return text


    def add_words_from_string(self, string):
        if not string:
            return
        if string:
            need_start = string[0]==" "
            need_end = string[-1]==" " and len(string)>1
            if need_start:
                string = string[1:]
            if need_end:
                string = string[:-1]
        all_words = breaking_re.split(string)

        if need_start:
            self.add_space()

        for word in all_words:
            self.add_nodes_from_word(word)

        if need_end:
            self.add_space()


from html.parser import HTMLParser
class RichWordSplitter(BaseWordSplitter, HTMLParser):
    def __init__(self, *args, **kwargs):
        BaseWordSplitter.__init__(self, *args, **kwargs)
        self.bold = 0
        self.italic = 0
        self.set_active_font()
        self.nodes = []
        HTMLParser.__init__(self)

    def split_paragraph(self, text):
        text = self.check_newlines(text)

        self.nodes = []
        self.feed(text)
        self.add_newline()

        return self.nodes

    def set_active_font(self):
        if self.bold and self.italic:
            self.active_font = self.font.bolditalicfont
        elif self.bold:
            self.active_font = self.font.boldfont
        elif self.italic:
            self.active_font = self.font.italicfont
        else:
            self.active_font = self.font.font
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'b':
            self.bold += 1
            self.set_active_font()
        elif tag.lower() == 'i':
            self.italic += 1
            self.set_active_font()
        elif tag.lower() == 'nb':
            self.nobreak += 1
        else:
            self.nobreak += 1
            self.handle_data(self.get_starttag_text())
            self.nobreak -= 1
    def push_nodes(self, string):
        self.add_words_from_string(string)

    def handle_endtag(self, tag):
        if tag.lower() == 'b':
            self.bold -= 1
            self.set_active_font()
        elif tag.lower() == 'i':
            self.italic -= 1
            self.set_active_font()
        elif tag.lower() == 'nb':
            self.nobreak -= 1
        else:
            self.nobreak += 1
            self.handle_data(f"</{tag}>")
            self.nobreak -= 1
    def handle_data(self, data):
        data = data.split("\n")
        for i, datum in enumerate(data):
            self.push_nodes(datum)
            if i != len(data) - 1:
                self.add_newline()

class BasicWordSplitter(BaseWordSplitter):
    def split_paragraph(self, text):
        text = self.check_newlines(text)
        self.nodes = []
        self.active_font = self.font.font

        self.add_words_from_string(text)
        self.add_newline()

        return self.nodes
