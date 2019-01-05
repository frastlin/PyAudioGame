"""Simple example showing how to get keyboard events.
Note that the mouse events don't work very well. Something is wrong with the pipe process that keeps the mouse event process from exiting in the inputs script. The bug has been reported, and as soon as it is fixed, uncommenting the run_mouse() function will work.
print(event.ev_type, event.code, event.state)
"""
import sys

from .inputs import get_key, get_mouse

from pyaudiogame.event_handler import EventHandler, EventTemplate

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
	def __init__(self, **kwargs):
		EventHandler.__init__(self, **kwargs)
		self.mod_keys = mod_keys
		self.pressed = set()
		self.activated_already = set()
		self.last_mouse_coords = (0, 0)
		self.event_queue = []
		# these below lists lines are queues for each type of event type because the get_event functions are blocking.
		self.mouse_events = []
		self.keyboard_events = []

	def run(self):
		self.event_queue = []
		self.run_key(self.event_queue)
#		self.run_mouse(self.event_queue)
		[self.run_handlers(e) for e in self.event_queue if e.input]

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

	def run_mouse(self, queue):
		events = get_mouse(False)
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
			queue.append(event_obj)
		if coords[0] or coords[1]:
			event_obj = EventTemplate(mousemotion_event)
			event_obj.set_type('mousemotion')
			event.mods = self.pressed
			event_obj.mouse_x, event_obj.mouse_y = coords
			event_obj.mouse_rel = (self.last_mouse_coords[0] - coords[0], self.last_mouse_coords[1] - coords[1])
			self.last_mouse_coords = coords
			queue.append(event_obj)

	def run_key(self, queue):
		events = get_key(False)
		for event in events:
			event = self.convert_key_event(event)
			if not event: # this is to make sure the duplicated events don't run
				continue
			queue.append(event)
			if event.state == 1 and event.input and not event.key in [e.key for e in self.pressed]:
				self.pressed.add(event)

	def convert_key_event(self, event): 
		ev_type, code, state = [event.ev_type, event.code, event.state]
		code = self.processCode(code)
		# make sure no duplicate keys are pressed
		if code in duplicated_keys and (code, state) in self.activated_already:
			self.activated_already.remove((code, state))
			return False
		else:
			self.activated_already.add((code, state))
		in_mods = [e for e in self.pressed if code == e.key]
		if not state and in_mods:
			self.pressed.remove(in_mods[0])
		event_obj = EventTemplate()
		event_obj.event = event
		event_obj.set_type(ev_type.lower())
		event_obj.state = state
		event_obj.mods = list(self.pressed)
		if event_obj.type == 'key':
			event_obj.key = code
		return event_obj

if __name__ == "__main__":
	def main():
		"""Just print out some event infomation when keys are pressed."""
		def run_func(event):
			if event.type == 'key':
				print(event.key)
				print("mods are: %s" % event.mods)

			elif event.type == "mousebutton" and event.state:
				print("clicked!")

		console = Console(run_func)
		while 1:
			console.run()

	main()