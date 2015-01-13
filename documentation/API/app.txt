<title>pyaudiogame.App -- PyAudioGame API</title>

[API](index.html)
__________

#pyaudiogame.App
pyaudiogame.App(title="Test app", fps=30)  
The master/main class of the pyaudiogame engine.
- title is the name of your application's window.
- fps stands for frames per second and is how many times your game loop runs each second. The default is 30, but most graphical applications run at 60. Audio games do not use graphics, so don't really need the extra speed. Having the loop speed this low means that the app takes up much less memory.

<table border=1>
<tr>
<td>pyaudiogame.App.__init__</td>
<td>The initialization function of the pyaudiogame.App class</td>
</tr>
<tr>
<td>pyaudiogame.App.logic</td>
<td>The method/function where all the game logic goes.</td>
</tr>
<tr>
<td>pyaudiogame.App.set_defaults</td>
<td>A method that is run in init. This is to make a nice easy way of setting default settings when sub-classing</td>
</tr>
<tr>
<td>pyaudiogame.App.run</td>
<td>Creates the screen and starts the game loop</td>
</tr>
<tr>
<td>pyaudiogame.App.key_repeat</td>
<td>Toggles and sets what holding down a key does</td>
</tr>
<tr>
<td>pyaudiogame.App.event_queue.schedule</td>
<td>Place all events that need a timer in this function</td>
</tr>
</table>

##Description
The pyaudiogame.App class provides the core functionality needed to run an application. It captures keyboard input and schedules and runs events.

##logic
logic(actions) -> bool  
The function you over-ride and fill with game logic.  
Return a False when you wish the game loop to quit.  
 The actions is a dict of keyboard and mouse events as follows:  
	*['mousex'] The x coordinate of the mouse  
	*['mousey'] The y coordinate of the mouse  
	*['key'] The name of a key as a string. For example "space", "f", "return", "up"... To figure out what a key is, go to examples/keyboard_test.py  
	*['mouseClicked'] The state of the mouse click  
	*['mods'] a list of mod keys like ['ctrl', 'shift'] means that ctrl and shift are held down. ['shift'] means that just shift is held down  

##`set_defaults`
`set_defaults(self)` -> None  
Should really only be sub-classed to change the class variables. it is run when the class is initialized.

##run
run() -> None  
Creates the screen and starts the game loop. Call this at the bottom of your main script to start the app.

##`key_repeat`
`key_repeat(self, on=True, delay=1000, delay_before_first_repeat=1)`  
Toggles on and off what happens when a key is held down.  
call with on=False to turn it off and  
just put delay=200  
to turn it back on.

- on Is the toggle. If it is False, the last settings are erased and keys no longer repeat.
- delay is the number of milliseconds between each key repeat. By default a key event repeats every second when it is held down.
- `delay_before_first_repeat` is the amount between the first event and the first of the repeating events. By default this is set to 1 millisecond as most people wish their repeating keyboard events to be steady. Passing 0 to this will toggle off the repeating.

##`action_queue.schedule`
`schedule(function, delay=0, repeats=1, before_delay=False, *args, **kwargs)`  
Adds a function to the event queue to run delay seconds later.  

- function is a function like `hello_world()` but without the (). So like `hello_world`. This function will run after or before the wait and will repeat the number of times specified.
- delay is the time in seconds before the event will run. It does take a float, so 0.5 or 1.7659208 will work as well.
- repeats is the number of times a function will run. If value is 0, the function will run for ever.
- `before_delay` if True will set the function to run before the timer runs. This is mostly used for repeating functions.
- `*args **kwargs` If the function that is passed in takes arguments, they can be specified by either placing them after all the above arguments, or better, labeling them with keywords. So if our `hello_world` function takes name as an argument, a schedule would look like:  
`schedule(hello_world, 1, name="Joe")`  
This will schedule `hello_world` to run one time in one second and `hello_world` will be passed the argument name.

##default attributes/variables
These are settings that can be changed or accessed by typing `App.variable_name.`  

- windowwidth = 640
- windowheight = 480  
These first two items determine the size of the screen. Currently it is a little box something like 2 inches by 3 inches.
- fullscreen = False  
If you wish to fill the whole screen, toggle this to True. Note though that if someone has a projector on, this will remove the black screen. It also makes everything larger to fit the full screen.
- mouse = False  
if this is true, a mouse cursor will show.
- `event_queue = ticker.Scheduler(time_format=0.001)`  
Our event queue, the `time_format` is how much to multiply the tick numbers by in order to make a second. Don't change this unless you know what you're doing.
- exit_key = 1  
Even before our logic statement runs, this key is processed. It is recommended to have this on while testing, but to take it off when releasing as nothing is saved when using this key.
