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