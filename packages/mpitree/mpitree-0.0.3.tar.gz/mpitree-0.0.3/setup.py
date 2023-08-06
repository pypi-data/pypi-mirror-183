#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mpitree",
    version="0.0.3",
    author="Jason Duong",
    licence="MIT",
    author_email="my.toe.ben@gmail.com",
    description="A Parallel Decision Tree implementation using MPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["mpitree"],
    url="https://github.com/duong-jason/mpitree",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["graphviz", "matplotlib", "mpi4py", "pandas", "scikit-learn"],
    python_requires=">=3.8",
    extras_require={"testing": ["pytest"]},
    include_package_data=True,
)
