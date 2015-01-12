from setuptools import setup, find_packages

__version__ = 0.240

setup(
 name = 'platform_utils',
 version = __version__,
 description = 'Cross-platform utilities for accomplishing basic tasks',
 package_dir = {'platform_utils': 'platform_utils'},
 packages = find_packages(),
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
'Topic :: Software Development :: Libraries'
],
)
