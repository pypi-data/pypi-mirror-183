from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

#with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#    long_description = "\n" + fh.read()

VERSION = '0.7'
DESCRIPTION = 'GRL Merger tool package for integrating two GRL models'
LONG_DESCRIPTION = 'A package that allows to merge two GRL models that are written in TGRL syntax.'

# Setting up
setup(
    name="GRLMerger",
    version=VERSION,
    author="Nadeen AlAmoudi",
    author_email="<nadeenamoudi1@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'random', 'statistics', 'neattext', 'nltk', 'warnings', 'sentence_transformers'],
    keywords=['python', 'GRL', 'merging', 'semantic-matching'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)