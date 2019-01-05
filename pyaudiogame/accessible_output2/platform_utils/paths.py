import inspect
import platform
import os
import sys

from functools import wraps

def merge_paths(func):
 @wraps(func)
 def merge_paths_wrapper(*a, **k):
  return unicode(os.path.join(func(**k), *a))
 return merge_paths_wrapper

def windows_path(path_id):
 import ctypes
 path = ctypes.create_unicode_buffer(260)
 if ctypes.windll.shell32.SHGetFolderPathW(0, path_id, 0, 0, ctypes.byref(path)) != 0:
 	raise ctypes.WinError()
 return path.value

def app_data_path(app_name=None):
 """Cross-platform method for determining where to put application data."""
 """Requires the name of the application"""
 plat = platform.system()
 if plat == 'Windows':
  path = windows_path(0x01a)
 elif plat == 'Darwin':
  path = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support')
 elif plat == 'Linux':
  path = os.path.expanduser('~')
  app_name = '.%s' % app_name.replace(' ', '_')
 return os.path.join(path, app_name)

def prepare_app_data_path(app_name):
 """Creates the application's data directory, given its name."""
 dir = app_data_path(app_name)
 if not os.path.exists(dir):
  os.mkdir(dir)

def is_frozen():
 """Return a bool indicating if application is compressed"""
 import imp
 return hasattr(sys, 'frozen') or imp.is_frozen("__main__")

def get_executable():
 if is_frozen():
  return sys.executable
 return sys.argv[0]

def get_module():
 return inspect.stack()[2][1]

def app_path():
 """Always determine the path to the main module, even when run with py2exe or otherwise frozen"""
 return os.path.abspath(os.path.dirname(get_executable()))

def module_path():
 return os.path.abspath(os.path.dirname(get_module()))

def executable_path():
 return os.path.join(app_path(), get_executable())

def ensure_path(path):
  if not os.path.exists(path):
   os.makedirs(path)

def documents_path():
 """On windows, returns the path to My Documents. On OSX, returns the user's Documents folder. For anything else, returns the user's home directory."""
 plat = platform.system()
 if plat == 'Windows':
  return windows_path(0x005)
 elif plat == 'Darwin':
  path = os.path.join(os.path.expanduser('~'), 'Documents')
 else:
  path = os.path.expanduser('~')
 return path
