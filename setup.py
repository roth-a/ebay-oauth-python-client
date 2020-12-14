# coding: utf-8

"""
   eBay oauth SDK adapted to Python 3 and to be installed with pip 
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ebayoauth"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["selenium >= 3.141.0", "requests >= 2.21.0", "PyYAML >= 5.1"]

setup(
    name=NAME,
    version=VERSION,
    description="Realarb fork for ebayoauth",
    author="eBay",
    author_email="",
    url="",
    keywords=[],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="Notes: this is not an official distribution of the eBay oauth Python SDK"
)