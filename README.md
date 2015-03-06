# Hacks and black magic to run cPython stuff with PyPy

PyPy is not as slow as CPython, so it could be useful for number crunching.
However, PyPy doesn't really support stuff like NumPy and SciPy and matplotlib,
which are also very useful in number crunching stuff. `cpyproxy` is an evil hack
to use CPython stuff in PyPy code. The heavy lifting is done by RpyC.

Usage may well break bits, pieces and living organisms.

Everything is in public domain, except stuff in `cpyproxy/fake-site` has their
own licenses, so check them out first if you're doing some evil business stuff.

## Install
    $ git clone https://github.com/jampekka/cpyproxy.git

Optionally copy `cpyproxy/cpyproxy` to some directory that's in `PYTHONPATH`.

## Usage

The simplest usage is to run your not-fully-PyPy-compliant stuff
using:

    $ pypy -m cpyproxy.black_magic <your_script.py>

See the examples below for different kinds of insanity.

## Examples

After install, do `cd cpyproxy` and try out these and pray. If you have
matplotlib installed, they should end up showing a picture. If not,
you'll get an error.

### Automagic black magic
    $ pypy -m cpyproxy.black_magic test_no_magic.py
### Manual black magic
    $ pypy test_black_magic.py
### Import magic
    $ pypy test_black_magic.py
### Boring manual labor
    $ pypy test_explicit.py
