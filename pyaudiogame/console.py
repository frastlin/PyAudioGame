"""Simple example showing how to get keyboard events.
print(event.ev_type, event.code, event.state)
"""
import sys

from inputs import get_key

mod_keys = [
'capslock',
'leftshift',
'rightshift',
'leftctrl',
'rightctrl',
'f15',
'rightmeta',
'leftmeta'
]

class Console(object):
	def __init__(self, run_func=lambda key, pressed, state: [key, pressed]):
		self.mod_keys = mod_keys
		self.pressed = set()
		self.mods = set()
		self.run_func = run_func

	def processCode(self, code):
		"""makes the key code the same as pygame's"""
		return code.split("_")[-1].lower()

	def run(self):
		events = get_key()
		for event in events:
			ev_type, code, state = [event.ev_type, event.code, event.state]
			code = self.processCode(code)
			self.run_func(code, self.pressed, state)
			if event.state == 1:
				if code in mod_keys:
					self.mods.add(code)
				self.pressed.add(code)
			elif code in self.pressed:
				self.pressed.remove(code)
				if code in self.mods:
					self.mods.remove(code)
 
if __name__ == "__main__":
	def main():
		"""Just print out some event infomation when keys are pressed."""
		def run_func(key, mods, state):
			if state and key == "space" and mods == set(["leftshift"]):
				print("Ran!")
		console = Console(run_func)
		while 1:
			console.run()

	main()