#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      setup.py
   Description:
   Author:          dingyong.cui
   date：           2022/12/27
-------------------------------------------------
   Change Activity:
                    2022/12/27:
-------------------------------------------------
"""
import os.path

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-report-diff',
    version='1.0',
    license='BSD License',  # example license
    description='A simple Django app to diff bi report.',
    long_description=README,

    url='https://www.example.com/',
    author='Dillon',
    author_email='18721296190@163.com',

    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Django',
        'djangorestframework'
    ],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
