#This is a module that creates menus.
#you call the menus.Menu with all the settings, then you cicle using the Menu.run(key, mod) call.
import display
"""
my notes:
if using a numbered list look at:
for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v

"""
import text
from speech import speak as spk

class Menu(object):
	"""Used for creating a menu in your program"""

	def __init__(self, options=["yes", "no"], default_position=0, keys=["up", "down", ["escape", "backspace"], "return"], mouse=False, shortkeys=None, title="Test Menu", loops=True, persistent=0, font={}, highlight=False, sounds={}, top_left_corner=(350, 100), center=True, remain=False):
		"""This creates a menu with the following values:
			options: are what the user sees displayed. If you pass a list, all items will have the settings of font. if you pass a dict, the keys will be the options and the values will be font settings for each line, like the font argument.
			default_position: the first selected option
			keys: when using the keyboard, move up through the options, down through the options, exits the menu, selects an option. you can make a list of items for each one.
			mouse: the ability to select options with the mouse
			shortkeys: Create a list of key names that is as long as the options list and pass it. For example ['1', '2', '3'] will activate options 0, 1 and 2 in the options list.
			title: The text that shows above the menu. pass as None if you don't wish any.
			loops: when using the keyboard, says if you will reach the bottom of the screen and do nothing or if you will loop back to the start. also vice-versa
			persistent: will remember your position. has 4 options, 0 doesn't remember anything, 1 remembers only on exit, 2 only remembers on selection, 3 remembers on both
			highlight: When using the mouse, will change the highlighted text when you move your mouse over it and will do the same for when you arrow over it
			font: is a dict, you can specify the settings for "default_font" or "highlighted_font" in a dict key and their value is another dict with the following: 'size', 'spacing' any extra spacing between menus above the default, 'font_color': color of the font, 'font_background': color of the small rectangle behind the text, 'font': any font file in the dir of your game file
			sounds: are sounds for different actions. the excepted values are: "change": for when the selection changes, "select": for when the selection is clicked on, "exit": when the menu is closed, "hit": when
				using the keyboard, will make a sound when hitting the top or bottom and loop is not on, "pass": for when loop is on and using the keyboard, will make this sound when switching between the
				top and bottom of the menu. It is best to use mp3 or ogg and needs pygame to run.
			top_left_corner:The location where the top left of the text rectangle will be.
			center:Means that text will be centered alined with the location. Otherwise it will be left-alined.
			remain:Means that it will remain till a clear of the screen is called.

			Note, if you just run this menu with the defaults, it will be a yes and no menu. All you need to run it is:
			menu1 = menus.Menu(title="Who would you like to date?", options=["fred", "frank", "Julia", "sally"])
		"""

		self.options = options
		self.default_position = default_position
		self.keys = keys
		self.mouse = mouse
		self.shortkeys = shortkeys
		self.title = title
		self.loops = loops
		self.persistent = persistent
		self.highlight = highlight
		self.font = font
		self.sounds = sounds
		self.top_left_corner = top_left_corner
		self.center = center
		self.remain = remain

		#These are class spacific variables
		self.current_position = default_position
		self.say_title = True
		self.message = None
		self.options_display = []
		self.single_settings = False
		self.options_rect = []

		if isinstance(self.options, dict):
			self.options = [f for f in self.options]
			self.single_settings = options

	def run(self, key=None, mods=None, mouse_position=(0, 0), mouse_clicked=False):
		"""Is the function you call every time you run the menu.
			key: are the keyboard events
			mods: are keys like, shift, ctrl, right_shift, left_shift, right_ctrl, left_ctrl.
			mouse_position: where the mouse is
			mouse_clicked: is if the mouse has clicked or not
		"""

		self.message = None
		key = str(key)
		result = None
		if not self.options_display:
			self.first_run()
		if key in (self.keys[0], self.keys[1]):
			self.key_checker(key)
		elif mouse_position[0] and not mouse_clicked:
			self.mouse_checker(mouse_position)
		elif key in (self.keys[2]):
			result = self.exit_menu()
		elif key in (self.keys[3]) or (mouse_clicked and self.mouse_checker(mouse_position, True)):
			result = self.chose_item()

		if self.message:
			spk(self.message)
			self.txt()
		return result

	def first_run(self):
		if self.say_title and self.title:
			spk(self.title)
			self.message = self.options[self.current_position]
			self.say_title = False
		self.options_display = self.set_options_display()
		self.options_rect = self.txt()

	def key_checker(self, key):
		"""checks what key it is and does stuff accordingly"""
		if key == self.keys[0]:
			self.change_position("add")
		elif key == self.keys[1]:
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

	def txt(self):
		"""Will display the text and show what option is highlighted"""
		highlighted = self.current_position
		od = self.options_display
		[i[1].refresh() for i in od]
		od[highlighted][1].select()
		od = [[i[0], i[1].current_font] for i in od]
		return text.complex_multilign(text_settings=od, xpos=self.top_left_corner[0], ypos=self.top_left_corner[1], persistent=self.remain, center=self.center, clear=True)

	def set_options_display(self):
		"""Creates our tuple list of settings"""
		if self.single_settings:
			l = [[i, Fonter(self.single_settings[i])] for i in self.single_settings]
		else:
			l = [[i, Fonter(self.font)] for i in self.options]
		for t in l:
			t[0] = "    %s    " % t[0]
		return l

	def mouse_checker(self, mouse_position, mouser=False):
		"""Checks if the mouse is in a box and if so, checks what option it is over. if mouser is False, it will only say the position if it has changed from the last one."""
		check_list = [i.collidepoint(mouse_position) for i in self.options_rect]
		if not mouser and 1 in check_list and self.current_position != check_list.index(1):
			self.current_position = check_list.index(1)
			self.message = self.options[self.current_position]
		elif mouser and 1 in check_list:
			return True

