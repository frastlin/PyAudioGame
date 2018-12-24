#Has functions to do everything your engine module needs
import pygame, random, sys
from pygame.locals import *

from pyaudiogame.speech import speak as spk
from pyaudiogame.keymap import KeyMap
from pyaudiogame.pygame_input import PygameInput
from pyaudiogame.console import Console

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
		# The default keymap. If there is no quit mapping, then you will need to go to the command prompt and hit ctrl+c to exit the window.
		# the key mapping object
		self.keymap = KeyMap([
			{'key': 'f4', 'mods': ['alt'], 'event': 'quit'},
			{'key': 'escape', 'event':'quit'}
		])
		# The input objects
		self.pygame_events = PygameInput(self.keys)
		self.console_events = Console(self.keys)
		self.events = self.console_events if self.window_type == 'console' else self.pygame_events

		#Our exicution variables
		self.running = True

		#This function runs to set default variables if people don't wish to mess with super
		self.set_defaults()

	def logic(self, actions):
		"""Overwrite this and put your game logic here. This is just a place-holder for now"""
		pass

	def set_defaults(self):
		"""Call this function to change the default variables"""
		pass

	def run(self):
		"""Call this when you are ready to start your game. It will run your main loop and create your screen"""
		#Call the screen
		self.create_surface(windowwidth=self.windowwidth, windowheight=self.windowheight, title=self.title, fullscreen=self.fullscreen, mouse=self.mouse)
		#the clock for checking that we run 30 times a second:
		fpsClock = pygame.time.Clock().tick
		fps = self.fps
		#tick is for events that are scheduled
		tick = event_queue.tick
		#create the game loop
		while True:
			self.events.run() # logic and everything runs in the key function
			if not self.running:
				break
			tick(fpsClock(fps))
		self.quit()

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
			return displaySurface

	def keys(self, input_event):
		event = self.keymap.getEvent(input_event.key, input_event.mods, input_event.state)
#		print(input_event.key, input_event.mods, input_event.state)
		if event == "quit" or self.logic(input_event.__dict__) == False:
			self.running = False

	def old_keys(self):
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