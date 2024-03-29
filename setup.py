# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in gospafe/__init__.py
from gospafe import __version__ as version

setup(
	name='gospafe',
	version=version,
	description='Internal Application for The Company GOSPAFE',
	author='GOSPAFE',
	author_email='admin@gospafe.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
