<title>Lesson 6: Balista! -- Basic Tutorial</title>

[Back to Index](index.html)

__________

#Bombs away!
This is the last thing you need to learn before being able to make a game!  

#Managing items
In python we often need to be able to access items in order. For example, we need to know what sceen we're on. We have a variable that says that we are on sceen 14, but currently it would be really dificult to get from sceen 13 to 14. There is this lovely construct called a  
list  
Lists are used in many different ways, from checking to see if a key is in a list of keys to figuring out if a script has run before.  
Lists have a group of built-in functions that one can use to manage them. These include:  

<table border=1>
<tr>
<td>append</td>
<td>Add the item passed to it to the end of the list</td>
<td>listName.append("Fred")</td>
</tr>
<tr>
<td>pop</td>
<td>remove the number of the item you passed to it from the list. If no number is given, remove the last item.</td>
<td>listName.pop(3) -> removed item</td>
</tr>
<tr>
<td>insert</td>
<td>Add an item at the position given. The order is position item.</td>
<td>listName.insert(4, "Fred")</td>
</tr>
<tr>
<td>remove</td>
<td>remove the item that is passed. So if the list has "pizza" in it and you pass "pizza" to the remove function, "pizza" will be removed from the list</td>
<td>listName.remove("pizza")</td>
</tr>
<tr>
<td>index</td>
<td>Find out what number in the list the item that is passed is in the list</td>
<td>listName.index("Fred") -> number in the list of "Fred"</td>
</tr>
</table>

To make a list you type brackets:  
[]  
around a list of things seperated by commas like:  
["fred", "sam", 42, "pizza"]  
A list is just like a string or an int, it can be assigned to a variable. So  
list1 = ["fred", "sam", 42, "pizza"]  
would be assigned to list1. Now you can type the above functions after list1 to have them run like:  
list1.pop()  
will remove pizza from the list.  
You can refer to an item in the list by typing:  
list1[0]  
list1[1]  
Wait, why is there a 0 there?  
lists are on the cardinal numbering system. This means that everything starts from 0 rather than 1. Doing things this way means that it's much easier to do equasions with numbers. For example, if you would like to check if a list of sceens have been run, you can type something like:  
if not `scene_counter`:  
      `scene_counter` +=1  
    `run_scene()`  
This is much clearer and concise than any other way you could write it.  
So when working with lists, just know that you need to subtract 1 always.  

#before typing the code
This code has a lot of strange things in it and it is really long, so type everything and get it running. Everything will be explained below.

#code
	#Pizza please
	import pyaudiogame
	from pyaudiogame import storage
	spk = pyaudiogame.speak
	MyApp = pyaudiogame.App("Pizza Please")
	
	storage.screen = ["start"]
	storage.toppings = ["cheese", "olives", "mushrooms", "Pepperoni", "french fries"]
	storage.your_toppings = ["cheese"]
	storage.did_run = False
	
	def is_number(number, topping_list):
		"""Will check that what the user enters is really a number and not a letter, also that it is within our list"""
		if number in "0123456789":
			number = int(number)
			if number <= len(topping_list)-1:
				return number
	
	def say_message(message):
		"""Will check if the message has been read and if so, passes. Else, it will read the message"""
		if not storage.did_run:
			spk(message)
			storage.did_run = True
	
	def add_topping(key):
		"""Will add a topping to your pizza"""
		number = is_number(key, storage.toppings)
		if number or number == 0:
			storage.your_toppings.append(storage.toppings[number])
			spk("You added %s to your pizza. Your pizza currently has %s on top" % (storage.toppings[number], storage.your_toppings))
	
	def remove_topping(key):
		"""Removes toppings from the pizza"""
		number = is_number(key, storage.your_toppings)
		if number or number == 0:
			t = storage.your_toppings.pop(number)
			if t == "cheese":
				spk("You can't remove cheese, what are you, Italian?")
				storage.your_toppings.insert(0, "cheese")
			else:
				spk("You removed %s from your pizza. Now your pizza has %s on top" % (t, storage.your_toppings))
	
	def logic(actions):
		"""Press a and d to switch from adding and removing toppings, press 0-9 to deal with the toppings and press space to eat the pizza"""
		key = actions['key']
		if key == "d":
			spk("Press a number to remove a topping from your pizza, press a to add toppings again")
			storage.screen[0] = "remove"
			storage.did_run = False
		elif key == "a":
			spk("Press a number to add a topping to your pizza. Press d to remove a topping you don't like")
			storage.screen[0] = "add"
			storage.did_run = False
		elif key == "space":
			spk("You sit down to enjoy a yummy pizza. You eat... eat... eat... eat... and are finally done. That was good! Now it's time for another!")
			storage.your_toppings = ['cheese']
			storage.did_run = False
		elif storage.screen[0] == "start":
			spk("Welcom to pizza madness! Here you can build your own pizza to eat! Press a to add toppings, press d to remove them and when you are done, press space to eat your yummy pizza!!!")
			storage.screen.remove("start")
			storage.screen.append("add")
		elif storage.screen[0] == "add":
			say_message("Please choose a number of toppings to add! Press d to start removing toppings. Toppings are %s" % storage.toppings)
			if key:
				add_topping(key)
		elif storage.screen[0] == "remove" and key:
				remove_topping(key)
	
	MyApp.logic = logic
	MyApp.run()

