from setuptools import setup, find_packages
from glob import glob
from platform import system
import sys

_system = system()

install_requires = ['platform_utils']
if _system == 'Darwin':
 install_requires += ['appscript']
elif _system == 'Windows':
 install_requires += ['pywin32']
else:
 install_requires = []


setup(
 name = 'accessible_output',
 author = 'Christopher Toth',
 author_email = 'q@qwitter-client.net',
 version = '0.7.8',
 url = 'http://www.qwitter-client.net',
 description = 'Library to provide speech and braille output to a variety of different screen readers and other accessibility solutions.',
 long_description = open('README.txt').read(),
 package_dir = {'accessible_output':'accessible_output'},
 packages = find_packages(),
 package_data = {"accessible_output":["lib/*"]},
 classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
'Topic :: Adaptive Technologies',
'Topic :: Software Development :: Libraries'
],
 install_requires = install_requires,
)
