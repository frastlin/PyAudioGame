<title>lesson 3: but what if -- Basic Tutorial</title>

[Back to Index](index.html)

#But What if...
So we have functions and variables so far.  
You can group code together and name it, but it can't do anything yet. This lesson will teach the fundamental way in which most programs run.  
#Logic  
There are 3 logic seperator statements, 6 comparison statements, 2 boolian statements and 2 nothing statements:  

##logic seperator statements

<table border=1>
<tr>
<td>and</td>
<td>Seperate two statements that both need to be true</td>
</tr>
<tr>
<td>or</td>
<td>Seperate two statements where at leaste one needs to be true</td>
</tr>
<tr>
<td>not</td>
<td>Check for a statement to be False rather than True</td>
</tr>
</table>

##comparison statements

<table border=1>
<tr>
<td>!=</td>
<td>Is not equal to</td>
</tr>
<tr>
<td>==</td>
<td>equals</td>
</tr>
<tr>
<td>&gt;</td>
<td>Greater than</td>
</tr>
<tr>
<td>&lt;</td>
<td>Less than</td>
</tr>
<tr>
<td>&gt;=</td>
<td>Greater than or equal to</td>
</tr>
<tr>
<td>&lt;=</td>
<td>Less than or equal to</td>
</tr>
</table>

##Boolian statements

<table border=1>
<tr>
<td>True</td>
<td>Is something</tr>
</tr>
<tr>
<td>False</td>
<td>Is not something</td>
</tr>
</table>

##Nothing statements

<table border=1>
<tr>
<td>None</td>
<td>Makes a variable False or blank through a word statement</td>
</tr>
<tr>
<td>0</td>
<td>Makes a variable False or nothing but through a numeric statement</td>
</tr>
</table>

#What the statements mean
##and  
Say you are looking for a cat. Not just any cat, but a fat black cat. Fat and black are the only 2 specifications. You go to the petstore and see several different cats.  
The first one is fluffy, white and medium.  
Is he fat and black? no. Not what you want.  
The next cat is mean, fat and orange.  
Is he fat? Yes.  
Is he black? No.  
So he is not the cat we want.  
The third cat is fat, has a shedding problem, is not house-broken and black.  
Is he fat? Yes.  
Is he black? Yes.  
Is he the cat we want? ... Well yes!  
We said in python:

	if cat.color == "black" or cat.size == "fat":
		buy(cat)

So despite not being house-trained or a clean cat, he fits our two specifications and is what we want.  
##or
Now after a few weeks with your new fat and black cat, your mom asks you to get her a cat that is either skinny or younger than 2 years. She lives on a farm and really wants a cat that can catch her mice. So you go back to the petstore and see some more cats.  
The first cat is:  
Orange, likes to eat carrots, is 3 years old and fat.  
Is it skinny? No. is it younger than 2 years? No. so it is not what we want.  
The next cat is Blue, is fat and is 6 months old.  
Is it skinny? No. Is it younger than 2 years? Yes.  
Is it the cat your mom wants? Yes.  
So how we would do this check in python is:  

	if cat.size == "skinny" or cat.age < 2:
		buy(cat)

Now you just hope that your mom won't mind that it's blue!
##not
Now, after a week your mom calls you up and says that she can't stand blue on a cat and that this cat won't even go out side to catch the mice that get into the garage! So no blue and no housecat, but she still wants either a skinny or a cat under 2 years old!  
You reluctantly go back to the petstore and ask to see the other cats.  
The first cat is orange, has been in the house all its life, is skinny and is 4 years old.  
Is it skinny or young? Yes, it's skinny.  
is it not blue? Yes.  
is it not a house cat? No.  
So it doesn't work.  
The next cat is green, fat, is under 1 year and loves sleeping on the couch 23 hours out of the day.  
Is the cat skinny or under 2 years old? Yes, it is under 2 years old.  
is it not blue? Yes, it's green.  
Is it not a housecat? No, it is a house cat.  
So it doesn't work either.  
The next cat loves being outside, is a renown mouse catcher at only 1 year old, is skinny and blue.  
Is it either skinny or under 2 years old? Yes.  
Is it not blue? No.  
Is it not a housecat? yes.  
Darn, so close but so far! You think about calling your mom and letting her know about this cat, but think to try one more cat.  
The next cat is a mangy brown cat that is skinny and has never been owned by anyone before.  
Is it skinny or under 2 years old? Yes.  
is it not blue? Yes.  
is it not a housecat? Yes.  
Awesome, this is the cat your mom wants!  
In python this check would look like:  

	if (cat.size == "skinny" or cat.age < 2) and (cat.color != "blue" and not cat.housecat):
		buy(cat)

