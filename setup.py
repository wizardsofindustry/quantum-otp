#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

import safi

setup(
    name='safi',
    version=safi.__version__,
    packages=find_packages()
)

# pylint: skip-file
