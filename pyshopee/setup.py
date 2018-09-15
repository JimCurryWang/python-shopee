import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup


 
NAME = "python-shopee"
PACKAGES = ["hmac","hashlib","requests","urllib"]
DESCRIPTION = "python implementation for Shopee Partners API."
LONG_DESCRIPTION = read("README.md")
KEYWORDS = "Shopee,Partners API,Shopee Partners API,python-shopee,pyshopee"
AUTHOR = "jimcurrywang"
AUTHOR_EMAIL = "jimcurrywang@gmail.com"
URL = "https://github.com/JimCurryWang/python-shopee"
VERSION = "1.2.2"
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
