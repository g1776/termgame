#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name="termgame",
    version="0.0.1",
    description="Terminal-based graphical game engine",
    author="Gregory Glatzer",
    author_email="gregoryg323@gmail.com",
    url="",
    packages=["termgame"] + ["termgame." + pkg for pkg in find_packages(where="src")],
    package_dir={
        "termgame": "src",
    },
)
