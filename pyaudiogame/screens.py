#handles screens of events

class Screen(object):
	def __init__(self, *args, **kwargs):
		[setattr(self, func.__name__, func) for func in args]
		[setattr(self, k, kwargs[k]) for k in kwargs]

	def on_key_press(self, key, mods):
		pass

	def on_key_release(self, key, mods):
		pass
