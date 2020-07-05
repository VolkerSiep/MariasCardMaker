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

packages = setuptools.find_packages(include=["mcm"])

setuptools.setup(
    name="mcm",
    version=version,
    author="Volker Siepmann",
    author_email="volker.siepmann@gmail.com",
    description="Maria's Card maker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VolkerSiep/MariasCardMaker",
    packages=packages,
    package_data={'mcm': ['Zangoose.png']},
    # data_files=[('', ['mcm/Zangoose.png'])],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
