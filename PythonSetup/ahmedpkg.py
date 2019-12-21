import setuptools

with open("README.md, "r"") as fh:
	long_description = fh.read()

setuptools.setup(
name="AhmedPackage",
version="1.00",
author="Ahmed Sadiq",
description="My first python package",
long_description="This is my firts python package.",
long_description_content_type="text/markdown",
packages=setuptools.find_packages(),
classifiers=["python package"],
python_requires='>=3.0',)
