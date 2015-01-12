from pywintypes import com_error
import win32gui
import win32com.client

from main import OutputError, BrailleOutput

class Jaws (BrailleOutput):
 """Braille output supporting the Jaws for Windows screen reader."""

 name = 'jaws'

 def __init__(self, *args, **kwargs):
  super (Jaws, self).__init__(*args, **kwargs)
  try:
   self.object = win32com.client.Dispatch("FreedomSci.JawsApi")
  except com_error: 
   try:
    self.object = win32com.client.Dispatch("jfwapi")
   except com_error: #give up
    raise OutputError

 def braille(self, text):
  # HACK: replace " with ', Jaws doesn't seem to understand escaping them with \
  text = text.replace('"', "'")
  self.object.RunFunction("BrailleString(\"%s\")" % text)

 def canBraille(self):
  try:
   return self.object.SayString('',0) == True or win32gui.FindWindow("JFWUI2", "JAWS") != 0 and super(Jaws, self).canBraille()
  except:
   return False
