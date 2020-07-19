#!/usr/bin/env python

import os
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'requirements.in')) as req:
    requirements = req.read().split()


setup(
    install_requires=requirements,
)
