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
			{'keys':'space', 'event': "oranges"},
			{'keys':['f', 'a'], 'mods': ['ctrl','shift'], 'function': funcCallback},
		])
		self.assertEqual(keymap.getEvent(keys=['f', 'a'], mods=['ctrl','shift']), funcCallback())
		self.assertEqual(keymap.getEvent(keys='space'), 'oranges')


if __name__ == '__main__':
	unittest.main