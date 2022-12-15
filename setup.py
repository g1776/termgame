#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
from pathlib import Path

setup(
    name="termgame",
    version="0.0.1",
    description="Terminal-based graphical game engine",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Gregory Glatzer",
    author_email="gregoryg323@gmail.com",
    url="",
    packages=["termgame"]
    + ["termgame." + pkg for pkg in find_packages(where="termgame/src")],
    package_dir={
        "termgame": "termgame/src",
    },
    install_requires=[
        "Colr==0.9.1",
        "cursor==1.3.5",
        "keyboard==0.13.5",
        "numpy==1.22.3",
        "Pillow==9.3.0",
        "pymunk==6.4.0",
        "python-dotenv==0.21.0",
    ],
)
