from setuptools import setup, find_packages
#from setuptools.command.develop import develop
#from setuptools.command.install import install
#from subprocess import check_call

#class PostDevelopCommand(develop):
#	"""Post-installation for development mode."""
#	def run(self):
#		check_call("pip install pywin32")
#		develop.run(self)

#class PostInstallCommand(install):
#	"""Post-installation for installation mode."""
#	def run(self):
#		check_call("pip install pywin32")
#		install.run(self)

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
#	'cmdclass': {
#		'develop': PostDevelopCommand,
#		'install': PostInstallCommand,
#	},
	'install_requires': ['pygame'],
}

setup(include_package_data=True, **config)