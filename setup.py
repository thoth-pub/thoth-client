#!/usr/bin/env python
"""Thoth package definition"""

import os
from setuptools import setup
from thothlibrary import __version__

ROOTDIR = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(ROOTDIR, "README.md")) as in_file:
    LONG_DESCRIPTION = in_file.read()

setup(
    name="thothlibrary",
    version=__version__,
    description="Python client for Thoth's APIs",
    author="Javier Arias, Martin Paul Eve",
    author_email="javier@arias.re",
    packages=[
        "thothlibrary",
        "thothrest",
        "thothdjango",
        "thothlibrary.thoth-0_4_2",
        "thothrest.thoth-0_4_2",
        "thothlibrary.thoth-0_5_0",
        "thothlibrary.thoth-0_6_0",
        "thothlibrary.thoth-0_8_0"
    ],
    include_package_data=True,
    install_requires=["graphqlclient", "requests", "munch"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
