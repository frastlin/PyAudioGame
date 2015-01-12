#This is a hello world example using the more powerful sub-classing option
from pyaudiogame import App
from pyaudiogame.speech import speak as spk

class MyApp(App):
	"""We create our class as a child of App and we can sub-class the logic function which is run each iteration of the game loop."""
	def logic(self, actions):
		"""actions is a dict of all the input events, like keyboard and mouse"""
		if actions['key'] == "space":
			spk("Hello world")

if __name__ == '__main__':
	#call the run function for our app to begin the game loop. press escape to exit.
	MyApp().run()