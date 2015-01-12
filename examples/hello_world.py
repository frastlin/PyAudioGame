import pyaudiogame
spk = pyaudiogame.speech.speak

#First create a basic app
app = pyaudiogame.App("My hello world app")

#Now make some game logic
def logic(actions):
	"""Our game logic function that gets run every iteration of our app's running loop"""
	if actions['key'] == "space":
		spk("Hello world")

#Put our logic into the app
app.logic = logic

#Run our app
app.run()
