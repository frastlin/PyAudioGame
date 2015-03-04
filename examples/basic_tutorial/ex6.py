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
