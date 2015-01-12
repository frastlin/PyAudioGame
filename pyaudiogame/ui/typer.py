## coding: latin-1
#This module is used to display and handle typing of text.
from pyaudiogame.speech import speak as spk

class Typer(object):

	#This is a dict that has default character sets"""
	character_sets = {
		'numbers': ['1','2','3','4','5','6','7','8','9','0'],
		'letters_simple': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
		'capitals': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','S','Y','Z'],
		'letters_special': False,
		'punctuation_simple': ['.',',','_','\"','\''],
		'punctuation_medium': ['\\','/','[',']','`','=','-'],
		'punctuation_complex': False
	}

	#This is a dict with all the modification keys
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

	#This is a dict with all the shifted keys in it.
	shifters = {'space':'space', '-':'_', '\'':'\"', '=':'+', ';':':', '[':'{', ']':'}', '.':'>', ',':'<', '/':'?', '\\':'|', '`':'~',

	'1':'!', '2':'@', '3':'#', '4':'$', '5':'\%', '6':'^', '7':'&', '8':'*', '9':'(', '0':')'
	}

	def __init__(self, title="", valid_characters=['letters_simple', 'capitals', 'numbers', 'punctuation_simple'], multiline=False, length=0, current_string=""):
		#This creates a list of all the valid chars we can have typed. if it is in the set list, that set list is appended, otherwise, the string directaly is appended.
		self.title = title
		self.valid_characters = self.valid_list_maker(valid_characters)
		self.multiline = multiline
		#The next line will update character_sets with our boolian values for the complex stuff.
		[self.character_sets.update({i: True}) for i in valid_characters if isinstance(self.character_sets.get(i), bool)]
		self.length = length
		self.current_string = current_string

		#These are our operation variables:
		self.ran = False

	def run(self, actions):
		"""Run this to catch input and to return a string."""
		key = actions['key']
		if "shift" in actions['mods']:
			key = self.shifter(key)
		text = None
		if not self.ran:
			text = self.first_run()

		if key in self.valid_characters:
			self.current_string += key
			text = key
		elif key == "space":
			self.current_string += " "
			text = "space"
		elif key == "backspace" and self.current_string:
			text = self.current_string[-1]
			self.current_string = self.current_string[:-1]
		elif key in ['up', 'down']:
			text = self.title + ' ' + self.current_string
		elif key == 'return' and not self.multiline:
			self.ran = False
			return self.current_string


		if text:
			if text in self.character_sets['capitals']:
				text = "capital %s" % text
			spk(text)
		return None


	def first_run(self):
		"""Is the creation of the first string of text"""
		self.ran = True
		return self.title + self.current_string

	def valid_list_maker(self, options):
		"""Will check if the option is in the character_sets and if so will add that set to the list. if not, it will just add the option to the returned list."""
		char_list = []
		for o in options:
			check = self.character_sets.get(o)
			if isinstance(check, (list, tuple, set)):
				char_list += check
			else:
				char_list += o
		return char_list

	def shifter(self, key):
		"""Changes characters from their unshifted state to their shifted state"""
		k = self.shifters.get(key)
		if not k:
			k = key.upper()
		return k

def add_typer(actions, title="", default_text="", dict={}, name=None, character_sets=[]):
	"""You pass the name of the thing you wish to have text for and it is either added to the dict or ran"""
	if not name:
		name = title
	if dict.get(name):
		t = dict[name].run(actions)
	else:
		if character_sets:
			dict.update({name: Typer(title=title, current_string=default_text, valid_characters=character_sets)})
		else:
			dict.update({name: Typer(title=title, current_string=default_text)})
		t = None
	return t
