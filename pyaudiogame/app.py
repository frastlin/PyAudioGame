#Has functions to do everything your engine module needs
import pygame, random, sys
from pygame.locals import *

from pyaudiogame.speech import speak as spk
from pyaudiogame.pygame_input import PygameInput
from pyaudiogame.console import Console
from pyaudiogame import global_keymap

#our program spacific modules:
import pyaudiogame.ticker as ticker

#This is a global event queue
event_queue = ticker.Scheduler(time_format=0.001)

class App(object):
	"""This is to subclass for an application."""

	def __init__(self, title="Test app", fps=30, window_type="pygame"):
		"""Title is the name of the window, fps is frames per second, how many iterations the loop runs in a given second. The default is 30"""
		self.title = title
		self.fps = fps
		self.window_type = window_type # pygame, console. are the options
		self.displaySurface = None # is set when self.create_surface is run. It is a pygame surface

		#Default variables that can be changed, but are not called
		#For the screen:
		#The two below numbers are in pixels, the current screen is a little box on the screen
		self.windowwidth = 640
		self.windowheight = 480
		#Full screen expands everything and fills the whole screen
		self.fullscreen = False
		#If the mouse should be visible or not
		self.mouse = False
		#Our event queue
		self.event_queue = event_queue
		# The input objects
		self.pygame_events = PygameInput(on_input=self._on_input)
		self.console_events = Console(on_input=self._on_input)

		#Our exicution variables
		self.running = True

		#This function runs to set default variables if people don't wish to mess with super
		self.set_defaults()

	def logic(self, actions):
		"""This is a function that is a placeholder. A dict of the event object is passed in and this is run in the on_input handler."""
		pass

	def in_main_loop(self):
		"""A function that is run every game loop that can be over ridden"""
		pass

	def set_defaults(self):
		"""Call this function to change the default variables"""
		pass

	def run(self):
		"""Call this when you are ready to start your game. It will run your main loop and create your screen"""
		#Call the screen
		self.create_surface(windowwidth=self.windowwidth, windowheight=self.windowheight, title=self.title, fullscreen=self.fullscreen, mouse=self.mouse)
		# add the event handlers specified in self
		self._add_handlers()
		#the clock for checking that we run 30 times a second:
		fpsClock = pygame.time.Clock().tick
		fps = self.fps
		# in_main_loop is a placeholder function that is run every loop
		in_main_loop = self.in_main_loop
		#tick is for events that are scheduled
		tick = event_queue.tick
		#create the game loop
		while True:
			self.pygame_events.run()
			if self.window_type == 'console':
				self.console_events.run()
			if not self.running:
				break
			in_main_loop()
			tick(fpsClock(fps))
		self.quit()

	def run_main_loop(self):
		"""This runs every loop of the game loop and makes sure pygame is running smoothely"""
		fpsClock = pygame.time.Clock().tick
		self.pygame_events.run()
		if self.window_type == 'console':
			self.console_events.run()
		if not self.running:
			return True
		in_main_loop()
		event_queue.tick(fpsClock(self.fps))

	def create_surface(self, windowwidth=640, windowheight=480, title="Test Surface", fullscreen=False, mouse=True):
		"""will make the main window"""
		pygame.init()
		if fullscreen:
				displaySurface = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
		else:
				displaySurface = pygame.display.set_mode((windowwidth, windowheight))
		pygame.display.set_caption(title)
		if self.window_type == "console":
			pygame.display.iconify() #makes the console go in front and the pygame window hide behind
			pygame.display.set_caption("Don't focus this window, Go back to the console!")
		if not mouse:
			pygame.mouse.set_visible(0)
		self.displaySurface  = displaySurface  
		return displaySurface

	def _on_input(self, input_event):
		"""Handles the logic function and exiting"""
		event = input_event.keymap_event
		if event == "quit" or self.logic(input_event.__dict__) == False:
			self.running = False

	def old__on_input(self):
		"""Will return a dict of all the keyboard and other input events of pygame's event system"""
		exit_key = self.exit_key
		#a dict with all the commands that go on
		actions = {
			'mousex': 0,
			'mousey': 0,
			'key': None,
			'mouseClicked': False,
			'mods': [],
			'state': None,
			'keyUp': None
			}
		for event in pygame.event.get():
			if event.type == MOUSEMOTION:
				actions['mousex'], actions['mousey'] = event.pos
			elif event.type == MOUSEBUTTONUP:
				actions['mousex'], actions['mousey'] = event.pos
				actions['mouseClicked'] = True
			elif event.type == KEYDOWN:
				actions['state'] = "down"
				actions['key'] = pygame.key.name(event.key)
				actions['mods'] = mod_id.get(pygame.key.get_mods(), [pygame.key.get_mods()])
			elif event.type == KEYUP:
				actions['state'] = "up"
				actions['keyUp'] = pygame.key.name(event.key)
				actions['mods'] = mod_id.get(pygame.key.get_mods(), [])
			if event.type == QUIT or (actions['key'] == "escape" and exit_key == 1) or ('alt' in actions['mods'] and actions['key'] == 'f4' and exit_key == 2):
				return False
		return actions

	def add_handler(self, handler_func, name=None, window=None):
		"""adds an event handler to the event handlers. Window can be either "console", "pygame", or None. If None, it will do both. The name is to specify the handler name, such as on_input if the name is different than the handler_func's name."""
		if not name:
			name = handler_func.__name__
		if window == "console":
			self.console_events.__dict__[name] = handler_func
		elif window == "pygame":
			self.pygame_events.__dict__[name] = handler_func
		else:
			self.pygame_events.__dict__[name] = handler_func
			self.console_events.__dict__[name] = handler_func

	def _add_handlers(self):
		"""Adds all the on_ functions in self to the two event handlers."""
		d = self.__dict__.items()
		for k, v in d:
			if k.startswith("on_"):
				self.add_handler(v, name=k)

	def key_repeat(self, on=True, delay=1000, delay_before_first_repeat=1):
		"""Call this function to either start what happens when a key is held down or to turn it off."""
		if on:
			pygame.key.set_repeat(delay_before_first_repeat, delay)
		else:
			pygame.key.set_repeat()

	def quit(self):
		"""Runs the functions needed to quit gracefully from pygame and python"""
		pygame.quit()
		sys.exit()

if __name__ == '__main__':
	f = App("Key Test", window_type="console")
	p = []
	def logic(actions):
		global p
		if(actions['key']):
#			spk(actions['key'])
			if not actions['key'] in p and actions['state']:
#				print(actions['key'])
				print('%s with mods %s' % (actions['key'], actions['mods']))
				p.append(actions['key'])
			elif not actions['state'] and actions['key'] in p:
				print("released: %s" % actions['key'])
				p.remove(actions['key'])
#		mods = actions['mods']
#		if mods:
#			spk(str(mods))

	f.logic = logic
	f.run()