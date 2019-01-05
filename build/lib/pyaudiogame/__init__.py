from pyaudiogame.keymap import KeyMap

# The default keymap. If there is no quit mapping, then you will need to go to the command prompt and hit ctrl+c to exit the window.
# the key mapping object
global_keymap = KeyMap([
	{'key': 'f4', 'mods': ['alt'], 'event': 'quit'},
	{'key': 'escape', 'event':'quit'}
])

from pyaudiogame.app import App
from pyaudiogame.app import event_queue
from pyaudiogame.speech import speak
import pyaudiogame.storage