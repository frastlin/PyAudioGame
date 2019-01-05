from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


class PostDevelopCommand(develop):
	"""Post-installation for development mode."""
	def run(self):
		check_call("pip install pywin32")
		develop.run(self)

class PostInstallCommand(install):
	"""Post-installation for installation mode."""
	def run(self):
		check_call("pip install pywin32")
		install.run(self)

config = {
	'description': 'PyAudioGame is a toolkit for making audio games in python.',
	'author': 'Brandon Keith Biggs',
	'url': 'https://github.com/frastlin/PyAudioGame',
	'download_url': 'https://codeload.github.com/frastlin/PyAudioGame/zip/master',
	'author_email': 'brandonkeithbiggs@gmail.com',
	'version': '0.01',
	'install_requires': ['pygame', 'inputs', 'accessible_output2'],
	'dependency_links': ['https://github.com/frastlin/accessible_output2/tarball/master#egg=accessible_output2-0.12', 'https://github.com/frastlin/inputs/tarball/master#egg=inputs-0.5'],
#	'dependency_links': ['git+https://github.com/frastlin/accessible_output2.git@master'],

	'packages': find_packages(),
	'scripts': [],
	'name': 'pyaudiogame',
	'cmdclass': {
		'develop': PostDevelopCommand,
		'install': PostInstallCommand,
	},
}

setup(include_package_data=True, **config)