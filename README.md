<title>Readme for pyaudiogame</title>


<h1>About</h1>
Libaudiogame is a toolkit for creating audio games in python<br/>
In just a few lines of code, you can have a game window running and a place for your game logic.<br/>
<h1>Requirements</h1>
You need to have
<a href="http://hg.q-continuum.net/accessible_output/">Accessible_output</a>
and
<a href="http://hg.q-continuum.net/libloader/">libloader for accessible_output</a>
<a href="http://hg.q-continuum.net/platform_utils/">Platform_utils for accessible_output</a><br/>
*note* accessible_output is different than accessible_output2. There is some bugs in accessible_output2 currently that keep it from compiling, so that is why it is not intigrated yet. If you wish to use accessible_output2, please go to:<br/>
pyaudiogame/speech.py and uncomment the imports to accessible_output2 and comment the ones to accessible_output.<br/>
Also note that you need an older version of platform_utils than is on the website. see the<br/>
requires/platform_utils<br/>
for the setup.py.
<br/><br/>
You also need
<a href="http://pygame.org/download.shtml">pygame</a>
to run this package.

<h1>Code example</h1>
<pre>
#Hello world example
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
</pre>
<br/>
<br/>
Now run the above code and press space to hear "Hello world"<br/>