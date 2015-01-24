<title>Lesson 5: Balista! -- Basic Tutorial</title>

[Back to Index](index.html)

__________
#Bombs away!
There is one more super important thing you need to learn before you make your first game in the next lesson. This is how to organize your data.  
#code

#This is the description of the file. This is a template for an app.
import pyaudiogame
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

#put code here

def logic(actions):
	key = actions['key']

MyApp.logic = logic
MyApp.run()
