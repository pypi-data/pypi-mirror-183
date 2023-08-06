#!/usr/bin/env python

from setuptools import setup
import os.path
import codecs

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='deepti_utils',
      version=get_version("deepti_utils/__init__.py"),
      description='Package of utility functions for Deepti Kannan',
      long_description=readme(),
      author='Deepti Kannan',
      author_email='dk.kannan97@gmail.com',
      packages=['deepti_utils'],
      license='MIT',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Topic :: Utilities'
      ],
      url='https://github.com/kannandeepti/deepti_utils',
      install_requires=['numpy', 'matplotlib']
     )