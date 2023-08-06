from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Kumpulan rumus'
LONG_DESCRIPTION = 'Rumus bangun datar dan bangun ruang'

# Setting up
setup(
    name="Rumus_12",
    version=VERSION,
    author="heybudie2",
    author_email="<lhrbdipras2@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)