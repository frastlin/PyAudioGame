try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'PyAudioGame is a toolkit for making audio games in python.',
	'author': 'Brandon Keith Biggs',
	'url': 'https://github.com/frastlin/PyAudioGame',
	'download_url': 'https://codeload.github.com/frastlin/PyAudioGame/zip/master',
	'author_email': 'brandonkeithbiggs@gmail.com',
	'version': '0.01',
	'install_requires': ['accessible_output', 'pygame', 'pyinstaller'],
	'packages': ['pyaudiogame'],
	'scripts': [],
	'name': 'pyaudiogame'
	}

setup(include_package_data=True, **config)