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
	'version': '0.01a',
	'install_requires': ['pygame'],
#	'dependency_links': ['https://github.com/frastlin/accessible_output2/tarball/master#egg=accessible_output2-0.12.dev0'],
	'dependency_links': ['git+https://github.com/frastlin/accessible_output2.git@master'],

	#accessible_output2 is broken and accessible_output is in packages.
	#can't get the links to an hg repo to work for some reason...
#	dependency_links=['hg+http://hg.q-continuum.net/accessible_output2/'],
	#Added the accessible_output to the packages for now, will take it out when the above work with accessible_output2
	'packages': ['pyaudiogame', 'pyaudiogame/ui', 'pyaudiogame/templates', 'pyaudiogame/helper', 'requires/accessible_output', 'requires/libloader/libloader', 'requires/platform_utils/platform_utils'],
	'scripts': [],
	'name': 'pyaudiogame'
	}

setup(include_package_data=True, **config)