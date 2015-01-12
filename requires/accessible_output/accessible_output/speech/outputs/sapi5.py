import sapi5voice
from main import OutputError, SpeechOutput

import _winreg
import win32com.client

class Sapi5(SpeechOutput):
 """Provides speech output via Microsoft speech API version 5."""

 name = 'sapi5'

 def __init__(self, rate=None, volume=None, voice=None, *args, **kwargs):
  super(Sapi5, self).__init__(*args, **kwargs)
  try:
   self.object = win32com.client.Dispatch("SAPI.SPVoice")
  except:
   raise OutputError

  if rate:
   self.rate = rate
  if volume:
   self.volume = volume
  if voice:
   self.voice = voice

 def canSpeak(self):
  try:
   r = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "SAPI.SPVoice")
   r.Close()
   return True
  except:
   return False

 def speak(self, text, interrupt=0):
  if interrupt:
   self.silence()
  self.object.Speak(text, 1)

 def silence(self):
  self.object.Speak("", 3)
 def getRate (self):
  return self.object.Rate
 def setRate (self, rate):
  self.object.Rate = rate
 def getVolume (self):
  return self.object.Volume
 def setVolume (self, volume):
  self.object.Volume = volume
 def getVoice (self):
  v = self.object.Voice
  return v.GetDescription()
 def setVoice (self, voice):
  self.object.Voice = sapi5voice.available_voices()[voice]
 rate = property(fget=getRate, fset=setRate)
 volume = property(fget=getVolume, fset=setVolume)
 voice = property(fget=getVoice, fset=setVoice)
