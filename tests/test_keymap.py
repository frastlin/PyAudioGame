import unittest
from pyaudiogame.keymap import KeyMap

def funcCallback():
	return True

class TestKeymap(unittest.TestCase):
	def test_add_function(self):
		keymap = KeyMap()
		keymap.add(keys=["f"], mods=["shift"], event="fligh")
		keymap.add({
			"keys": "j",
			"event": "jump"
		})
		self.assertEqual(keymap.getEvent(keys=["f"], mods=["shift"]), "fligh")
		self.assertEqual(keymap.getEvent(keys="j"), "jump")
		self.assertEqual(keymap.getEvent("space"), None)

	def test_add_in_object(self):
		keymap = KeyMap([
			{'keys':['space'], 'event': "oranges"},
			{'keys':['f', 'a'], 'mods': ['ctrl','shift'], 'function': funcCallback},
		])
		self.assertEqual(keymap.getEvent(keys=['f', 'a'], mods=['ctrl','shift']), funcCallback())
		self.assertEqual(keymap.getEvent(keys='space'), 'oranges')

	def test_add_a_list(self):
		keymap = KeyMap()
		keymap.add([
			{'keys':'space', 'event': "oranges"},
			{'keys':['f', 'a'], 'mods': ['ctrl','shift'], 'function': funcCallback},
		])
		self.assertEqual(keymap.getEvent(keys=['f', 'a'], mods=['ctrl','shift']), funcCallback())
		self.assertEqual(keymap.getEvent(keys='space'), 'oranges')

	def test_state(self):
		keymap = KeyMap([
			{'keys':'space', 'mods':['shift'], 'state':0, 'event':'shiftSpace'},
			{'keys':'a', 'state':1, 'event':'apple'},
		])
		self.assertEqual(keymap.getEvent(keys='space', mods='shift', state=0), 'shiftSpace')
		self.assertEqual(keymap.getEvent('a', state=0), None)

	def test_nutral_mods(self):
		keymap = KeyMap([
			{'keys': 'f', 'mods': ['alt', 'ctrl', 'shift'], 'event':'modded'},
		])
		self.assertEqual(keymap.getEvent(keys="f", mods=['alt', 'ctrl', 'shift']), 'modded')
		self.assertEqual(keymap.getEvent(keys="f", mods=['leftalt', 'rightctrl', 'shift']), 'modded')
		self.assertEqual(keymap.getEvent(keys="f", mods=['leftmeta', 'rightctrl', 'leftshift']), 'modded')


if __name__ == '__main__':
	unittest.main