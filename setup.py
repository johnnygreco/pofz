#! /usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pofz",
    version='0.1',
    author="Johnny Greco",
    author_email="jgreco.astro@gmail.com",
    packages=["pofz"],
    url="https://github.com/johnnygreco/pofz",
    license="MIT",
    description="Estimate p(z) of galaxy sample",
)
