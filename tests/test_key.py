#Tests the functionality in pyaudiogame.key
from pyaudiogame import key as k

def test_constant():
	assert k.A == 97

def test_text_functions():
	assert k.key_text(k.A) == "a"
	assert k.key_text(301) == "301"
	assert k.mod_text(k.MOD_SHIFT) == ["shift"]
	assert k.mod_text(100) == ["alt", "command"]

