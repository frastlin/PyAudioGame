#This module deals with sound and music playback
from random import choice
from pygame.mixer import *
from pygame.mixer import Sound as Mixer_sound
pre_init(44100,-16, 2, 2048)
init()
set_num_channels(50)

# event queue for scheduling end events
from pyaudiogame import event_queue

# Position is to controll the 3D audio
from pyaudiogame import position

# this is a list of currently playing sounds so that when the listener moves, the listener can be updated on any looping sound
playing_sounds = []

# The listener is set facing north at 90 degrees. east is 0 degrees and the positions move counterclockwise.
position.set_listener(0,0,90)

def get_listener():
	return position.get_listener()

def set_listener(x,y,o):
	"""Sets pos of the listener. east is o=0 and north is o=90"""
	position.set_listener(x,y,o)
	[sound.set_volume() for sound in playing_sounds]

class Sound(object):
	"""
		todo is to wrap all the channel methods so they only work on the sound. This could happen either by checking if the sound is playing on the channel or possibly by calling methods on the sound itself.
		mixer documentation:
		https://www.pygame.org/docs/ref/mixer.html

		This class ads support for 3D positioning. Just pass the position of the sound in a tuple of (x,y) coordinates after the path of the file.
	"""

	def __init__(self, filename, position=None, single_channel=True):
		self.name = filename
		self.pos = position # should be a tuple (x, y)
		self.channel = None
		self.paused = False
		self.playing = False
		self.stopped = False # this is to tell a callback if the sound was stopped by a stop function or not.
		self.single_channel = single_channel
		self.callback = lambda e: None # the callback is passed this object as an argument and is triggered at the end of the sound
		self._id = "sound-%s-%s" % (self.name, id(self))

		try:
			self.sound = Mixer_sound(filename)
		except:
			raise Exception("Unable to open file %r" % filename)


	def play(self, loops=0, maxtime=0, fade_ms=0):
		self.playing = True
		self.stopped = False
		if not self.channel or ((not self.single_channel or self.channel.get_sound() != self.sound) and self.channel.get_busy()):
			self.channel = find_channel() or self.channel
		self.channel.play(self.sound, loops, maxtime, fade_ms)
		if self.pos:
			playing_sounds.append(self)
			self.set_volume()
		event_queue.schedule(function=self.check_if_finished, repeats=-1, delay=0, name=self._id) # this uses the channel.get_busy to figure out if the sound has finished playing.
#		event_queue.schedule(function=self.finish, repeats=1, delay=self.get_length()-0.09, name=self._id) # This does the same as above, but uses the length of the sound to schedule an end event. The problem with this is that if one pauses the sound, the event still runs. The pro is that the end event can be faster than the actual sound.

	def get_volume(self):
		return self.channel.get_volume()

	def move_pos(self, x=0, y=0):
		cx, cy = self.pos
		self.set_pos(cx+x, cy+y)
		return self.pos

	def set_pos(self, x, y):
		self.pos = (float(x), float(y))
		if(self.channel):
			self.channel.set_volume(*position.stereo(*self.pos))

	def get_pos(self):
		return self.pos

	def get_length(self):
		return self.sound.get_length()

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
		"""This stops the channel from playing."""
		event_queue.unschedule(self._id)
		if self in playing_sounds:
			playing_sounds.remove(self)
		self.playing = False
		self.paused = False
		self.stopped = True
		self.unpause()
		if self.channel:
			self.channel.stop()
		self.finish()

	def stop_sound(self):
		"""This stops the sound object from playing rather than the channel"""
		self.sound.stop()
		self.unpaws()
		self.playing = False
		mixer_queue.remove(self.channel)
		if self in playing_sounds:
			playing_sounds.remove(self)

	def get_busy(self):
		"""Returns if the channel is active. This is used for triggering the callback"""
		if self.channel:
			return self.channel.get_busy()
		return False

	def check_if_finished(self):
		"""This runs every tick to see if the channel is done. if it is done, then it runs the finish method and removes itself from the event_queue."""
		if not self.get_busy():
			self.finish()
			event_queue.unschedule(self._id)

	def toggle_playing(self):
		if self.playing:
			self.stop()
		else:
			self.play()

	def set_volume(self, volume=1, right=None):
		"""Sets the volume if there is a channel. If there is a position, then volume is adjusted to be that position. If no arguments are passed, then it will update the volume to be the current pos, or set volume back to 1."""
		if not  self.channel:
			return 0
		if volume > 1:
			volume = 1
		elif volume <= 0:
			self.channel.set_volume(0)
			return 0
		if not self.pos and not right:
			self.channel.set_volume(volume)
		elif right:
			self.channel.set_volume(volume, right)
		else:
			x, y = self.pos
			if x == 0 and y == 0:
				self.channel.set_volume(volume)
				return 0
			self.channel.set_volume(*position.stereo(x/volume, y/volume))

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

class SoundIterator(object):
	def __init__(self, *args, random=False, random_repeat=True):
		"""Pass in sound files, or SoundIterator objects (anything with a play method and an on_end event (if the play_loop functionality is desired)), and if random is false, then they will be played in order. Otherwise they will be played randomly. Sound objects can be passed in as well, but their callback functionality will be replaced. It is better to pass in strings."""
		self.sounds = []
		self.random = random
		self.random_repeat = random_repeat
		self.index = 0
		self.event_name = "%sEndSoundEvent" % id(self)
		self.playing = False
		for s in args:
			if type(s) == str:
				s = Sound(s)
			self.sounds.append(s)

	def play(self, looping=False):
		"""Plays sounds"""
		self.playing = True
		if looping:
			self._play_looping()
		else:
			self._play_single()

	def toggle_looping(self, current_sound=True):
		if self.playing:
			self.stop(current_sound)
		else:
			self.play(looping=True)

	def _play_looping(self, e=None):
		"""plays the sounds until stop is called. makes this function the callback of the sound. If this sound is called, it should not have a callback as it overwrites the callback"""
		if self.playing:
			s = self.sounds[self.index]
			s.callback = self._play_looping
			self._play_single()

	def stop(self, current_sound=True):
		"""Stops all sounds. If current_sound is False, then the current sound will finish, and no more sounds will play."""
		self.playing = False
		if current_sound:
			[s.stop() for s in self.sounds]

	def _play_single(self):
		"""Will play either the next sound, or a random sound. If there are no sounds, it plays no sounds."""
		if not self.sounds:
			return False
		self.sounds[self.index].play()
		if self.random:
			if self.random_repeat:
				self.index = choice(list(range(len(self.sounds))))
			else:
				r = list(range(self.index)) + list(range(self.index + 1, len(self.sounds)))
				self.index = choice(r)
		else:
			self.index += 1
			if self.index == len(self.sounds):
				self.index = 0

	@property
	def callback(self):
		"""Just needed as a getter for the property, not needed for the code"""
		pass

	@callback.setter
	def callback(self, cb):
		"""Sets all the sound objects to have the passed callback (cb)"""
		for s in self.sounds:
			s.callback = cb
