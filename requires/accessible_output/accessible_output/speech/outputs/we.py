from accessible_output.output import OutputError
from pywintypes import com_error
import win32gui
import win32com.client

from main import ScreenreaderSpeechOutput

class WindowEyes (ScreenreaderSpeechOutput):
 """Speech output supporting the WindowEyes screen reader"""

 name = 'Window-Eyes'

 def __init__(self, *args, **kwargs):
  super(WindowEyes, self).__init__(*args, **kwargs)
  try:
   self.object = win32com.client.Dispatch("gwspeak.speak")
  except com_error:
   raise OutputError

 def speak(self, text, interrupt=0):
  if interrupt:
   self.silence()
  self.object.speakstring(text)

 def silence (self):
  self.object.Silence()

 def canSpeak(self):
  try:
   return win32gui.FindWindow("GWMExternalControl", "External Control") != 0 and super(WindowEyes, self).canSpeak()
  except:
   return False

