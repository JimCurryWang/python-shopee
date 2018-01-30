import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup


 
NAME = "python-shopee"
PACKAGES = ["hmac","hashlib","requests","urllib"]
DESCRIPTION = "Shopee Partners API python implementation , This is an unofficial Python implementation for the Shopee Partner REST API."
LONG_DESCRIPTION = read("README.md")
KEYWORDS = "Shopee,Partners API,Shopee Partners API,python-shopee"
AUTHOR = "jimcurrywang & ketu"
AUTHOR_EMAIL = "jimcurrywang@gmail.com"
URL = "https://github.com/JimCurryWang/python-shopee"
VERSION = "1.0.0"
LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
