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
    author_email="info@thoth.pub",
    url="https://github.com/thoth-pub/thoth-client",
    packages=[
        "thothlibrary",
        "thothrest",
        "thothdjango",
        "thothlibrary.thoth-0_4_2",
        "thothrest.thoth-0_4_2",
        "thothlibrary.thoth-0_5_0",
        "thothlibrary.thoth-0_6_0",
        "thothlibrary.thoth-0_8_0",
        "thothlibrary.thoth-0_8_4",
        "thothlibrary.thoth-0_9_0"
    ],
    include_package_data=True,
    install_requires=[
        "requests==2.32.3",
        "fire==0.6.0",
        "munch==3.0.0",
        "requests_mock==1.12.1",
        "ascii_magic==2.3.0",
        "graphqlclient==0.2.4",
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
