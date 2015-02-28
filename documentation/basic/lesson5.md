<title>lesson 5: No, I didn't say my jewels -- Basic Tutorial</title>

[Back to Index](index.html)

#The module
So just like with everything else, programmers like to shroud their craft with fancy words for things that probably don't need it.  
Module is one of these words.  
What is a module? A module is another file with code in it that you can use in your script. Why not call it a file? Because a file doesn't have code in it...  
So we call files with code in them modules.  
The module is something that python is particularly good at. You group functions and tasks into modules so you can manage and read your code better.  
#How to use a module
You call the module's functions or add the module to your namespace by doing two different things:  
For most things, it is best to always do the first as it will make your code cleaner in the end if you choose to use a lot of different functions from the imported module. The first is:  
import moduleName  
This will bring that moduleName into your current module so you can type  
moduleName.function()  
to run a function inside that module.  
The second way is only used if you are only using one function from a module. There is no real speed difference, it just takes up a name in your module's namespace. It is:  
from moduleName import function  
That way you can type:  
function()  
just as if you created it in your current module.  
The next example needs you to make 2 files. Name one  
ex5.py  
and the other  
ex5_1.py  
#code for ex5_1.py

	#My first module!
	from pyaudiogame import speak as spk
	
	def func():
		spk("This is the ex5_1 module!!! Hello world!!!")

#code for ex5.py
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

#What you should see
When you press space you should hear:  
"This is the ex5_1 module!!! Hello world!!!"  
If you press return you should hear:  
"Your random number is: %s!"  
Where `%s` is a random number.
#Built-in modules
Python has something called The
[Python Standard Library](https://docs.python.org/2/library/)
Which is a group of modules that every python instilation comes with. These include a random module for generating random numbers, a time module for dealing with dates and time, a sys module with functions that deal with the computer, os which has functions to tell info about the current operating system, a math module with more complex math functions and somewhere around 100 modules filled with functions.  
In general, if you find that there is a built-in way of doing something, it will be faster for you to use that way than to write your own code for doing the same thing. Always google to see if you can already do something in python before trying to make it yourself.  
#What is going on in our code
##ex5_1.py

	#My first module!
	from pyaudiogame import speak as spk

Here we are using the second type of importing with a little fancy keyword:  
from pyaudiogame import speak as spk  
Instead of typing  
speak("text to speak")  
we are saying that we wish the variable spk to be assigned to speak. That way we have a free speak variable and because spk is something that is typed a lot, we can save our fingers the trouble of typing a 5 letter word. Just put that "as" keyword after the module name and then the new name.  

	def func():
		spk("This is the ex5_1 module!!! Hello world!!!")

This is just a simple function with no call.

##ex5.py
	#fraught with possibility
	import pyaudiogame
	import random
	import ex5_1
	spk = pyaudiogame.speak
	MyApp = pyaudiogame.App("My Application")

Sorry to burst your bubble of magical mystery, but these lines are no more than imports. We are just importing pyaudiogame, random and our ex5_1 module. We are also importing the speak function and we have one line of magic that we know is a variable and something that looks like a function in a module but I will tell you that it is not, it is something we will learn about in a couple lessons.  

	def logic(actions):
		key = actions['key']
		if key == "space":
			ex5_1.func()
		elif key == "return":
			spk("Your random number is: %s!" % random.randint(1,10))

By typing the name of the module,  
ex5_1.func()  
We can use the function from ex5_1.  

	MyApp.logic = logic
	MyApp.run()

And our last two lines that look like modules, but are really not.  

#assignment
1. Add some more functions to the program from the ex5_1 module.
2. Add another module.
3. Check out the python standard for writing code,
[pep8](https://www.python.org/dev/peps/pep-0008/)
and read what it says about imports. Change any code you find or write to follow it. This will make you a better programmer than many.

#extra credit
1. Find what the difference between a module and a package is.
2. Read up on random and find all the different functions that are in it. \*hint\* I like random.choice, random.randint, random.randrange and random.uniform. Why would I like using these and not the others? Write some code that uses these.
3. Find another module from the Python Standard Library  and use some functions from it in your code.
4. Play some games.
