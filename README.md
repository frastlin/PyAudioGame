Readme for pyaudiogame


# About

pyaudiogame is a toolkit for creating audio games in python  
In just a few lines of code, you can have a game window running and a place for your game logic.  

# Where to download

You can download [from pypi](https://pypi.org/project/pyaudiogame/)  
type:  

	pip install pyaudiogame

if you are on windows, also type:

	pip install pywin32

or, if you would like to get all the new updates  
[go here for the latest git version](https://github.com/frastlin/PyAudioGame)  
Clone the repository and type:

	python setup.py install

Also checkout  
[The official website for the latest news](http://frastlin.github.io/PyAudioGame/)

# Requirements

the console input functionality does not work on python 3.7, and accessible_output2 to a screen reader does not work on python 2.  
The dependencies for this package are pygame, and if you are on Windows, pywin32.

# Code example
<pre>
#Hello world example
import pyaudiogame
from pyaudiogame import speak as spk
#First create a basic app
app = pyaudiogame.App("My hello world app")

#Now make some game logic
def on_input(event):
	"""A function that is run whenever there is some kind of event."""
	# key is the name of the key, and state is either 0 for released or 1 for pressed.
	if event.key == "space" and event.state == 1:
		spk("Hello world")

#Put our logic into the app
app.add_handler(on_input)

#Run our app
app.run()
</pre>  
<br/><br/>  

Now run the above code and press space to hear "Hello world"  

#Documentation

There are pretty extensive comments in the different modules, but better documentation is coming soon!
