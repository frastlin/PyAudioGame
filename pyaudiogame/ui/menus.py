#This is a module that creates menus.
#you call the menus.Menu with all the settings, then you cicle using the Menu.run(key, mod) call.
"""
my notes:
if using a numbered list look at:
for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v

"""
from pyaudiogame.speech import speak as spk

class Menu(object):
	"""Used for creating a menu in your program"""

	def __init__(self, options=["yes", "no"], default_position=0, keys={"back": "up", "forward": "down", "exit": ["escape", "backspace"], "except": "return"}, shortkeys=None, title="Test Menu", loops=True, persistent=0, sounds={}):
		"""This creates a menu with the following values:
			options: are what the user sees displayed. If you pass a list, all items will have the settings of font. if you pass a dict, the keys will be the options and the values will be font settings for each line, like the font argument.
			default_position: the first selected option
			keys: pass a string or a list of strings for each entry. back is if you were going up in the menu, forward is down in the menu, exit is to leave, except is to choose an option.
			shortkeys: Create a list of key names that is as long as the options list and pass it. For example ['1', '2', '3'] will activate options 0, 1 and 2 in the options list.
			title: The text that is said before the menu. pass as None if you don't wish any.
			loops: when using the keyboard, says if you will reach the bottom of the screen and do nothing or if you will loop back to the start. also vice-versa
			persistent: will remember your position. has 4 options, 0 doesn't remember anything, 1 remembers only on exit, 2 only remembers on selection, 3 remembers on both
			sounds: are sounds for different actions. the excepted values are: "change": for when the selection changes, "select": for when the selection is clicked on, "exit": when the menu is closed, "hit": when
				using the keyboard, will make a sound when hitting the top or bottom and loop is not on, "pass": for when loop is on and using the keyboard, will make this sound when switching between the
				top and bottom of the menu. It is best to use mp3 or ogg and needs pygame to run.

			Note, if you just run this menu with the defaults, it will be a yes and no menu. All you need to run it is:
			menu1 = menus.Menu(title="Who would you like to date?", options=["fred", "frank", "Julia", "sally"])
		"""

		self.options = options
		self.default_position = default_position
		self.keys = keys
		self.shortkeys = shortkeys
		self.title = title
		self.loops = loops
		self.persistent = persistent
		self.sounds = sounds

		#These are class spacific variables
		self.current_position = default_position
		self.say_title = True
		self.message = None
		self.ran = False

		#default checks
		default_key_dict = {"back": "up", "forward": "down", "exit": ["escape", "backspace"], "except": "return"}
		[i.update({i: default_key_dict[i]}) for i in default_key_dict if not self.keys.get(i)]

	def run(self, actions):
		"""Is the function you call every time you run the menu. Just pass in a dict of actions"""
		actions['key'] = str(actions['key'])
		self.message = None
		key = actions['key']
		keys = self.keys
		result = None
		if not self.ran:
			self.first_run()

		if key in keys["back"] or key in keys['forward']:
			self.key_checker(key)
		elif key in keys['exit']:
			result = self.exit_menu()
		elif key in keys['except']:
			result = self.chose_item()

		if self.message:
			spk(self.message)
		return result

	def first_run(self):
		if self.say_title and self.title:
			spk(self.title)
			self.message = self.options[self.current_position]
			self.say_title = False
			self.ran = False

	def key_checker(self, key):
		"""checks what key it is and does stuff accordingly"""
		if key == self.keys['back']:
			self.change_position("add")
		elif key == self.keys['forward']:
			self.change_position('minus')
		self.message = self.options[self.current_position]

	def exit_menu(self):
		"""Resets the menu for the next call"""
		self.say_title = True
		self.options_display = []
		if self.persistent in [0, 2]:
			self.current_position = self.default_position
		return "exit"

	def chose_item(self):
		"""resets the menu and returns the current option"""
		self.say_title = True
		self.options_display = []
		position = self.current_position
		if self.persistent in [0, 1]:
			self.current_position = self.default_position
		return self.options[position]

	def change_position(self, direction):
		p = self.current_position
		o = len(self.options) - 1
		if direction == "minus":
			p += 1
		elif direction == "add":
			p -= 1
		if p > o:
			if self.loops:
				p = 0
			else:
				p -= 1
		elif p < 0:
			if self.loops:
				p = o
			else:
				p += 1
		self.current_position = p

def add_menu(actions, options=['Yes', 'No'], dict={}, name=None, result_list=[], default_position=0, keys={"back": "up", "forward": "down", "exit": ["escape", "backspace"], "except": "return"}, shortkeys=None, title="Test Menu", loops=True, persistent=0, sounds={}):
	"""Call this function with a dict of actions and the name of a dict to append either the name or title to."""
	if not name:name = title
	if not dict.get(name):
		dict[name] = Menu(options, default_position, keys, shortkeys, title, loops, persistent, sounds)
	else:
		s = dict[name].run(actions)
		if result_list and s:
			if s == "exit":
				result_list.pop()
			else:
				result_list.append(s)
		return s
