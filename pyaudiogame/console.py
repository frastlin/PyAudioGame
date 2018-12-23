"""Simple example showing how to get keyboard events.
print(event.ev_type, event.code, event.state)
"""
import sys
from threading import Thread

from inputs import get_key, get_mouse

from event_handler import EventHandler, EventTemplate

mod_keys = [
'capslock',
'left shift',
'right shift',
'left ctrl',
'right ctrl',
'f15', 
'right meta',
'left meta'
]

event_names = {
	'esc': 'escape',
	'enter': 'return',
	'f15': 'help',
	'102nd': '\\',
	'minus': '-',
	'apostrophe': "`",
	'equal': '=',
	'backslash': "'",
	'semicolon': ';',
	'rightbrace': ']',
	'leftbrace': '[',
}

duplicated_keys = [
	'backspace',
	'delete',
	'up',
	'down',
	'right',
	'left',
	'page up',
	'page down',
	'home',
	'end',
]

mouse_types = {
	'Absolute': 'mousemotion',
	'Key': 'mousebutton',
}

class Console(EventHandler):
	def __init__(self, run_func=lambda event: event):
		self.mod_keys = mod_keys
		self.pressed = set()
		self.mods = set()
		self.run_func = run_func
		self.activated_already = set()
		self.last_mouse_coords = (0, 0)
		self.event_queue = []
		# these below lists lines are queues for each type of event type because the get_event functions are blocking.
		self.mouse_events = []
		self.keyboard_events = []

	def start(self):
		Thread(target=self.run_key, daemon=True).start()
#		Thread(target=self.run_mouse, daemon=True).start()

	def run(self):
		self.clear_queue()
		if self.mouse_events:
			self.event_queue += self.mouse_events
			self.mouse_events = []
			Thread(target=self.run_mouse, daemon=True).start()
		if self.keyboard_events:
			self.event_queue += self.keyboard_events
			self.keyboard_events = []
			Thread(target=self.run_key, daemon=True).start()
		[self.run_func(e) for e in self.event_queue if e.input]

	def clear_queue(self):
		self.event_queue = []

	def processCode(self, code):
		"""makes the key code the same as pygame's"""
		code = code.split("_")[-1].lower()
		mod_code = code.replace('left', '').replace('right', '')
		if 'page' in code:
			code = 'page ' + code[4:]
		if mod_code in ['ctrl', 'shift', 'meta']:
			code = code.replace('left', 'left ').replace('right', 'right ')
		code = event_names.get(code, code)
		return code

	def run_mouse(self):
		print("ran")
		events = get_mouse()
		coords = [0,0]
		mousemotion_event = None
		for event in events:
			event_type, code, state = event.ev_type, event.code.lower(), event.state
			event_obj = EventTemplate(event)
			event.mods = self.pressed
			if '_x' in code:
				coords[0] = state
				mousemotion_event = event
				continue
			elif '_y' in code:
				coords[1] = state
				continue
			elif 'btn_' in code:
				event_obj.set_type('mousebutton')
				event_obj.button = code[4:]
				event_obj.state = state
				if event.state == 1:
					self.pressed.add(event)
				elif event in self.pressed:
					self.pressed.remove(event)
			else:
				event_obj.set_type(event_type)
				event_obj.state = state
			self.mouse_events.append(event_obj)
		if coords[0] or coords[1]:
			event_obj = EventTemplate(mousemotion_event)
			event_obj.set_type('mousemotion')
			event.mods = self.pressed
			event_obj.mouse_x, event_obj.mouse_y = coords
			event_obj.mouse_rel = (self.last_mouse_coords[0] - coords[0], self.last_mouse_coords[1] - coords[1])
			self.last_mouse_coords = coords
			self.mouse_events.append(event_obj)

	def run_key(self):
		events = get_key()
		for event in events:
			event = self.convert_key_event(event)
			if not event: # this is to make sure the duplicated events don't run
				continue
			self.keyboard_events.append(event)
			if event.state == 1 and event.input:
				self.pressed.add(event)
			elif event in self.pressed:
				self.pressed.remove(event)

	def convert_key_event(self, event): 
		ev_type, code, state = [event.ev_type, event.code, event.state]
		code = self.processCode(code)
		# make sure no duplicate keys are pressed
		if code in duplicated_keys and (code, state) in self.activated_already:
			self.activated_already.remove((code, state))
			return False
		else:
			self.activated_already.add((code, state))
		event_obj = EventTemplate()
		event_obj.event = event
		event_obj.set_type(ev_type.lower())
		event_obj.state = state
		event_obj.mods = self.pressed
		if event_obj.type == 'key':
			event_obj.key = code
		return event_obj

if __name__ == "__main__":
	def main():
		"""Just print out some event infomation when keys are pressed."""
		def run_func(event):
			if event.type == 'key':
				print(event.key)

		console = Console(run_func)
		console.start()
		while 1:
			console.run()

	main()