#What you should see
When you run the script, the screen will pop up and you will hear:  
"Welcom to pizza madness! Here you can build your own pizza to eat! Press a to add toppings, press d to remove them and when you are done, press space to eat your yummy pizza!!!"  
"Please choose a number of toppings to add! Press d to start removing toppings. Toppings are ["cheese", "olives", "mushrooms", "Pepperoni", "french fries"]"  
If you press 1 it will say:  
"You added olives to your pizza. Your pizza currently has ["cheese", "olives"] on top"  
if you press d it will say:  
"Press a number to remove a topping from your pizza, press a to add toppings again"  
Then if you press a number, it will remove that item from your pizza. If you press 0, it will say:  
"You can't remove cheese, what are you, Italian?"  
If you press space it will say:  
"You sit down to enjoy a yummy pizza. You eat... eat... eat... eat... and are finally done. That was good! Now it's time for another!"  
And your toppings will be reset.  

#What is going on?
Lets go through this code one step at a time:  

	#Pizza please
	import pyaudiogame
	from pyaudiogame import storage
	spk = pyaudiogame.speak
	MyApp = pyaudiogame.App("Pizza Please")

We have our imports like always. We import pyaudiogame, we import pyaudiogame.storage, then we assign spk to the function pyaudiogame.speak. Finally we assign MyApp to pyaudiogame.App with the title "pizza please".  

	storage.screen = ["start"]
	storage.toppings = ["cheese", "olives", "mushrooms", "Pepperoni", "french fries"]
	storage.your_toppings = ["cheese"]
	storage.did_run = False

Here we create our variables. We have one constant, storage.toppings, but in order to make everything match, we put it in storage.  
storage.screen is a string inside a list that helps us keep track of where we are in the app. This is how one can figure out what what scene should be running and by making this accessible by all the modules in an app, any function can then change the screen of the program.  
`storage.your_toppings` is the list that we change most, it is the player's list of toppings.  
`storage.did_run` is the most checked variable, it is checked every time the game loop runs. It says if the message that is the instructions for each screen has run or not.  
Wait, what is storage?  
Storage is a built-in module where you can place variables, lists and what ever you would like to access throughout the life of the game in any module. It is built to be your global variable place.  

	def is_number(number, topping_list):
		"""Will check that what the user enters is really a number and not a letter, also that it is within our list"""
		if number in "0123456789":
			number = int(number)
			if number <= len(topping_list)-1:
				return number

We have a lot of new things in this function, so lets go through it line by line:  

	def is_number(number, topping_list):

This function is what we call an error checkor. It checks that the program won't crash if the user enters a letter or a number that is out of range.  

		"""Will check that what the user enters is really a number and not a letter, also that it is within our list"""

