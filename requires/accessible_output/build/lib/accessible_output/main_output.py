from accessible_output import braille as b, speech as s

class Output(object):

 def __init__(self, braille=True, speech=True):
  self.braille = braille
  self.speech = speech
  self.braille_output = b.brailler.Brailler()
  self.speech_output = s.speaker.Speaker()

 def output(self, text, interrupt=True):
  if self.braille:
   self.braille_output.braille(text)
  if self.speech:
   self.speech_output.say(text, interrupt=interrupt)