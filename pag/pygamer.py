#Has functions to do everything your engine module needs

import pygame, random, sys
from pygame.locals import *
from speech import speak as spk
#our program spacific modules:
import display, ticker

fps = 30
fpsClock = pygame.time.Clock()
surfaces = {}

def begin(windowwidth=640, windowheight=480, caption="Test Surface", fullscreen=False, mouse=True):
	"""will make the main window"""
	pygame.init()
	if fullscreen:
			displaySurface = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
	else:
			displaySurface = pygame.display.set_mode((windowwidth, windowheight))
	pygame.display.set_caption(caption)
	surfaces["main"] = displaySurface
	if not mouse:
		pygame.mouse.set_visible(0)

def keys(mouse=True, exit_keys=[{"key": "escape"}, {"mods": "alt", "key": "f4"}]):
	"""Will return a dict of all the keyboard and other input events of pygame's event system"""
	#a dict with all the commands that go on
	actions = {
		'mousex': 0,
		'mousey': 0,
		'key': None,
		'mouseClicked': False,
		'mods': []
		}

	for event in pygame.event.get():
		if event.type == MOUSEMOTION:
			actions['mousex'], actions['mousey'] = event.pos
		elif event.type == MOUSEBUTTONUP:
			actions['mousex'], actions['mousey'] = event.pos
			actions['mouseClicked'] = True
		elif event.type == KEYDOWN:
			actions['key'] = pygame.key.name(event.key)
			actions['mods'] = mod_id.get(pygame.key.get_mods(), [])
		if event.type == QUIT or ('alt' in actions['mods'] and actions['key'] == 'f4'):
			#The reason why we have sys.exit() here is because otherwise the display below throws an error because the video is not initalised
			pygame.quit()
			sys.exit()
	return actions

mod_id = {
64: ['ctrl'],
320: ['ctrl'],
1: ['shift'],
257: ['shift'],
65: ['ctrl', 'shift'],
256: ['alt'],
257: ['alt', 'shift'],
321: ['ctrl', 'alt', 'shift']
}

def tick(fps=30, graphics=True, displaySurface="main"):
	"""Will tick and run the actions on the action queue. This should be run every iteration of the game loop"""
	if graphics:
		rect_list = display.renderer(surfaces[displaySurface])
		#Redraw the screen and wait a clock tick
#		pygame.display.update()
		if rect_list:
			pygame.display.update(rect_list)
		display.event_queue.tick(fpsClock.tick(fps))

if __name__ == "__main__":
	import text
	begin(caption="My first test screen", fullscreen=True)

	r = pygame.draw.rect(surfaces["main"], (255, 255, 255), (200, 150, 200, 500), 0)
	display.draw(r, False)

	surface = "main"
	rect_list = []
	screen = None
	import menus

	while True:
		actions = keys()

		if actions["key"] == "return":
			screen = "menu"
		elif actions["key"] == "space":
			spk("drawing a rectangle")
			display.draw(pygame.draw.rect(surfaces["main"], (255, 100, 255), (200, 150, 200, 400), 0), False)

		if screen == "menu":
			s = menus.add_menu(actions, options=["fred", "sam", "claudia", "me", "you", "black", "orange", "cheese", "potatos", "tomatos", "birthdays", "oranges", "clickers", "mice", "us", "us again", "queens quackers", "twinkle twinkle"], title="Da menu")
			if s == "exit":
				screen = None

		tick(displaySurface=surface)