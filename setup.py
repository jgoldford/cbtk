from setuptools import find_packages, setup

setup(
	name = "cbtk",
	version = '0.0',
	description = 'Python package containing common functions used for analysis work',
	url = 'https://github.com/jgoldford/cbtk/',
	author = 'Joshua E. Goldford',
	author_email = 'goldford.joshua@gmail.com',
	packages = find_packages(),
	install_requires = [],
	include_package_data = True,
)