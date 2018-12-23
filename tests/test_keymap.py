import unittest
from pyaudiogame.keymap import KeyMap

def funcCallback():
	return True

class TestKeymap(unittest.TestCase):
	def test_add_function(self):
		keymap = KeyMap()
		keymap.add(key=["f"], mods=["shift"], event="fligh")
		keymap.add({
			"key": "j",
			"event": "jump"
		})
		self.assertEqual(keymap.getEvent(key=["f"], mods=["shift"]), "fligh")
		self.assertEqual(keymap.getEvent(key="j"), "jump")
		self.assertEqual(keymap.getEvent("space"), None)

	def test_add_in_object(self):
		keymap = KeyMap([
			{'key':['space'], 'event': "oranges"},
			{'key':['f', 'a'], 'mods': ['ctrl','shift'], 'function': funcCallback},
		])
		self.assertEqual(keymap.getEvent(key=['f', 'a'], mods=['ctrl','shift']), funcCallback())
		self.assertEqual(keymap.getEvent(key='space'), 'oranges')

	def test_add_a_list(self):
		keymap = KeyMap()
		keymap.add([
			{'key':'space', 'event': "oranges"},
			{'key':['f', 'a'], 'mods': ['ctrl','shift'], 'function': funcCallback},
		])
		self.assertEqual(keymap.getEvent(key=['f', 'a'], mods=['ctrl','shift']), funcCallback())
		self.assertEqual(keymap.getEvent(key='space'), 'oranges')

	def test_state(self):
		keymap = KeyMap([
			{'key':'space', 'mods':['shift'], 'state':0, 'event':'shiftSpace'},
			{'key':'a', 'state':1, 'event':'apple'},
		])
		self.assertEqual(keymap.getEvent(key='space', mods='shift', state=0), 'shiftSpace')
		self.assertEqual(keymap.getEvent('a', state=0), None)

	def test_nutral_mods(self):
		keymap = KeyMap([
			{'key': 'f', 'mods': ['alt', 'ctrl', 'shift'], 'event':'modded'},
		])
		self.assertEqual(keymap.getEvent(key="f", mods=['alt', 'ctrl', 'shift']), 'modded')
		self.assertEqual(keymap.getEvent(key="f", mods=['leftalt', 'rightctrl', 'shift']), 'modded')
		self.assertEqual(keymap.getEvent(key="f", mods=['leftmeta', 'rightctrl', 'leftshift']), 'modded')

	def test_quit_event(self):
		keymap = KeyMap([
			{'key': 'escape', 'event': 'quit'},
			{'key': 'f4', 'mods':['alt'], 'event': 'quit2'}
		])
		self.assertEqual(keymap.getEvent(key='escape'), 'quit')
		self.assertEqual(keymap.getEvent(key='F4', mods=['left alt']), 'quit2')



if __name__ == '__main__':
	unittest.main