Note the () between the different statements of checks. You can do this to separate different sets of checks. So python does one set and says if the whole set is a yes or a no, then does the second statement to say if it is a yes or a no. In this case, we have an "and" between the two statements, so we need both statements to be yes in order to buy.
##boolian statements
In all programming languages, programmers use something called boolian statements to say if something is or is not. We used "yes" and "no" above, but in programming we would use True or False. In particular, when we were checking if a cat was a "housecat" we were checking a boolian statement.  
if not cat.housecat:  
If we looked at what housecat is, it would either be True or False.
##Nothing statements
There is also something similar to boolian statements, or the False statement in particular. One could say that there is no data on that part of a cat. So say there was a stray. No one knows how old it is or if it is a house cat or not. So if you looked at what cat.age was, it would say 0 and if you looked at cat.housecat, it would say None.  
This is a great way of creating variables that will then be changed later in the script, but that you have no data on yet. It makes code more readable and if you have a nothing statement (in programming speak they are culled a "null operator"), you can run a function on them.  
The vet has one of these when he checks the cat. It looks like:  

	if not cat.age:
		check_age(cat)
	if not cat.housecat:
		check_history(cat)
	if cat.sick:
		treat(cat)


It doesn't matter what those functions are, they are just something that the vet does. But he uses a check to see if there is a null operator for cat.age and cat.housecat.  
Cat.sick could also have a null operator, but why? it doesn't make sense if someone asks "Is the cat sick" and the reply is "None". If the reply was "True" or "False" which are programming speak for "yes" and "no", it makes a lot more sense.

#if, elif and else
Along with all the logic statements, there are 3 kinds of statements for a logic block. They are:  
if  
elif  
else  
In english we say:  
if something, than do item1, elif this other thing, do item2, else do item3.  
Taking from our vet example above, if the vet finds that cat.sick == True, he runs another block of statements that look like:  

	if not cat.shots:
		shoot(cat)
	elif cat.shots == "partly":
		finish_shooting(cat)
	if cat.cough:
		if cat.cough == "hairball":
			hairball(cat)
		elif cat.cough == "tuberculosis":
			putdown(cat)
		elif cat.cough == "cold":
			decongestant(cat)
			cough_medicine(cat)
		else:
			cough_medicine(cat)

OK, there is a lot in the above example, first, you can see that we can have as many elif statements as we wish, but we can only have one if and one else statement.  
Second, it is perfectly fine to put if statements under other if statements. This replaces the need for super long logic lines.  
\*warning\* It is OK to put logic statements under other logic statements, but if you are finding that you are going above 3 indentations, you should consider placing the logic statement into another function.

#Code
	#if elif else
	import pyaudiogame
	spk = pyaudiogame.speak
	MyApp = pyaudiogame.App("My Application")
	
	#Lets check if they pressed the right keys
	def check_keys(key):
		if key == "1":
			spk("Great, you are correct!")
		elif key == "return" or key == "space":
			spk("This is also correct!")
		elif key == "f2":
			spk("And you found the hidden key that's correct!")
		else:
			spk("Nope, try again, I'm sorry")
	
	def logic(actions):
		key = actions['key']
		#Lets see if there was really a key press
		if key:
			check_keys(key)
	
	MyApp.logic = logic
	MyApp.run()

#What you should see
if you press 1, a message says "Great, you are correct!"  
if you press return or space, a message says "This is also correct!"  
if you press f2 a message says: "And you found the hidden key that's correct!"  
All other keys will say: "Nope, try again, I'm sorry"  

#assignment
This lesson was a very long and difficult lesson. So I would like you to stay on it for about a week, just digesting everything. I would also like it if you went to a chapter in Learn Python the Hard Way and memorised the
[Truth tables he created.](http://learnpythonthehardway.org/book/ex27.html)  

#extra credit
1. Go back through all the other code up to this point and comment above each if statement and explain what it does.
2. Look through some of the examples in the examples/basic_games folder and comment above each if statement saying what it does.
