import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
name="ahmedpkg",
version="1.00",
author="Ahmed Sadiq",
description="My first python package",
long_description="This is my firts python package.",
long_description_content_type="text/markdown",
packages=setuptools.find_packages(),
classifiers=["Programming Language :: Python :: 3"],
python_requires='>=3.0',)
