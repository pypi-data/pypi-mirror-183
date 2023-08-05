# PyParagraph

## Knuth Plass line-breaking for Python, with PIL rendering

This package is an attempt to make it easy to render paragraphs to a PIL Image in Python, with excellent line-breaking via the [Knuth-Plass algorithm](http://www.eprg.org/G53DOC/pdfs/knuth-plass-breaking.pdf). This algorithm is used by TeX and LaTeX, and is commonly called the TeX line-breaking algorithm or the LaTeX line-breaking algorithm). A simple greedy wrapping algorithm is available as a fallback. Console/text output is supported as well as PIL output.

Thanks to Bram Stein for inspiration, via [his JavaScript implementation](https://github.com/bramstein/typeset/) of the algoritm.

Example, typeset with the naïve greedy line-breaking algorithm:

![An image of a paragraph, typeset with a greedy algoritm](/images/tom_sawyer_greedy.png "Tom Sawyer Excerpt: Greedy Linebreaking")

The same, typeset with Knuth-Plass. Note the more even line-lengths:

![An image of a paragraph, typeset with Knuth-Plass's algoritm](/images/tom_sawyer_kp.png "Tom Sawyer Excerpt: Knuth-Plass Linebreaking")

## Usage

Simple command-line examples, either after installation or from the `src/` directory in the tree:

`python -m pyparagraph -f ../data/tom_sawyer.txt -i tom_sawyer.png`

Render wrapped text from `../data/tom_sawyer.txt` to image `tom_sawyer.png`, in default font and size.

`python -m pyparagraph -f ../data/tom_sawyer.txt --font Calibri --margin 20 --font-size 24pt --width 600 --image tom_sawyer.png`

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
textwrap.render_image(text, filename="gettysburg.png", margin=20)


# Render to a PIL Image:

from PIL import Image
our_image = Image.new("RGBA", (800,800), "white")

textwrap.render_image(text, img=our_image)
our_image.save("gettysburg2.png")
```
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
