#!/usr/bin/env python
"""Thoth package definition"""

import os
from setuptools import setup
from thothlibrary import __version__, __license__

ROOTDIR = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(ROOTDIR, "README.md")) as in_file:
    LONG_DESCRIPTION = in_file.read()

setup(
    name="thothlibrary",
    version=__version__,
    description="Python client for Thoth's GraphQL API",
    author="Javier Arias",
    author_email="javier@arias.re",
    packages=["thothlibrary"],
    install_requires=["graphqlclient", "requests"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=__license__,
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
