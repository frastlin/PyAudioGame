from .. import load_library
import platform

class OutputError(Exception):
 pass

class Output(object):
 name = "Unnamed Output"
 lib32 = None
 lib64 = None
 cdll = False
 priority = 100
 system_output = False

 def __init__(self):
  self.is_32bit = platform.architecture()[0] == "32bit"
  if self.lib32 and self.is_32bit:
   self.lib = load_library(self.lib32, cdll=self.cdll)
  elif self.lib64:
   self.lib = load_library(self.lib64, cdll=self.cdll)
  else:
   self.lib = None

 def output(self, text, **options):
  output = False
  if self.speak(text, **options):
   output = True
  if self.braille(text, **options):
   output = True
  if not output:
   raise RuntimeError("Output %r does not have any method defined to output" % self)

 def is_system_output(self):
  return self.system_output

 def speak(self, **optiont):
  return False

 def braille(self, **options):
  return False
