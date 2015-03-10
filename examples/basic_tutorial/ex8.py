#dict out
import pyaudiogame
from pyaudiogame import storage
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

storage.screen = "start"
storage.text = ""
storage.wait_screen = None

def txt(msg):
	"""Will first make the msg a string, then make storage.text equal the msg as well as speak the msg"""
	msg = str(msg)
	spk(msg)
	storage.text = msg

def wait(new_screen):
	"""Will change the screen and set it so the screen will only change after the player has hit enter"""
	storage.screen = "wait"
	storage.wait_screen = new_screen
	t = "\nPress enter to continue"
	spk(t)
	storage.text += t

body_dict = {"1": "head", "2": "torso", "3": "hands", "4": "legs", "5": "feet", "6": "other random thing"}
color_dict = {"1": "red", "2": "green", "3": "orange", "4": "blue", "5": "yellow", "9": "Kind of a muddy brown and yellow together, although they make kind of a blueish green if you put them against a window"}
#Clothe_body_dict = {"head": head, "torso": torso, "hands": hands, "legs": legs, "feet": feet, "other random thing": thing}
current_clothes = {"head": "Nothing", "torso": "Nothing", "hands": "Nothing", "legs": "Nothing", "feet": "Nothing", "other random thing": "No random thing"}

def wearing():
	"""Will say what the player is wearing"""
	txt("You are currently wearing:\n%s on the head, %s on the torso, %s on the hands, %s on the legs, %s on the feet and %s" % (current_clothes["head"], current_clothes["torso"], current_clothes["hands"], current_clothes["legs"], current_clothes["feet"], current_clothes["other random thing"]))

def start(key):
	"""Will say the first text, then move on to the next screen"""
	txt("Welcome to all dect out! Today you are going to a party. This isn't just any party, it is a top-of-the line, rits to-the-hips party with all kinds of really really really rich people. You are dressing to impress!")
	wait("pre_choice")

def pre_choice(key):
	"""Will be what the player hears every time they come back to choice"""
	wearing()
	storage.screen = "choice"
	spk("Press the numbers to choose a bodypart")

def choice(key):
	"""Will change to the body part"""
	if key:
		c = body_dict.get(key, None)
		if c:
			spk(c)

def wait_screen(key):
	"""Will wait till a key press, then change the screen"""
	if key == "return":
		storage.screen = storage.wait_screen


scenes_dict = {"start": start, "pre_choice": pre_choice, "wait": wait_screen, "choice": choice}

def logic(actions):
	key = actions['key']
	screen = storage.screen
	if scenes_dict.get(screen, None):
		scenes_dict[screen](key)

	if key == "r":
		spk(storage.text)



MyApp.logic = logic
MyApp.run()
