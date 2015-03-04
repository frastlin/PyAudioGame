#Here are all the different scenes for the different rooms
import random
from pyaudiogame import storage
from pyaudiogame import speak as spk

def add_text(text):
	storage.text = text

def start():
	add_text("Welcome to pie Heavens! Press return to blast off into space and escape to exit!")

def start2():
	add_text("""Floating between the stars, no end in sight. Hot from the oven, ready for someone to take a bite.
A Hot Apple Pie gifted with space flight.
The Milky Way bites swarm all around, but the crown to control still must be found.
For a lost pie in space is never aloud.
Forks and knives are used to hurt and you blast heat for a chocolate milting spurt.
Press the arrow keys to go randomly drift. If you happen to hit a chocolate foe melt it with space or controll.
""")
	storage.screen = "drift"

def healroom():
	add_text("""Near a red giant
A bright red glow spreads out from a massive star relatively close by. The heat helps a pie weld itself back together.
""")
	num = random.randint(1,int(storage.player_max_hp/2))
	if storage.player_hp + num <= storage.player_max_hp:
		storage.player_hp += num
	else:
		storage.player_hp = storage.player_max_hp

def damageroom():
	add_text("""Escaping a black hole
Yikes! That is a black hole! Sometimes drifting is not all it's cracked up to be... But now you are... All cracked up... Ouch!
""")
	num = random.randint(0,storage.player_max_hp/3)
	num = int(num)
	storage.player_hp -= num
	if storage.player_hp <= 0:
		storage.player_hp = 1

def room1():
	add_text("""Closer into the red giant
This massive red star is nearing the end of its shining life. At this point the star is poofed up like a balloon with a small dense center of helium that is turning into carbon. The red is due to the relatively cool exterior, but one would still want to keep its distance. Soon though, the force in the center of the star will die and the entire outer layer will implode, making a very squozen ball of mass.
""")

def room2():
	add_text("""With the cheeses
Chilling chunks of cheese are floating around you. Earth is not the only moon with its satellite made out of cheese and most planets with moons have more than one. This planet has 37 and they are all made out of cheese. Wonder what they call the largest moon? Probably the big cheese.
""")

def room3():
	add_text("""Between the Stars
Between the countless dots of light, time is inconsequential. Space is all that matters. With light years between each star, drifting turns into something only another drifter can understand.
""")

def room4():
	add_text("""By an Asteroid
A giant hunk of metal and rock is orbiting around the nearest star. Dust from past collisions cover the surface. Talk about being hard headed...
""")

def room5():
	add_text("""Overlooking a Planet
Dull and seemingly lifeless, this massive collection of elements has formed a very dense and massive rock. What makes this different from Asteroids is first the size, it is much larger than any asteroid could ever be. Second, this hunk of junk has an atmosphere of gas!
""")

def room6():
	add_text("""Around a Neutron Star
This corpse is the result of a fairly large star that became a red giant, and then became so dense that all the corks became neutrons. The mass is not enough for a black hole, but it was too much for a white dwarf.
""")

