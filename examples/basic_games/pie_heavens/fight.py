#The fighting functions
import random
from pyaudiogame import storage
from pyaudiogame import speak
import messages, foes

#constants that can only be seen in this module, but are just like the ones in game.py
chance_of_foe = 50 #percent
chance_to_hit = 70 #percent
xp_per_hit = 0.5
xp_multiplyer_tnl = 2
hit_gain = 0.3

#our list of foes
foe_list = [foes.enemy1, foes.enemy2, foes.enemy3, foes.enemy4, foes.enemy5]
bosses = [foes.boss1, foes.boss2, foes.boss3, foes.boss4, foes.boss5]

def spk(text, state=2):
	"""Will either just speak text with state being 0, append to the text with it being 1 or replace the text with it being 2."""
	if state == 1:
		storage.text += "\n" + text
	elif state == 2:
		storage.text = text
	speak(text)

def charge_deathray():
	"""Will charge the deathray"""
	charge = 10
	if storage.player_deathray_charge <= 100-charge:
		storage.player_deathray_charge += charge
	else:
		storage.player_deathray_charge = 100


def combat_check():
	"""This checks if there should be an enimy in the room"""
	n = random.randint(1,100)
	if n <= chance_of_foe:
		boss_message = boss_check()
		if not boss_message:
			make_foe()
			storage.screen = "precombat"
			return random.choice(messages.see_foe_messages) + "\npress return to begin the fight!"
		return boss_message


def make_foe(hp=0, foe=None, hit=0):
	"""Will set the variables for the foe"""
	if not hp:hp = random.randint(storage.player_max_hp-30, storage.player_max_hp+30)
	storage.foe_hp = hp
	storage.foe_max_hp = hp
	if not foe:foe = random.choice(foe_list)
	storage.current_foe = foe
	if not hit:hit = storage.foe_max_hit
	storage.foe_hit = hit


def boss_check():
	"""Will check and if needed, set the boss"""
	if random.randint(0,2) and storage.boss_list:
		boss = random.choice(storage.boss_list)
		storage.boss = boss
		desc, hp, hit, storage.extra_lives, storage.extra_xp = boss()
		make_foe(hp=hp, foe=desc, hit=hit)
		storage.screen = "precombat"
		return random.choice(messages.see_boss_messages) + "\npress return to begin the fight!"
	return False

def hit_check():
	"""Will check if the player or foe hit"""
	hit = random.randint(1,100)
	if hit <= chance_to_hit:
		return True

def death_check(foe_deaths=messages.foe_deaths, player_deaths=messages.player_deaths):
	"""Checks if anyone has died. if so, it returns a message and if not, it returns a blank string"""
	text = ""
	if storage.foe_hp <= 0:
		if storage.foe_death_message:
			text += storage.foe_death_message
		else:
			text += random.choice(foe_deaths)
		if storage.boss:
			storage.boss_list.remove(storage.boss)
			storage.boss = None
		storage.current_foe = None
		storage.screen = "back_to_drift"
		if storage.extra_xp or storage.extra_lives:
			storage.player_xp += storage.extra_xp
			storage.player_lives += storage.extra_lives
			text += "You gained %s extra xp and %s more lives" % (storage.extra_xp, storage.extra_lives)
			storage.extra_xp, storage.extra_lives = [0, 0]
	elif storage.player_hp <= 0:
		text += random.choice(player_deaths)
		storage.player_lives -= 1
		if storage.player_lives < 0:
			storage.scene = dead
			storage.screen = "dead"
		else:
			storage.player_hp = storage.player_max_hp
			text += "\nA magic piemaker gives you back a new shell and you zoom back to attack the evil %s" % storage.current_foe[0]
	return text

def dead():
	"""Will give the player a choice of quitting or restarting"""
	spk("You have run out of all your lives. What do you wish to do? Press return to start over or press escape to leave..", 2)

def foe_combat():
	"""Will be the turn for the foe"""
	if hit_check():
		h = random.randint(1,storage.foe_hit)
		storage.player_hp -= h
		return random.choice(messages.foe_attacks) % h
	else:
		return random.choice(messages.foe_misses)

def player_combat(key):
	"""Will run the player's combat"""
	if key == "space":
		if hit_check():
			charge_deathray()
			h = random.randint(1,storage.player_hit)
			storage.foe_hp -= h
			return (h, random.choice(messages.player_attacks) % h)
		else:
			charge_deathray()
			return (0, random.choice(messages.player_misses))
	elif "ctrl" in key:
		if storage.player_deathray_charge != 100:
			spk("Your deathray has not charged, it is at %s percent" % storage.player_deathray_charge, 0)
			return (None, None)
		charge_deathray()
		if hit_check():
			storage.player_deathray_charge = 0
			h = int(storage.player_deathray_hit * storage.foe_hp)
			storage.foe_hp -= h
			return (h, random.choice(messages.deathray_hits) % h + "\n.")
		else:
			return (0, random.choice(messages.deathray_misses))

def combat(key):
	"""Runs the player and the foe's turn and does the death check. It also builds the messages that are spoken"""
	player_hit, text = player_combat(key)
	if text:
		text += "\n"
		d = death_check()
		if not d:
			text += foe_combat()
			d = death_check()
		text += d
		text += level(player_hit)
		spk(text, 2)

def level(hit):
	"""Will give xp as well as level if needed"""
	storage.player_xp += hit*xp_per_hit
	if storage.player_xp >= storage.player_next_level:
		storage.screen = "leveled"
		storage.player_next_level *= xp_multiplyer_tnl
		storage.player_level += 1
		storage.player_max_hp += int(storage.player_max_hp * 0.1)
		storage.player_hp = storage.player_max_hp
		storage.player_deathray_hit += 0.05
		storage.player_hit += int(storage.player_hit*hit_gain)
		storage.foe_max_hit += int(storage.foe_max_hit*hit_gain)
		return "\nYou leveled! You're now level %s! Press return to go back to combat" % storage.player_level
	return ""

