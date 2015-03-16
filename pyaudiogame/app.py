import pyglet

#To keep people with Intel graphics drivers  from crashing
pyglet.options['shadow_window']=False

#The module wide variables.
event_queue = pyglet.clock.get_default()

class App(pyglet.window.Window):
	"""
The master app for pyaudiogame. Call this like:
my_app = pyaudiogame.App("My App")
You can then access screens and clock events through my_app.
This is a child of the pyglet.window class, so any events you can do on a window in pyglet.window you can do here.
The run method below is added and runs the pyglet main_loop.
"""

	def __init__(self, title=None, width=None, height=None, resizable=False, style=None, fullscreen=False, visible=True, vsync=True, display=None, screen=None, config=None, context=None):
		#give all the methods and attributes of window's __init__ function to this class
		super(App, self).__init__(width=width, height=height, caption=title, resizable=resizable, style=style, fullscreen=fullscreen, visible=visible, vsync=vsync, display=display, screen=screen, config=config, context=context)
		self.event_queue = event_queue
		self.screens = []

	def run(self):
		"""calls the pyglet.app run function"""
		pyglet.app.run()

	def exit(self):
		"""Will exit the current application"""
		pyglet.app.exit()

	def add_screens(self, *args):
		"""Will both append to the class screen list as well as appending the screen to the event stack"""
		[self.push_handlers(screen) for screen in args]
		self.screens.append(list(args))

	def add_screen(self, screen):
		try:
			self.screens[-1].append(screen)
		except:
			self.screens.append([screen])
		self.push_handlers(screen)

	def remove_screen(self, screen=None):
		if not self.screens:
			return None
		if not screen:
			screen = self.screens[-1][-1]
		for s in self.screens:
			if screen in s:
				s.remove(screen)
			if not s:
				self.screens.remove(s)
		self.remove_handlers(screen)
		return screen

	def remove_screens(self, *args):
		"""will remove either the whole chunk or a list of screens"""
		if not self.screens:
			return None
		if not args:
			args = self.screens.pop()
		else:
			[s.remove(a) for s in self.screens for a in args if a in s]
		[self.remove_handlers(a) for a in args]
		return args


if __name__ == '__main__':
	my_app = App("My App")

	@my_app.event
	def on_key_press(key, mods):
		if key == pyglet.window.key.SPACE:
			print("Hello world")


	my_app.run()
