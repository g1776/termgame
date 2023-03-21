#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
from pathlib import Path


def get_install_requires():
    with open("./termgame/requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="termgame",
    version="0.0.3",
    description="Terminal-based graphical game engine",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Gregory Glatzer",
    author_email="gregoryg323@gmail.com",
    url="",
    packages=["termgame"] + ["termgame." + pkg for pkg in find_packages(where="termgame/src")],
    package_dir={
        "termgame": "termgame/src",
    },
    install_requires=get_install_requires(),
)
