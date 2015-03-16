"""
A basic wrapper around the pyglet.window.key module.
To see a list of all the keycodes see:
http://www.pyglet.org/doc/api/pyglet.window.key-module.html
Use the text function in this module to get a string. use it like:
if pyaudiogame.key.text(key) == "space":
	spk("Hello world")

Here is a brief list of key codes:
Everything is always capital:
key.A
key.SPACE
key.LEFT
key._1
and for the numpad:
key.NUM_1
for mod keys:
key.MOD_SHIFT
"""
from pyglet.window.key import *

def key_text(key_number):
	"""Pass in the number of the key and text will be returned. This does not work on mod keys as there is some conflict with typing text"""
	return symbol_string(key_number).lower()

def mod_text(mod_number):
	"""Pass in the number of the mod key and a list of string/s will be returned. This does not work on keys as there is a conflict with the mods and text. The mods are the key name without mod_ before it, so like: ctrl, shift, alt, capslock, windows..."""
	mod_list = modifiers_string(mod_number).split("|")
	return [m.lower().split("_")[1] for m in mod_list]
