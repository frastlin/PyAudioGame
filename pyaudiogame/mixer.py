#This module deals with sound and music playback
from pygame.mixer import *
from pygame.mixer import Sound as Mixer_sound
pre_init(44100,-16, 2, 2048)
init()
set_num_channels(50)

# the queue for moving events
from pyaudiogame.app import mixer_queue

# Position is to controll the 3D audio
from pyaudiogame import position

# The listener is set facing north at 90 degrees. east is 0 degrees and the positions move counterclockwise.
position.set_listener(0,0,90)

def get_listener():
	return position.get_listener()

def set_listener(x,y,o):
	position.set_listener(x,y,o)

class Sound(object):
	"""
		todo is to wrap all the channel methods so they only work on the sound. This could happen either by checking if the sound is playing on the channel or possibly by calling methods on the sound itself.
		mixer documentation:
		https://www.pygame.org/docs/ref/mixer.html

		This class ads support for 3D positioning. Just pass the position of the sound in a tuple of (x,y) coordinates after the path of the file.
	"""

	def __init__(self, filename, position=(0.0, 0.0), single_channel=True):
		self.name = filename
		self.sound = Mixer_sound(filename)
		self.pos = position
		self.channel = None
		self.paused = False
		self.playing = False
		self.single_channel = single_channel
		self.callback = lambda e: None

	def play(self, loops=0, maxtime=0, fade_ms=0):
		self.playing = True
		if not self.channel or ((not self.single_channel or self.channel.get_sound() != self.sound) and self.channel.get_busy()):
			self.channel = find_channel() or self.channel
		self.channel.set_volume(*position.stereo(*self.pos))
		self.channel.play(self.sound, loops, maxtime, fade_ms)
# (figure out what the mixer_queue was in the old script)
#		mixer_queue.add(self.channel, self)

	def get_event(self):
		return self.channel.get_endevent()

	def get_volume(self):
		return self.channel.get_volume()

	def move_pos(self, x=0, y=0):
		cx, cy = self.pos
		self.set_pos(cx+x, cy+y)
		return self.pos

	def set_pos(self, x, y):
		self.pos = (float(x), float(y))
		if(self.channel):
			self.channel.set_volume(*stereo(*self.pos))

	def get_pos(self):
		return self.pos

	def toggle_pause(self):
		"""This function can be called to pause and unpause a sound without the script needing to handle the check for paused and unpaused. If the sound is paused when this function is called, then the sound is unpaused and if the sound is playing when this function is called, then the sound is paused. It's very good for buttons to play and pause sounds."""
		if not self.channel or not self.playing:
			self.play()
		elif self.paused:
			self.unpause()
		else:
			self.pause()

	def unpause(self):
		if not self.channel: return False
		self.channel.unpause()
		self.paused = False

	def is_paused(self):
		return self.paused

	def pause(self):
		if not self.channel: return False
		self.channel.pause()
		self.paused = True

	def stop(self):
		self.playing = False
		self.unpause()
		self.channel.stop()
		mixer_queue.remove(self.channel)
		self.finish()

	def stop_sound(self):
		self.sound.stop()
		self.unpaws()
		self.playing = False
		mixer_queue.remove(self.channel)

	def toggle_playing(self):
		if self.playing:
			self.stop()
		else:
			self.play()

	def set_volume(self, volume):
		if self.channel:
			x, y = self.pos
			if volume > 1:
				volume = 1
			elif volume <= 0:
				self.channel.set_volume(0)
				return 0
			elif x == 0 and y == 0:
				self.channel.set_volume(volume)
				return 0
			self.channel.set_volume(*stereo(x/volume, y/volume))

	def finish(self):
		self.playing = False
		self.paused = False
		self.callback(self)

mixer_paused = False
def mixer_toggle_pause(excluded_channels=[]):
	global mixer_paused
	if mixer_paused:
		unpause()
		[c.pause() for c in excluded_channels if c.is_paused()]
		mixer_paused = False
	else:
		pause()
		mixer_paused = True
		[c.unpause() for c in excluded_channels if not c.is_paused()]
