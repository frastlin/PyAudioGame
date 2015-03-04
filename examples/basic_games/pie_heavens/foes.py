#This is a module with all the descriptions for the foes
import random

enemy1 = ("Small Milkey Way",
"Directly from Mars, this small piece of chocolate and malt is having a bad nutday!")

enemy2 = ("American Milkey Way",
"450 calories of unadulterated milkey madness with nuts!")

enemy3 = ("UK milkey Way",
"Creamy, smoothe and 99 calories inside a thick chocolate shell. Put this guy in milk to see how he floats.")

enemy4 = ("Forever Yours",
"The evil twin of an already evil chocolate bar! This time you've got twin vanilla to destroy.")

enemy5 = ("Milky Way Midnight",
"Black, small, but more evil than the other bars, this little guy will not give up until someone is dead. Someone better attack before they lose their head.")


def boss1():
	desc =("Giant American Milkey Way, boss number 1!",
"\"The sweet you can eat between meals!\" This milkey way is a giant version of the little guys you have seen before. It is a little more than 450 calories, you better be careful!")
	hp = 500
	hit = 40
	extra_lives = 1
	extra_xp = 150
	return (desc, hp, hit, extra_lives, extra_xp)

def boss2():
	desc =("America, the Milkey Way, boss number 2!",
"\" At work, rest and play, you get three great tastes in a Milky Way.\" Death, milk and ablivian!")
	hp = 1000
	hit = 250
	extra_lives = 1
	extra_xp = 50
	return (desc, hp, hit,  extra_lives, extra_xp)

def boss3():
	desc =("Milkey God, boss number 3!",
"The milkey god says: \"Life's Better the Milky Way.\" Come and join me, don't float away.")
	hp = 200
	hit = 200
	extra_lives = 2
	extra_xp = 500
	return (desc, hp, hit, extra_lives, extra_xp)

def boss4():
	desc =("Milkey Way Magic stars, boss number 4!",
"Pop Star, Jess Star, Bright Star, Super Star, Happy Star, Sport Star and Baby Star are all looking at you... Sorry, we were just Eating our last victim... Hahahahahahahaha!!! You're next!")
	hp = 2000
	hit = 40
	extra_lives = 2
	extra_xp = 1000
	return (desc, hp, hit, extra_lives, extra_xp)

def boss5():
	desc = ("The Giant Way, boss 5!",
"Shiver and crack my flaky foe! You seem a little tarty today, perhaps you would like some ice cream to come your way?")
	return (desc, 2000, 150, 0, 100000)
