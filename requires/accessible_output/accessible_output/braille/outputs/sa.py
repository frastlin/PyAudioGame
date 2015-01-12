from main import BrailleOutput, OutputError
from platform_utils import libloader, paths
import os

class SystemAccess (BrailleOutput):

 """Supports Brailling to System Access."""

 name = 'System Access'

 def __init__(self, *args, **kwargs):
  super(SystemAccess, self).__init__(*args, **kwargs)
  library_path = os.path.join(paths.module_path(), '..', '..', 'lib')
  try:
   self.dll = libloader.load_library('SAAPI32', library_path)
  except Exception as e:
   raise OutputError(e)

 def braille(self, text):
  self.dll.SA_BrlShowTextW(unicode(text))

 def canBraille(self):
  try:
   return self.dll.SA_IsRunning() and super(SystemAccess, self).canBraille()
  except:
   return False
