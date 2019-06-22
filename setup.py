# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.org') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SunFlwr',
    version='0.1.0',
    description='Real State Apraising tool',
    long_description=readme,
    author='Sergio Yanez',
    author_email='seryan.1115@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
