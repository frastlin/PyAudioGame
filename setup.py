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
	'install_requires': ['accessible_output2', 'pygame', 'pyinstaller'],
	#dependency_links=['hg+http://hg.q-continuum.net/accessible_output2'],
	'packages': ['pyaudiogame'],
	'scripts': [],
	'name': 'pyaudiogame'
	}

setup(include_package_data=True, **config)