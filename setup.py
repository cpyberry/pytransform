"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pybencode

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


import os
from setuptools import setup


NAME = "pytransform"


def get_absolute_path(*paths):
	root_dir = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(root_dir, *paths)
	return path


info = {}
with open(get_absolute_path(NAME, "__info__.py")) as f:
	exec(f.read(), info)


with open(get_absolute_path("README.md"), encoding="utf-8") as f:
	long_description = f.read()


setup(
	name=info["__title__"],
	description=info["__description__"],
	long_description=long_description,
	long_description_content_type="text/markdown",
	url=info["__url__"],
	license=info["__license__"],
	version=info["__version__"],
	author=info["__author__"],
	author_email=info["__author_email__"],
	packages=[NAME],
	python_requires=info["__python_requires__"],
	zip_safe=False,
	include_package_data=True,
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: Apache Software License",
		"Natural Language :: English",
		"Natural Language :: Japanese",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: Implementation",
		"Topic :: Software Development :: Libraries :: Python Modules"
	]
)
