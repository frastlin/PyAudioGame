from setuptools import setup, find_packages
from setuptools.command.develop import develop as _develop
from setuptools.command.install import install as _install
from subprocess import check_call

# these post commands are to install pywin32 if the user doesn't already have it.
# https://stackoverflow.com/questions/46542657/python-package-with-pywin32-or-pypiwin32-dependency/54049186#54049186
#post develop command
class develop(_develop):
	"""Post-installation for development mode."""
	def run(self):
		check_call("pip install pywin32")
		develop.do_egg_install(self)
#		it may be .run(self) instead.

# post install command
class install(_install):
	"""Post-installation for installation mode."""
	def run(self):
		check_call("pip install pywin32")
		install.do_egg_install(self)

config = {
	'description': 'PyAudioGame is a toolkit for making audio games in python.',
	'author': 'Brandon Keith Biggs',
	'url': 'https://github.com/frastlin/PyAudioGame',
	'download_url': 'https://codeload.github.com/frastlin/PyAudioGame/zip/master',
	'author_email': 'brandonkeithbiggs@gmail.com',
	'version': '0.0.2',
	'license': 'MIT',
	'packages': find_packages(),
	'package_data': {'pyaudiogame': ['accessible_output2/lib/*']},
	"zip_safe": False,
	'scripts': [],
	'name': 'pyaudiogame',
	'cmdclass': {
		'develop': develop,
		'install': install,
	},
	'install_requires': ['pygame'],
}

setup(include_package_data=True, **config)