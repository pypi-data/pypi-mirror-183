#!/usr/bin/env python3

from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()
    
VERSION = '0.0.1'
DESCRIPTION = 'Creating GUI designs on the fly'
LONG_DESCRIPTION = 'A package that allows you to build simple GUI apps utilizing basic classes and functions.'

# Setting up
setup(
    name='guiq',
    version=VERSION,
    author='multi-threaded (Matt Goyer)',
    author_email='matthew.goyer1@gmail.com',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'gui', 'simple', 'gui designer'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)