#Has functions to do everything your engine module needs
import pygame, random, sys
from pygame.locals import *

from pyaudiogame.speech import speak as spk

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
		self.window_type = "window_type # pygame, console. are the options

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
		#A hard-coded exit key, 1 is escape, 2 is alt + f4 and 0 is nothing **WARNING** if there is no exit key you need to go to command prompt window and hit ctrl + c to exit the window!
		self.exit_key = 1

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
		#The game logic
		logic = self.logic
		#Returns events like key presses and mouse movement and we use it in our game logic
		keys = self.keys
		#create the game loop
		while True:
			actions = keys()
			if actions == False:
				break
			running = logic(actions)
			if running == False:
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

	def keys(self):
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

mod_id = {
64: ['left ctrl', 'ctrl'],
320: ['left ctrl', 'ctrl'],
1: ['left shift', 'shift'],
257: ['left shift', 'shift'],
256: ['left alt', 'alt'],
2: ['right shift', 'shift'],
128: ['right ctrl', 'ctrl'],
65: ['left ctrl', 'ctrl', 'left shift', 'shift'],
66: ['left ctrl', 'ctrl', 'right shift', 'shift'],
257: ['left alt', 'alt', 'left shift', 'shift'],
129: ['right ctrl', 'ctrl', 'left shift', 'shift'],
130: ['right ctrl', 'ctrl', 'right shift', 'shift'],
321: ['left ctrl', 'ctrl', 'left alt', 'alt', 'left shift', 'shift'],
322: ['left ctrl', 'ctrl', 'left alt', 'alt', 'right shift', 'shift'],
258: ['left alt', 'alt', 'right shift', 'shift'],
384: ['left alt', 'alt', 'right ctrl', 'ctrl'],
386: ['left alt', 'alt', 'right ctrl', 'ctrl', 'right shift', 'shift'],
}

if __name__ == '__main__':
	f = App("Key Test")
	def logic(actions):
		if(actions['key']):
#			spk(actions['key'])
			print(actions['key'])
		mods = actions['mods']
		if mods:
			spk(str(mods))

	f.logic = logic
	f.run()