from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = ' ini adalah rumus bangun ruang dan bangun datar'
LONG_DESCRIPTION = 'kumpulan rumus.'

# Setting up
setup(
    name="BELAJAR_bangundatar-bangunruang",
    version=VERSION,
    author="Abu Sobri Al Jamali",
    author_email="<abusobri007@gmaiil.com>",
    description=DESCRIPTION,
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)