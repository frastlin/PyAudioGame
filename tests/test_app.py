import pyaudiogame
my_app = pyaudiogame.App(title="Test app")
k = pyaudiogame.key

#Is our check for the below code
r = False

def on_key_press(key, mods):
	"""Is the sample key handler/screen. It will change the global variable, then exit the screen"""
	global r
	if key == k.A:
		r = True
		my_app.exit()

def send_key(dt):
	"""Will send the key press"""
	my_app.dispatch_event('on_key_press', k.A, 0)

my_app.add_screen(on_key_press)

#Adding our event to my_app's event queue with a time because otherwise the screen won't be able to run.
my_app.event_queue.schedule_once(send_key, 0.1)

#running the app
my_app.run()

def test_r():
	"""Now we check if the key press really worked"""
	assert r == True

def test_screens():
	"""Makes sure that the custom screen handler has an item in it"""
	assert len(my_app.screens) == 1

#now adding many screens
screen1 = pyaudiogame.Screen()

def test_number_of_screens():
	"""Tests all the screen related functions"""
	my_app.add_screens(screen1, screen1, screen1)
	my_app.add_screen(screen1)
	assert len(my_app.screens[1]) == 4
	assert len(my_app.screens) == 2
	my_app.remove_screen()
	assert len(my_app.screens[1]) == 3
	my_app.remove_screens()
	assert len(my_app.screens) == 1

