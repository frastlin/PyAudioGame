"""
The same mixer deals with sound (loaded before playing) and music (loaded while playing).
In Python, a module is actually imported the first time only. The next times the module is only linked.
The module should import pygame and eventually initialize it in the beginning of the module, or in a function called once. The main initialization can happen in the beginning of the main module. On the other hand the pygame.init() function can be called several times during the initialization phase without a problem. Just make sure that pre_init is called before any pygame.init() or the parameter will be ignored.
Turning the module into a reusable one is not that easy. I have tried to make a components-based framework engine in 2013 but I'm not sure if it would be good enough. A simpler module mimicking pySonic API might be better. It would manage the sound sources and move them when the listener is moving.
The stereo() function already deals with sounds behind the listener: the volume is divided by 2.
Here is a documented usable module from the engine framework, called pos.py, which essentially contains the formulas:

#start module
This module can be combined with pygame mixer to have a portable
positional audio system. The formulae are purely empiric. They have
been taken from SoundMUD and SoundRTS.

example:
import pos

pos.set_listener(10, 10, 90)
print pos.stereo(20, 10)
"""

import math


_x, _y, _o = 0, 0, 0

def set_listener(x, y, o):
	"""sets the position of the listener:

	- x, y: coordinates of the listener
	- o: orientation in degrees, east is 0 degrees, counterclockwise
	"""
	global _x, _y, _o
	_x, _y, _o = x, y, o

def _distance(x, y):
	"""distance of x, y from the listener"""
	dx = x - _x
	dy = y - _y
	return math.sqrt(dx * dx + dy * dy)

def _angle(x, y):
	"""angle of x, y observed from the listener"""
	d = _distance(x, y)
	if d == 0:
		return 0 # object too close => in front of the listener
	ac = math.acos((x - _x) / d)
	if y - _y > 0:
		a = ac
	else:
		a = -ac
	return a - math.radians(_o)

def stereo(x, y, nodist=False, above=False):
	"""returns the left and right volumes

	- x, y: coordinates of the object
	- nodist: distance = 1 (for signaling object direction)
	- above: from above
	"""
	# TODO: above
	a = _angle(x, y)
	d = _distance(x, y)
	left = (math.sin(a) + 1) / 2.0
	right = 1 - left
	left = math.sin(left * math.pi / 2.0)
	right = math.sin(right * math.pi / 2.0)
	if math.cos(a) < 0: # behind
		if nodist:
			k = 1.3
		else:
			k = 2.0  # TODO: attenuate less? (especially in overhead view)
		left /= k
		right /= k
	if d < 1 or nodist:
		d = 1
	left = min(left / d, 1)
	right = min(right / d, 1)
	return left, right

def get_listener():
	"""returns the current position of the listener"""
	return (_x, _y, _o)

if __name__ == "__main__":
	assert stereo(0, 0)
	assert set_listener(10,10,90) == None
	assert get_listener() == (10, 10, 90)
