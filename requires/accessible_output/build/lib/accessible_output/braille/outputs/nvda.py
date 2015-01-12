from platform_utils import libloader, paths
import os

from main import OutputError, BrailleOutput

class NVDA (BrailleOutput):

 """Brailler which supports The NVDA screen reader"""

 name = 'NVDA'

 def __init__(self, *args, **kwargs):
  library_path = os.path.join(paths.module_path(), '..', '..', 'lib')  
  try:
   self.dll = libloader.load_library('nvdaControllerClient32', library_path)
  except Exception as e:
   raise OutputError(e)

 def braille(self, text):
  self.dll.nvdaController_brailleMessage(unicode(text))

 def canBraille(self):
  try:
   return self.dll.nvdaController_testIfRunning() == 0 and super(NVDA, self).canBraille()
  except:
   return False

