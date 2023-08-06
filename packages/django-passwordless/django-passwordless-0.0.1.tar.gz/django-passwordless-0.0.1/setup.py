# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name="django-passwordless",
    version="0.0.1",
    author="Jon Combe",
    author_email="me@joncombe.net",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    license="MIT licence, see LICENCE file",
    description="Secure passwordless login for Django",
    long_description="View readme on github: https://github.com/joncombe/django-passwordless",
    url="https://github.com/joncombe/django-passwordless",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)
