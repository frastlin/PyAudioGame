from accessible_output.output import OutputError, AccessibleOutput

from accessible_output import priority

class SpeechOutput (AccessibleOutput):
 """Parent speech output class"""

 def __init__(self, *args, **kwargs):
  super(SpeechOutput, self).__init__(*args, **kwargs)

 def canSpeak (self):
  return True

 def output (self, *args, **kwargs):
  self.speak(*args, **kwargs)
 def silence (self):
  self.speak("", True)

class ScreenreaderSpeechOutput (SpeechOutput):
 def __init__ (self, *args, **kwargs):
  if 'priority' not in kwargs:
   kwargs['priority'] = priority.screenreader
  super(ScreenreaderSpeechOutput, self).__init__(*args, **kwargs)

