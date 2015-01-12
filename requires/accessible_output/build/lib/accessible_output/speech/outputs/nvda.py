import os
from platform_utils import libloader, paths
from main import OutputError, ScreenreaderSpeechOutput

class NVDA (ScreenreaderSpeechOutput):
 """Supports The NVDA screen reader"""

 name = 'NVDA'

 def __init__(self, *args, **kwargs):
  super(NVDA, self).__init__(*args, **kwargs)
  library_path = os.path.join(paths.module_path(), '..', '..', 'lib')
  try:
   self.dll = libloader.load_library('nvdaControllerClient32', library_path)
  except Exception as e:
   raise OutputError(e)

 def speak(self, text, interrupt=0):
  if interrupt:
   self.silence()
  self.dll.nvdaController_speakText(unicode(text))

 def silence(self):
  self.dll.nvdaController_cancelSpeech()

 def canSpeak(self):
  try:
   return self.dll.nvdaController_testIfRunning() == 0 and super(NVDA, self).canSpeak()
  except:
   return False
