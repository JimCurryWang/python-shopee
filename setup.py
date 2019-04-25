import codecs
import os
import sys


try:
    from setuptools import setup,find_packages
except:
    from distutils.core import setup,find_packages


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
 

NAME = "pyshopee"
PACKAGES = ['hmac','hashlib','requests','urllib']
DESCRIPTION = "python implementation for Shopee Partners API."
KEYWORDS = "pyshopee,Shopee,Shopee Partners API,python-shopee"
AUTHOR = "jimcurrywang"
AUTHOR_EMAIL = "jimcurrywang@gmail.com"
URL = "https://github.com/JimCurryWang/pyshopee"
VERSION = "1.3.8"
LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    # long_description = LONG_DESCRIPTION,
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
    packages = find_packages(),
    include_package_data=True,
    zip_safe=True,
)
