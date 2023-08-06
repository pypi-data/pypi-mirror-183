# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:20:34 2022

@author: Clayton Barnes
"""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='eventlogic',
    author='Clayton Barnes',
    author_email='barnes.clayton@icloud.com',
    packages=find_packages(where='src',exclude=['eventlogic.tests']),
    version='0.1.3',
    description='Performs logical operations on event-style data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)