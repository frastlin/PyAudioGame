from accessible_output.output import OutputError, AccessibleOutput

class BrailleOutput (AccessibleOutput):
 """Parent Braille output class"""

 def canBraille (self):
  return True

 def output (self, *args, **kwargs):
  self.braille(*args, **kwargs)

 def clear (self):
  self.braille("")