class Fonter:
	"""Placing the font settings in a class(and putting each setting to be assigned in a function) removes the need for copy. It is 45 seconds with deep copy on 1000000 and 2.5 seconds for assigning a class to 1000000. having a built-in function rather than doing refresh or select is 0.1 seconds slower for 1m."""
	def __init__(self, settings={}):
		self.current_font = {'size': 46, 'spacing': 0, 'font_color': 'white', 'font_background': 'black', 'font': 'freesansbold.ttf'} # 'ypos': 50, 'xpos': 350}
		self.default_font = {'size': 46, 'font_color': 'white', 'spacing': 0, 'font_background': 'black', 'font': 'freesansbold.ttf'}
		self.highlighted_font = {'size': 46, 'font_color': 'black', 'spacing': 0, 'font_background': 'white', 'font': 'freesansbold.ttf'}
		self.update_font(settings)

	def update_font(self, settings):
		"""Will go through the settings and update the classes fonts if needed"""
		if not settings:
			return 0
		elif settings.get('default_font'):
			self.default_font.update(settings['default_font'])
		elif settings.get('highlighted_font'):
			self.highlighted_font.update(settings['highlighted_font'])
		self.current_font.update(self.default_font)

	def refresh(self):
		"""Will switch current_font back to default_font"""
		self.current_font.update(self.default_font)

	def select(self):
		"""Will switch current_font to highlighted_font"""
		self.current_font.update(self.highlighted_font)

def add_menu(actions, options=['Yes', 'No'], dict={}, name=None, result_list=[], default_position=0, keys=["up", "down", ["escape", "backspace"], "return"], mouse=False, shortkeys=None, title="Test Menu", loops=True, persistent=0, font={}, highlight=False, sounds={}, top_left_corner=(350, 100), center=True, remain=False):
	"""Call this function with a dict of actions and the name of a dict to append either the name or title to."""
	if not name:name = title
	if not dict.get(name):
		dict[name] = Menu(options, default_position, keys, mouse, shortkeys, title, loops, persistent, font, highlight, sounds, top_left_corner, center, remain)
	else:
		s = dict[name].run(key=actions.get('key'), mods=actions.get('mods', []), mouse_position=(actions.get('mousex', 0), actions.get('mousey', 0)), mouse_clicked=actions.get('mouseClicked'))
		if result_list and s:
			if s == "exit":
				result_list.pop()
			else:
				result_list.append(s)
		return s
