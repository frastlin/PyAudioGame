#This is the description of the file. This is a template for an app.
import pyaudiogame
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

#put code here

def logic(actions):
	key = actions['key']

MyApp.logic = logic
MyApp.run()
