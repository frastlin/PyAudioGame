#Working with variables
import pyaudiogame
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

#Here are some variables
#Lets first write one line of text
my_name = "Frastlin"

#now lets write a number
my_age = 42

#now lets write several lines of text
my_song = """
My application tis to be,
the coolest you've ever seen!
"""

#Magic time!
def logic(actions):
	key = actions['key']
	if key == "a":
		#Here is our one line of text, it will speak when we press a
		spk(my_name)
	elif key == "s":
		#Here is our number, it will speak when we press s
		spk(my_age)
	elif key == "d":
		#Here is our multiline text example. It will speak when we press d
		spk(my_song)

MyApp.logic = logic

MyApp.run()