This line is what we call a dockstring. It is what should always be placed on the first line of the function block. It describes why we have the function and a little of what it does. Up to this point we haven't been using so many dockstrings, but from now on, they should be in just about every function.  

		if number in "0123456789":

This checks if the number we are checking is really a number. The in statement checks in lists and strings. It is much better than writing or statements. So if we wished, we could type something like:  
if number in ["1", "2", "3", "4", "5", "6"]  
This will check in a list rather than a string. But as we are checking one character that is a string, we can just use a larger string.  

			number = int(number)

You can convert from one type to another by using the type function. There is an str function, there is a float function, there is an int function, there is a list function and a function for any other type you need. We need to convert to an int so we can access an item in a list.  

			if number <= len(topping_list)-1:

One can't do <= with a string very well. Len is a built-in function that will give the amount of items in a list or string. But remember, lists begin from 0 rather than 1, so if we had the len without the 1, we would pass a number that is too high and will raise an error. You can also just say if number < `len(topping_list)`:, but I think this way is clearer.  

				return number

The return statement is not something we have done before. Return is a way for a function to become a value. So if a number was passed to the function `is_number` and that number fit all the requirements, it would be returned. You can have a variable equal a function as well. We will see this later.  
Note that a function always returns something, but if nothing is given, it returns None.  
You can only return one value, but a list counts as one value and you can assign 2 or more variables to a list/function that returns a list like:  
name, age = ["Joe", 42]  
  
	def say_message(message):
		"""Will check if the message has been read and if so, passes. Else, it will read the message"""
		if not storage.did_run:
			spk(message)
			storage.did_run = True

This function makes sure that we run a function that says a message only once. This function is run every loop and if we didn't have it, our screen reader would be speaking the message 30 times a second.  

	def add_topping(key):
		"""Will add a topping to your pizza"""
		number = is_number(key, storage.toppings)

We define a function with the argument of the current key. Then we have the dockstring, then we run the function we created above, the `is_number` function. We pass the key and the list that we are going to check the length of.  

		if number or number == 0:

We check that there is a number that returned. We have a bug if we just say the first statement though as 0 is considered nothing, so will not be alowd through unless we say it is alowd explicitly.  

			storage.your_toppings.append(storage.toppings[number])

Here we append to `your_toppings` the topping from the toppings list.

			spk("You added %s to your pizza. Your pizza currently has %s on top" % (storage.toppings[number], storage.your_toppings))

Here we say the topping that we just added to the `your_toppings` list and the list of `your_toppings.` The reason why we can say the list of `your_toppings` is because we converted it to a string with the `%s` string formatter.  

	def remove_topping(key):
		"""Removes toppings from the pizza"""
		number = is_number(key, storage.your_toppings)
		if number or number == 0:
			t = storage.your_toppings.pop(number)

The first half of this function is the same as the `add_topping` function, but this last line brings a new function. The pop function. Pop will remove what ever number you tell it to remove and if there is no argument, it removes the last item. We are giving it the number that the player typed here.  

			if t == "cheese":
				spk("You can't remove cheese, what are you, Italian?")

The pop function will return the item that it popped, so that means that t is the popped item. Here we are checking if the pop item is cheese. If it is cheese, we will send a message saying that you can't remove cheese.  

				storage.your_toppings.insert(0, "cheese")

The insert function does exactly what it sounds like. It inserts an item into the list at the location you specify. Here we are inserting an item at the top of the list. The argument order is the location and then the item you wish to insert.  

			else:
				spk("You removed %s from your pizza. Now your pizza has %s on top" % (t, storage.your_toppings))

If t is not equal to cheese, we will keep it removed and send a message that the user removed the item and then say what toppings are left on the pizza.  

#assignment
1. Read the python documentation on lists.
2. Add another option for changing the sauce to be either pesto, white or red.

#Extra credit
1. Make it so that you can remove extra  cheese, but not the first cheese. \*hint\* check out len.
2. make it so you can't add more than one of each topping, but double cheese.
3. This looks almost like a game. Make it into a game somehow.
4. Use every list operation in some way, either in this program, or in another.
5. read the [API documentation](../API/storage.html) on storage. Try out save and load.
