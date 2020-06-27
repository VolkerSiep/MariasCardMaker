#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:41:15 2020

@author: volker
"""

# stdlib modules
import setuptools

# internal modules
from mcm.version import version

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages(include=["mdm.*", "mdm"])

setuptools.setup(
    name="mdm",
    version=version,
    author="Volker Siepmann",
    author_email="volker.siepmann@yara.com",
    description="Card maker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VolkerSiep/MariasCardMaker",
    packages=packages,
    package_data={'mdm': ['Zangoose.png']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    install_requires=[
        "python>=3.7",
        "wxpython>=4.0.7",
        "openpyxl>=3.0"
        ]
)
