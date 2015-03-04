<title>Lesson 4: wait, is that math? -- Basic Tutorial</title>

[Back to Index](index.html)

__________

#code

	#ATTACK!!!
	import pyaudiogame
	spk = pyaudiogame.speak
	MyApp = pyaudiogame.App("My Application")
	
	#Lets create a storage box so we can put our draggon's hp in there
	from pyaudiogame import storage
	
	#Now lets make our draggon's hp in the storage
	storage.dragon_hp = 100
	
	#Now lets make our hero's hit strength
	hero_hit = 10
	
	#An attack function
	def attack():
		#When the hero attacks he takes the dragon's hp
		storage.dragon_hp = storage.dragon_hp - hero_hit
	
	#Now lets make a way for our hero to attack
	def logic(actions):
		key = actions['key']
		if key == "space" and storage.dragon_hp > 0:
			attack()
			spk("You, the hero of our tail swing your sword. You hit the dragon for %s damage! Now our poor dragon has %s hp left" % (hero_hit, storage.dragon_hp))
			if storage.dragon_hp <= 0:
				spk("You, the hero of our story killed the dragon. The whole town thanks you!")
				spk("Press escape to go back home")
	
	MyApp.logic = logic
	MyApp.run()

#What you should see
Press space and you should hear:  
"You, the hero of our tail swing your sword. You hit the dragon for 10 damage! Now our poor dragon has 90 hp left"  
hit space again and you hear  
"You, the hero of our tail swing your sword. You hit the dragon for 10 damage! Now our poor dragon has 80 hp left"  
Hit space 8 more times and you will hear:  
"You, the hero of our tail swing your sword. You hit the dragon for 10 damage! Now our poor dragon has 0 hp left"
"You, the hero of our story killed the dragon. The whole town thanks you!"  
"Press escape to go back home"

#What just happened?
Lets go through the code line by line:  

	#ATTACK!!!
	import pyaudiogame
	spk = pyaudiogame.speak
	MyApp = pyaudiogame.App("My Application")

These are just the normal magical lines we have had all throughout.  

	#Lets create a storage box so we can put our draggon's hp in there
	storage = pyaudiogame.cash

pyaudiogame has a module for storing data. That probably makes no sense right now, but in the next few lessons you will learn all about this. Just know that after writing this line, you can store variables in storage. People may say something about "global" variables and those are used, but this way is more "pythonic" and safer as there is no way you will mistake `storage.dragon_hp` for anything except for what it is. In pyaudiogame.storage there is also some features for saving data from one session to the next you will learn about later.  

	#Now lets make our draggon's hp in the storage
	storage.dragon_hp = 100

Here is how we store our variable that we will be accessing later in the program. You can store any variable in storage, it is just like what we do with normal variables, but we can change this variable.  

	#Now lets make our hero's hit strength
	hero_hit = 10

This is a variable we've seen before. Here is another term: "constant" The hero_hit will not be changed throughout the life of our program, so it is called a "constant variable".  

	#An attack function
	def attack():
		#When the hero attacks he takes the dragon's hp
		storage.dragon_hp = storage.dragon_hp - hero_hit

Here is what seperates a constant from a variable in storage. The variable in storage can be added to or subtracted or changed completely where as the constant must stay the same. Go ahead and try to make `dragon_hp` a constant and run the program. Do you see that error? It is saying that there is no variable named `dragon_hp` even though you wrote it right above. This is because there is a thing in python called a "namespace". This means that a file has a namespace and a function has its own namespace. The function can see the file's namespace, but only on a read-only basis. The file can't see the function's namespace at all.  
This is to help you keep your program organized and easy to read. It also allows for great functionality when you start writing your game in many files (what we will go over later).  

	#Now lets make a way for our hero to attack
	def logic(actions):
		key = actions['key']
		if key == "space" and storage.dragon_hp > 0:
			attack()
			spk("You, the hero of our tail swing your sword. You hit the dragon for %s damage! Now our poor dragon has %s hp left" % (hero_hit, storage.dragon_hp))
			if storage.dragon_hp <= 0:
				spk("You, the hero of our story killed the dragon. The whole town thanks you!")
				spk("Press escape to go back home")

Here we are using 2 if statements. 1 will remove hp and run the attack function if the dragon's hp is above 0. The other if statement will run only if the dragon's hp is 0 or below.  

	MyApp.logic = logic
	MyApp.run()

Our last two magic statements. But notice that MyApp.logic, MyApp.run() and pyaudiogame.storage look the same. They are all methods of storage. You can save functions into storage by just treating them like variables and using them without the (). So go ahead and change it so that all the code accesses attack from storage.attack(). Look at these last two lines if you don't know how to get attack into storage.  
##Changing variables
One of the pillars of programming is the ability to change variables. You can do this with several operators:  

<table border=1>
<tr>
<td>+</td>
<td>Adds together variables</td>
</tr>
<tr>
<td>-</td>
<td>subtracts variables from one another</td>
</tr>
<tr>
<td>*</td>
<td>multiplies variables together</td>
</tr>
<tr>
<td>/</td>
<td>divides variables by one another</td>
</tr>
<tr>
<td>%</td>
<td>Will give the remaindor of 2 variables divided together</td>
</tr>
<tr>
<td>**</td>
<td>Finds to the power of</td>
</tr>
</table>

Along with the above you can combine = with `+-*/` to get something that looks like x += y. This is short-hand for writing:  
x = x + y  
Short-hand:  
x += y  
##Types
Variables are classified into several types. There are 4 that people run into all the time:  
string (str)  
intiger (int)  
float (float)  
bool (bool)  
We looked at strings the first lesson. They are characters like what you are reading now, but between quotes.  
string1 = "This is a string"  
Intigers are any number that is not in a quote.  
num = 10  
floating-point numbers are numbers with a point:  
float1 = 2.789  
A bool is what we looked at in the last lesson, it is a True or False value:  
bool1 = False  
You can use the operators on ints, floats and strings. Ints and floats can be combined to create a float, but strings can only be added to other strings or multiplied by ints. Bools can't be combined with anything.  
##string formatting
Strings have this nice feature called "string formatting" that allows us to insert variables of other types into a string. There is a huge list of string formatting commands, but the one that is most used is:  
`%s`  
This converts all variables to a string. Here is an example:  

	
	age = 10
	weight = 100.35
	name = "Fred"
	"%s is %s years old and has a weight of %s lbs" % (name, age, weight)
	
	"Hello, I am %s" % name
	
	"If you are %s pounds, I'll pull you out of that bed so we can go walking %s Greggery James!" % (weight, name)
	

If you inserted the lines with quotes into spk(), they will run just fine.  
#assignment
1. Change the attack function so it is stored in storage and called out of storage.
2. Go through the last example and above each variable, write what type it is.
3. Add a level variable, name variable and hp variable to our hero and anounce them.
4. Convert all the long-hand addition and subtraction we used in the above code to the short-hand. People never use the long-hand code, so get used to using x -= y.
5. Go read up on namespaces in python.

#Extra credit
1. Go read about string formatting. See what the difference is between .format and `%s`. Also see what all the different types are. Also find why people would use the other `%` characters and not just stick to `%s` when `%s` works all the time.
2. Make the dragon attack and take hp away from our hero.
3. Add a key to check the health of the hero
4. Add some messages as the dragon reaches a sertan amount of hp, explaining what the dragon is doing.
