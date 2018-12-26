import pygame
from pygame.locals import *
from pyaudiogame.event_handler import EventHandler, EventTemplate

mod_id = {
64: ['left ctrl'],
320: ['left ctrl'],
1: ['left shift'],
512: ['right alt'],
578: ['left ctrl', 'right shift', 'right alt'],
513: ['right alt', 'left shift'],
514: ['right alt', 'right shift'],
257: ['left shift'],
256: ['left alt'],
2: ['right shift'],
128: ['right ctrl'],
65: ['left ctrl', 'left shift'],
66: ['left ctrl', 'right shift'],
257: ['left alt', 'left shift'],
129: ['right ctrl', 'left shift'],
130: ['right ctrl', 'right shift'],
321: ['left ctrl', 'left alt', 'left shift'],
322: ['left ctrl', 'left alt', 'right shift'],
258: ['left alt', 'right shift'],
384: ['left alt', 'right ctrl'],
386: ['left alt', 'right ctrl', 'right shift'],
}

event_types = {
	KEYDOWN: 'key',
	KEYUP: 'key',
	MOUSEBUTTONDOWN: 'mousebutton',
	MOUSEBUTTONUP: 'mousebutton',
	ACTIVEEVENT: 'activeevent',
	USEREVENT: 'userevent',
	VIDEOEXPOSE: 'videoexpose',
	VIDEORESIZE: 'videoresize',
	MOUSEMOTION: 'mousemotion',
}

activeevent_states = {
	1: 'mouse',
	2: 'input',
	4: 'window'
}

class PygameInput(EventHandler):
	def __init__(self, **kwargs):
		EventHandler.__init__(self, **kwargs)

	def run(self):
		for event in pygame.event.get():
			event = self.convert_event(event)
			self.run_handlers(event)

	def convert_event(self, event):
		event_dict = event.__dict__
		event_obj = EventTemplate()
		event_obj.event = event
		event_obj.set_type(event_types.get(event.type, event.type))
		mods = mod_id.get(pygame.key.get_mods(), [pygame.key.get_mods()])
		if mods != [0]:
			event_obj.mods = mods
		if event.type in [KEYDOWN, MOUSEBUTTONDOWN]:
			event_obj.state = 1
		elif event.type in [KEYUP, MOUSEBUTTONUP]:
			event_obj.state = 0
		if event_dict.get('key'):
			event_obj.key = pygame.key.name(event.key).lower()
		elif event_obj.type == 'mousebutton':
			if event.button == 0:
				event_obj.button = 'left'
			elif event.button == 1:
				event_obj.button = 'middle'
			elif event.button == 2:
				event_obj.button = 'right'
			elif event.button == 4:
				event_obj.button = 'rollup'
			elif event.button == 5:
				event_obj.button = 'rolldown'
		elif event_obj.type == 'activeevent':
			event_obj.state = activeevent_states.get(event.state, event.state)
		elif event_obj.type == 'mousemotion':
			event_obj.mouse_x, event_obj.mouse_y = pygame.mouse.get_pos()
			event_obj.mouse_rel = pygame.mouse.get_rel()
		if event_dict.get('gain') != None:
			event_obj.focused = event.gain
		return event_obj
