import unittest
import pyglet
window = pyglet.window.Window(caption="Testing App")
key = pyglet.window.key
clock = pyglet.clock.get_default()

#Is our global variable to make sure the below code ran
ran = False

def on_key_press(symbol, mods):
	"""Is the sample key handler/screen. It will change the global variable, then exit the screen"""
	global ran
	if symbol == key.A:
		ran = True
		pyglet.app.exit()

def send_key(dt):
	"""Will send the key press"""
	window.dispatch_event('on_key_press', key.A, 0)

window.push_handlers(on_key_press)

#Adding our event to window's event queue with a time because otherwise the screen won't be able to run.
clock.schedule_once(send_key, 0.1)

#running the app
pyglet.app.run()

class TestApp(unittest.TestCase):
	def test_ran(self):
		"""Now we check if the key press really worked"""
		assert ran == True

if __name__ == '__main__':
	unittest.main()