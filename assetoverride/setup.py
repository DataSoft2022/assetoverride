from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in assetoverride/__init__.py
from assetoverride import __version__ as version

setup(
	name="assetoverride",
	version=version,
	description="asdf",
	author="asdf",
	author_email="sd",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
