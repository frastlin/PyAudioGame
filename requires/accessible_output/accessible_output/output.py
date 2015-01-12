import priority

class OutputError (Exception):
 pass

class AccessibleOutput (object):

 def __init__ (self, priority=priority.default, *args, **kwargs):
  self.priority = priority

 def output (self):
  #Override this in subclasses.
  pass

 def write (self, *args, **kwargs):
  self.output(*args, **kwargs)

