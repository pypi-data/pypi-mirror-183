# PyParagraph

## Knuth Plass line-breaking for Python, with PIL rendering

This package is an attempt to make it easy to render paragraphs to a PIL Image in Python, with excellent line-breaking via the [Knuth-Plass algorithm](http://www.eprg.org/G53DOC/pdfs/knuth-plass-breaking.pdf). This algorithm is used by TeX and LaTeX, and is commonly called the TeX line-breaking algorithm or the LaTeX line-breaking algorithm). A simple greedy wrapping algorithm is available as a fallback. Console/text output is supported as well as PIL output.

Thanks to Bram Stein for inspiration, via [his JavaScript implementation](https://github.com/bramstein/typeset/) of the algoritm.

Example, typeset with the naïve greedy line-breaking algorithm:

![An image of a paragraph, typeset with a greedy algoritm](/images/tom_sawyer_greedy.png "Tom Sawyer Excerpt: Greedy Linebreaking"){: .shadow}

The same, typeset with Knuth-Plass. Note the more even line-lengths:

![An image of a paragraph, typeset with Knuth-Plass's algoritm](/images/tom_sawyer_kp.png "Tom Sawyer Excerpt: Knuth-Plass Linebreaking"){: .shadow}

## Installation

`pip install pyparagraph`

Note that a relatively recent (as of December 2022) version of setuptools is required: `pip install --upgrade setuptools` if you get errors during the install, then try again.

## Usage

Simple command-line examples, either after installation or (to test without installing, from the `src/` directory in the tree use `python -m pyparagraph` in lieu of `pyparagraph`):

`pyparagraph -f ../data/tom_sawyer.txt --width 80`

Prints out on console, lines wrapped to 80 characters.

`pyparagraph -f ../data/tom_sawyer.txt -i tom_sawyer.png`

Render wrapped text from `../data/tom_sawyer.txt` to image `tom_sawyer.png`, in default font and size.

`pyparagraph -f ../data/tom_sawyer.txt --font Calibri --margin 20 --font-size 24pt --width 600 --image tom_sawyer.png`

Generates the image `tom_sawyer.png` from the text in the file `tom_sawyer.txt`, using 24pt Calibri as the font, on a 640px wide image (600px of text width, with 20 px margins on each side). The image will be as tall as needed to contain the text and margins.

Simple library example
```python
from pyparagraph import TextWrap

args = {
    "font": "Lato",
    "font-size": "24px",
    "width": "600"
}

text = """Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this."""

# Render to a file of the given name
textwrap = TextWrap.text_wrapper(args)
textwrap.render_image_to_file(text, filename="gettysburg.png", margin=20)


# Render to a PIL Image:

from PIL import Image
our_image = Image.new("RGBA", (800,800), "white")

textwrap.render_image(text, img=our_image)
our_image.save("gettysburg2.png")
```

Three major components handle the process:

_Splitters_ split a string into nodes. Two are available: RichWord (default) and BasicWord. The RichWord splitter attempts to treat HTML-style i and b tags as italic and bold markers, and also allows <nb> to designate a non-breaking string. The Basic splitter treats everything as plain text. Use `--splitter BasicWord` to override the default (or pass `{"splitter": "BasicWord"}` in the args in the API).

_Wrappers_ handle the wrapping of nodes into lines. Two are available: KnuthPlass (default) and Greedy. Greedy is the naïve greedy algorithm: words are layed out until the next one won't fit within the specified width, and then a line break is inserted. KnuthPlass uses the Knuth–Plass optimal breaking algorithm.

_Renderers_ render the lines. TextWrap is the only renderer currently. It has 3 relevant methods: `render_image` writes to a PIL `Image`. If you specify a `img` parameter, it must be a pre-allocated PIL `Image`. The text will be rendered to that image, which you can use (or write to a file) as desired. If img is None, an appropriate size image is created.

`render_image_to_file` takes a filename, and writes out an image to that file. It's essentially equivalent to `render_image` followed by calling `save` on the result.

`render_text` returns a list of lines. It's up to the user to render those using the same font and size as were passed to the code.

Fonts are found via matplotlib's `font_manager`, which should find system-installed fonts by name ('Liberation Sans', 'Calibri', 'Lucida Grande', etc) in normal default locations on Linux, OS X, and Windows (and hopefully on other common Unix flavors). If that fails, you'll have to fight with matplotlib or specify complete paths on your own (passing, e.g., `/usr/share/fonts/truetype/lato/Lato-Regular.ttf` instead of "Lato").  If you do the latter and pass it a base/regular font, the code will at least try to look for the Bold, Italic, and BoldItalic font faces in the same location with a variety of substitutions so you don't have to sort that all out manually. 

If you pass in the `pyparagraph.NonProportional` singleton as the value of font (or if you render as text with no font specified), the code will assume a monospace font and will treat the width as a character width rather than a pixel width. 

## Help

Run with `--help` for verbose help:

```
options:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  Pull text to wrap from FILE
  --image IMAGE, -i IMAGE
                        Generate image in file named IMAGE. Image filename
                        must end with .png
  --margin MARGIN       Have a margin of width MARGIN around the text (image
                        mode only)
  --hyphenate, -H       Attempt to hyphenate words with PyHyphen.
  --width WIDTH, -w WIDTH
                        Width to render. This is in pixels in image mode, or
                        in characters in text mode.
  --font FONT, -F FONT  Font to use. Can be a font face (Calibri, Lucida
                        Grande, Liberation Sans, etc) or a full path to a .ttf
                        or .otf file. If you pass it a regular/normal weight,
                        it'll try to find the bold/italic variants in the same
                        location.
  --font-size FONT_SIZE
                        Font size, either points or pixels, e.g. 12pt or 16px

Advanced Options:
  --splitter {RichWord,BasicWord}
                        Which text splitter to use. RichWord treats <b> and
                        <i> as bold/italic and <nb> for non-breaking runs.
                        BasicWord is a simple plaintext splitter (splits at
                        breaking whitespace only).
  --wrapper {KnuthPlass,Greedy}
                        Which word-wrapping algorithm to use; KnuthPlass is
                        the TeX algoritm, Greedy is simple greedy-matching
  --no-warn-locale, -W  Suppress warnings about being unable to set locale
  --verbose, -v         Print extra info
  --debug               Print debugging info
  --test, -t            Run on test data with text and image output
  --language LANGUAGE, -l LANGUAGE
                        Language to use for hyphenation (e.g. en_GB, ja_JP,
                        de_DE, fr_FR, zh_HANS, es_ES, etc); defaults to
                        platform locale, you can often set the LC_ALL
                        environment variable or change system configuration to
                        set that.
  --hyphen-penalty HYPHEN_PENALTY
                        Penalty factor for hyphenation (lower results in more
                        hyphenation; default 100)
  --midbreak-penalty MIDBREAK_PENALTY
                        Penalty factor for breaking after a hard - or — (lower
                        results in more breaks; default 25)

```
## Limitations

This is brand new. It works in expected cases, but should be considered experimental code. 

In some pathological cases, K–P cannot find a fit for the text. In those cases, the code falls back to a naïve Greedy matching algorithm.

## Requirements

This requires [the PyHyphen package](https://github.com/dr-leo/PyHyphen) by Dr. Leo for hyphenation (which is optional). "pip install pyhyphen" should install it. The first time you run with hyphenation for a given language, it will fetch the hyphenation library for that language.

The [matplotlib package](https://github.com/matplotlib/matplotlib) is optional but allows much nicer font support.

## References

* [Breaking Paragraphs into Lines](http://www.eprg.org/G53DOC/pdfs/knuth-plass-breaking.pdf)
* [TeX line breaking algorithm in JavaScript](https://github.com/bramstein/typeset/)
* [Knuth & Plass line-breaking Revisited](http://defoe.sourceforge.net/folio/knuth-plass.html)
* [Digital Typography, by Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/dt.html)

## License

This software is licensed under the MIT License.

Copyright (c) 2022, G. Sumner Hayes.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
