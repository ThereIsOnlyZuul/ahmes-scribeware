# Ahmes Scribeware

The purpose of this software is to facilitate the development of academic
practice work for students and teachers.

It is named in honor of Ahmes the Egyptian scribe who is was the author of
the first known written work concerning mathematical procedures.

## Prerequisites

You'll need LaTeX and Python (obviously), and a few other python packages.

This package is written in Python 3, not 2.7.

[Sympy](www.sympy.org) is used for symbolic calculations and LaTeX formatting.

[PyLaTeX](https://jeltef.github.io/PyLaTeX/current/) is used for preparing 
the LaTeX document and generating the PDFs.

## Installing

This is very much a work in progress, and I don't reccommend installing this 
in a production environment.

As this project progresses, this README will be updated with details.

## Tests

The built-in [unittest](https://docs.python.org/3/library/unittest.html) 
framework is used for testing. You can run all of the unit tests as 
described in the official documentation for that framework.

## Usage

This program is used from the command line. First identify the template you'd
like to use, then decide where you want the file to go. Then you call the
program like so:

```
	>> ahmes(.py) [template] [location]
```

You can also use the live-scribe for an interactive console experience. This
is new, and you can expect it to be buggy...

You can activate the console interactive live-scribe by not supplying a template name or location.


## Contributing

The [Code of Conduct](CONDUCT.md) applies to contributions.

I welcome pull requests, forks, etc. I am a relative newbie to Git. If you
have more exprerience and want to contribute, feel free to contat 
[me](mailto:schilke.60@gmail.com).

## ToDo

Test the code.
Make more templates.