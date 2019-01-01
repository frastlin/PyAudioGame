from pyaudiogame import global_keymap

def _run_on_callbacks(self, name):
	def returned_func(event):
		try:
			self.__dict__['_' + name](event)
		except KeyError:
			pass
		object.__getattribute__(self, name)(event)
	return returned_func

class EventTemplate(object):
	def __init__(self, event=None, input_types=['key', 'mousebutton', 'mousemove']):
		self._input_types = input_types
		self.event = event
		self.type = ''
		self.state = -1
		self.key = ''
		self._button = ''
		self.mods = []
		self.focused = None
		self.input = False
		self.mouse_x = 0
		self.mouse_y = 0
		self.mous_rel = (0, 0)

	def set_type(self, type):
		type = str(type)
		self.type = type
		if type in self._input_types:
			self.input = True

	@property
	def keymap_event(self):
		return global_keymap.getEvent(self.key, self.mods, self.state)

	@property
	def button(self):
		return self._button

	@button.setter
	def button(self, button):
		"""makes button set self.key to 'button' + button. This is so keymap and event handlers don't need to catch anything but key to get mouse clicks."""
		self._button = button
		self.key = "mouse" + str(button)

class EventHandler(object):
	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			if k.startswith("on"):
				self.__dict__["_" + k] = v

# Normally the over-ridden functions when creating an EventHandler
	def convert_event(self, event):
		pass
	def run(self):
		pass
	def on_event(self, event):
		pass
	def on_input(self, event):
		pass

	def run_handlers(self, event):
		"""Requires the above EventTemplate object to be used"""
		self.on_event(event)
		if event.input:
			self.on_input(event)
		if event.type == 'quit':
			self.on_exit()
		elif event.type == 'userevent':
			self.on_user(event)
		elif event.type == 'videoexpose':
			self.on_expose(event)
		elif event.type == 'videoresize':
			self.on_resize(event)
		elif event.type == 'key' and event.state == 0:
			self.on_key_up(event)
		elif event.type == 'key' and event.state == 0:
			self.on_key_down(event)
		elif event.type == 'mousemotion':
			self.on_mouse_move(event)
		elif event.type == 'mousebutton' and event.state == 0:
			if event.button == 'left':
				self.on_lbutton_up(event)
			elif event.button == 'middle':
				self.on_mbutton_up(event)
			elif event.button == 'right':
				self.on_rbutton_up(event)
		elif event.type == 'mousebutton' and event.state == 1:
			if event.button == 'left':
				self.on_lbutton_down(event)
			elif event.button == 'middle':
				self.on_mbutton_down(event)
			elif event.button == 'right':
				self.on_rbutton_down(event)
		elif event.type == 'activeevent':
			if event.state == 'mouse':
				if event.focused:
					self.on_mouse_focus(event)
				else:
					self.on_mouse_blur(event)
			elif event.state == 'input':
				if event.focused:
					self.on_input_focus(event)
				else:
					self.on_input_blur(event)
			elif event.state == 'window':
				if event.focused:
					self.on_restore(event)
				else:
					self.on_minimize(event)

	def on_input_focus(self, event):
		pass
	def on_input_blur(self, event):
		pass
	def on_key_down(self, event):
		pass
	def on_key_up(self, event):
		pass
	def on_mouse_focus(self, event):
		pass
	def on_mouse_blur(self, event):
		pass
	def on_mouse_move(self, event):
		pass
	def on_mouse_wheel(self, event):
		pass
	def on_lbutton_up(self, event):
		pass
	def on_lbutton_down(self, event):
		pass
	def on_rbutton_up(self, event):
		pass
	def on_rbutton_down(self, event):
		pass
	def on_mbutton_up(self, event):
		pass
	def on_mbutton_down(self, event):
		pass
	def on_minimize(self, event):
		pass
	def on_restore(self, event):
		pass
	def on_resize(self, event):
		pass
	def on_expose(self, event):
		pass
	def on_exit(self, event):
		pass
	def on_user(self, event):
		pass
	def on_joy_axis(self,event):
		pass
	def on_joybutton_up(self,event):
		pass
	def on_joybutton_down(self,event):
		pass
	def on_joy_hat(self,event):
		pass
	def on_joy_ball(self,event):
		pass
	def on_event(self, event):
		pass

	def __getattribute__(self, name):
		"""This runs a check to see if there are any internal functions to call before the handler runs. This is so the engine can set its own internal attributes and still allow users to create their own handlers"""
		if name.startswith("on"):
			return _run_on_callbacks(self, name)
		return object.__getattribute__(self, name)
