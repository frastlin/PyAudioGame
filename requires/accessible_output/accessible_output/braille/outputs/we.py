from pywintypes import com_error
import win32com.client
import win32gui

from main import OutputError, BrailleOutput

class WindowEyes (BrailleOutput):
 """Braille output which supports Window Eyes"""

 name = ' Window-Eyes'

 def __init__(self, *args, **kwargs):
  super(WindowEyes, self).__init__(*args, **kwargs)
  #This tries to load window eyes if it's not active, but it's still available on your system, so to prevent:
  if self.canBraille():
   try:
    self.object = win32com.client.Dispatch("WindowEyes.Application")
   except com_error:
    raise OutputError

 def canBraille(self):
  try:
   return win32gui.FindWindow("GWMExternalControl", "External Control") != 0 and super(WindowEyes, self).canBraille()
  except:
   return False

 def braille (self, text):
  try:
   self.object.Display(text)
  except:
   pass
