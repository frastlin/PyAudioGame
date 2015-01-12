import output
import os
from glob import glob

import braille
import speech

__all__ = ["braille", "speech"]
__author__ = "Christopher Toth"
__version__ = 0.6

def py2exe_datafiles():
 import accessible_output
 path = os.path.join(accessible_output.__path__[0], 'lib', '*.dll')
 results = glob(path)
 dest_dir = os.path.join('accessible_output', 'lib')
 return [(dest_dir, results)]
