#if elif else
import pyaudiogame
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

#Lets check if they pressed the right keys
def check_keys(key):
	if key == "1":
		spk("Great, you are correct!")
	elif key == "return" or key == "space":
		spk("This is also correct!")
	elif key == "f2":
		spk("And you found the hidden key that's correct!")
	else:
		spk("Nope, try again, I'm sorry")

def logic(actions):
	key = actions['key']
	#Lets see if there was really a key press
	if key:
		check_keys(key)

MyApp.logic = logic
MyApp.run()