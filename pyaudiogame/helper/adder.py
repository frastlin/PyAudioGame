#This is a module of functions that will add or check if something is added to a list. Mostly to check if a ui instance is already loaded.
from pyaudiogame import storage
from pyaudiogame import ui
storage.temp_dict = {}
temp_dict = storage.temp_dict

def add_menu(actions, options=['Yes', 'No'], dict=temp_dict, name=None, result_list=[], default_position=0, keys={"navigation_back": "up", "navigation_forward": "down", "exit": ["escape", "backspace"], "except": "return"}, shortkeys=None, title="Test Menu", loops=True, persistent=0, sounds={}):
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

def add_typer(actions, title="", default_text="", dict=temp_dict, name=None, character_sets=[]):
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
