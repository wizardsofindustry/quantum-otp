#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

import otp

setup(
    name='otp',
    version=otp.__version__,
    packages=find_packages()
)

# pylint: skip-file
