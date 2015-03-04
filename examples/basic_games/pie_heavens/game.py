#Our import to the builtin modules
import random
#Our imports from pyaudiogame
import pyaudiogame
game = pyaudiogame.App("Pie Heavens")
storage = pyaudiogame.cash
spk = pyaudiogame.speak
#imports from the modules created for this game
import scenes, fight

#Our constants
between_scenes = 2

#Here we have the lists we will use
scene_list = [scenes.healroom, scenes.damageroom, scenes.room1, scenes.room2, scenes.room3, scenes.room4, scenes.room5, scenes.room6]
last_scenes = []

def set_variables():
	"""Will set all the variables in storage"""
	#stored variables
	storage.text = ""
	storage.scene = scenes.start
	storage.screen = "start"
	#player info
	storage.current_foe = None
	storage.player_level = 1
	storage.player_hp = 100
	storage.player_max_hp = 100
	storage.player_xp = 0
	storage.player_deathray_charge = 100
	storage.player_hit = 20
	storage.player_deathray_hit = 0.40
	storage.player_next_level = 100
	storage.player_lives = 3
	#Foe variables
	storage.foe_hp = 100
	storage.foe_max_hp = 100
	storage.foe_hit = 15
	storage.foe_max_hit = 15
	storage.foe_death_message = None
	storage.boss_list = []
	storage.boss = None
	#foe rewards
	storage.extra_lives = 0
	storage.extra_xp = 0

#Lets check if there is a saved game and if not, create the variables to start the game
if not storage.load("pie.sav"):
	set_variables()


def precombat():
	"""This is what changes the screen to combat. It also rolls and checks who goes first"""
	storage.screen = "combat"
	storage.text = "You face the %s! %s HP of pure madness! %s" % (storage.current_foe[0], storage.foe_hp, storage.current_foe[1])
	spk(storage.text)
	spk("Press space or ctrl to attack")
	if random.randint(0,1):
		spk(fight.foe_combat())
		d = fight.death_check()
		if d:
			spk(d)

def leveled():
	"""Will set the boss for the new level, or check for the finish of the game"""
	if storage.current_foe:
		storage.screen = "combat"
		storage.text = "You have %s hp and the %s has %s hp" % (storage.player_hp, storage.current_foe[0], storage.foe_hp)
		spk(storage.text)
	else:
		storage.screen = "back_to_drift"
	if not storage.player_level % 2:
		storage.boss_list.append(fight.bosses[storage.player_level/2-1])

def drifting():
	"""This will select a new, random scene and, if needed, remove the first item from the last_scenes list, then it will take the chosen scene and remove it from the scene_list. Then it will ad that scene to the end of the last_scenes list. The reason why we have both these lists is to make sure that players don't return to the same room too soon."""
	fight.charge_deathray()
	storage.scene = random.choice(scene_list)
	if len(last_scenes) == between_scenes:
		scene_list.append(last_scenes.pop(0))
	last_scenes.append(storage.scene)
	scene_list.remove(storage.scene)

def change_scene(extra_text):
	"""Will change the scene and add the message there is an enemy if needed"""
	storage.scene()
	storage.scene = None
	if extra_text:
		storage.text += extra_text
	spk(storage.text)

def single_keys(key):
	"""Is where all the single pressed keys are checked for"""
	s = storage.screen
	if key == "r":
		spk(storage.text)
	elif key == "x" and storage.screen != "start":
		spk("You are level %s and have %s xp and need %s xp till you reach level %s" % (storage.player_level, storage.player_xp, storage.player_next_level - storage.player_xp, storage.player_level + 1))
	elif key == "h" and storage.screen != "start":
		spk("You have %s out of %s HP" % (storage.player_hp, storage.player_max_hp))
	elif key == "l" and storage.screen != "start":
		spk("You have %s lives left" % storage.player_lives)
	elif key == "c" and storage.screen != "start":
		spk("The death ray is %s percent charged" % storage.player_deathray_charge)
	elif key == "g" and storage.screen == "combat":
			spk("The %s has %s of %s hp left" % (storage.current_foe[0], storage.foe_hp, storage.foe_max_hp))
	if key == "1":
		print(storage.save(level=0))

def logic(actions):
	key = actions['key']
	extra_text = ""
	if storage.screen == "start" and key == "return":
		storage.scene = scenes.start2
	elif (storage.screen == "drift" and key in ['left', 'right', 'up', 'down']) or storage.screen == "back_to_drift":
		if storage.screen == "back_to_drift":
			storage.screen = "drift"
		drifting()
		extra_text = fight.combat_check()
	elif storage.screen == "combat" and key in ['right ctrl', 'left ctrl', 'space']:
		fight.combat(key)
	elif storage.screen == "precombat" and key == "return":
		precombat()
	elif storage.screen == "leveled" and key == "return":
		leveled()
	elif storage.screen == "dead" and key == "return":
		spk("The god of pies grants you another chance to prove your worth. Do not fail him again...")
		set_variables()


	single_keys(key)

	if storage.scene:
		change_scene(extra_text)

game.logic = logic
game.run()