# PyParagraph

## Knuth Plass line-breaking for Python, with PIL rendering

This package is an attempt to make it easy to render paragraphs to a PIL Image in Python, with excellent line-breaking via the [Knuth-Plass algorithm](http://www.eprg.org/G53DOC/pdfs/knuth-plass-breaking.pdf). This algorithm is used by TeX and LaTeX, and is commonly called the TeX line-breaking algorithm or the LaTeX line-breaking algorithm). A simple greedy wrapping algorithm is available as a fallback. Console/text output is supported as well as PIL output.

## Installation

`pip install pyparagraph`

Note that a relatively recent (as of December 2022) version of setuptools is required: `pip install --upgrade setuptools` if you get errors during the install, then try again.

## Usage & References

See [the gitlab home page](https://gitlab.com/sumnerh1/pyparagraph) for documentation.

## License

This software is licensed under the MIT License.  Copyright (c) 2022, G. Sumner Hayes.

See the LICENSE.txt for full details.
