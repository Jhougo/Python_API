#! /usr/bin/env python

from distutils.core import setup

VERSION = "2.3.1"

DESCRIPTION = """\
dbfpy is a python-only module for reading and writing DBF-files.
It was created by Jeff Kunce and then modified by Hans Fiby
and Yaroslav Samchuk.

dbfpy can read and write simple DBF-files.  The `DBF-format
<http://www.clicketyclick.dk/databases/xbase/format/>`_
was developed about 30 years ago and was used by a number
of simple database applications (dBase, Foxpro, Clipper, ...).
The basic datatypes numbers, short text, and dates are available.
Many different extensions have been used; dbfpy can read and write
only simple DBF-files.
"""

def run():
    setup(name="dbfpy",
        version=VERSION,
        description="Access .DBF (dBase) files from python",
        url="http://dbfpy.sourceforge.net/",
        license="public domain",
        author="Jeff Kunce",
        # XXX cannot add maintainer field to PKG-INFO:
        # it overwrites the author name on PyPI
        # because author's email is not known.
        #maintainer="dbfpy users mailing list",
        maintainer_email="dbfpy-users@lists.sourceforge.net",
        packages=["dbfpy"],
        long_description=DESCRIPTION,
        download_url="https://sourceforge.net/projects/dbfpy/files/dbfpy/%s/"
            % VERSION,
        platforms=["OS Independent"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: Public Domain",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Database",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )

if __name__ == "__main__":
    run()

# vim: set et sts=4 sw=4 :
