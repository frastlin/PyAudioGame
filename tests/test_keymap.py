from pyaudiogame.keymap import KeyMap

def test_add_function():
	keymap = KeyMap()
	keymap.add(key=["f"], mods=["shift"], event="fligh")
