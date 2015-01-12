import os
from platform_utils import libloader, paths

from main import OutputError, ScreenreaderSpeechOutput

class SystemAccess (ScreenreaderSpeechOutput):
 """Supports System Access and System Access Mobile"""

 name = 'System Access'

 def __init__(self, *args, **kwargs):
  super(SystemAccess, self).__init__(*args, **kwargs)
  library_path = os.path.join(paths.module_path(), '..', '..', 'lib')  
  try:
   self.dll = libloader.load_library('SAAPI32', library_path)
  except Exception as e:
   raise OutputError(e)

 def speak(self, text, interrupt=0):
  if self.dll.SA_IsRunning():
   self.dll.SA_SayW(unicode(text))

 def canSpeak(self):
  try:
   return self.dll.SA_IsRunning() and super(SystemAccess, self).canSpeak()
  except:
   return False
