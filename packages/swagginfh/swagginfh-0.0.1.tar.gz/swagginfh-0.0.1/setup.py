from distutils.core import setup
from setuptools import find_packages
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    
# Project name: 
name='swagginfh',

# Packages to include in the distribution: 
packages=find_packages(','),

# Project version number:
version='0.0.1',

# List a license for the project, eg. MIT License
license='MIT',

# Short description of your library: 
description='a library to read and write to .swaggin files',

# Long description of your library: 
long_description=long_description,
long_description_content_type='text/markdown',

# Your name: 
author='perigonsr',

# Your email address:
author_email='stripeysweatercat@gmail.com',

# Link to your github repository or website: 
url='https://github.com/stripeysweatercat/swaggin-fh',

# Download Link from where the project can be downloaded from:
download_url='https://github.com/stripeysweatercat/swaggin-fh',

# List of keywords: 
keywords=['swaggin', '.swaggin'],

# List project dependencies: 
install_requires=[
    'byteconvert',
],

# https://pypi.org/classifiers/ 
classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python',
]
)   