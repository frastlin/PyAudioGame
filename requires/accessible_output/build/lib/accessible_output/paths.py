
import os.path
import sys

def root(file=None):

 if hasattr(sys, "frozen"):
  from win32api import GetModuleFileName
  path = os.path.dirname(GetModuleFileName(0))
 else:
  path = os.path.split(os.path.realpath(__file__))[0]

 if file:
  path = os.path.join(path, file)
 return path
