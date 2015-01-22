#fraught with possibility
import pyaudiogame
import random
import ex5_1
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

def logic(actions):
	key = actions['key']
	if key == "space":
		ex5_1.func()
	elif key == "return":
		spk("Your random number is: %s!" % random.randint(1,10))

MyApp.logic = logic
MyApp.run()