#Many funcky functions!
import pyaudiogame
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

#Our first function we will call funky
def funky():
	spk("Hello, I'm funky!")

#Lets make some variables
player1_level = 99
player2_level = 92

#and lets make a function to say our player's levels
def say_level(player_level):
	spk("I am level ")
	spk(player_level)

#Now lets make a not so magic function that is filled with magic!
def logic(actions):
	key = actions['key']
	if key == "space":
		funky()
	elif key == "1":
		say_level(player_level=player1_level)
	elif key == "2":
		say_level(player2_level)

MyApp.logic = logic

MyApp.run()