"""
This Scheduler is quite easy. There are only two calls you need to know about, tick and schedule.
Here is an example:

import time
#Our little framerate (better to use something a little more advanced, but this works just fine.
fps = 0.03

def hello(name):
	#Just a random little function that prints 'hello name'
	print("hello %s" % name)

#There is one argument that goes in Scheduler, it is the amount you wished each time to be multiplied by. Pygame for example, ticks in incraments of 1000 each second where as time.sleep is in incraments of 1 for 1 second.
#Default is 1.0, for pygame it would be 0.001.

c = Scheduler()
c.schedule(function=hello, delay=1, repeats=2, before_delay=True, name="Fred")

while c.events:
	c.tick(fps)
	time.sleep(fps)
"""

class Scheduler:
	"""Call tick to run a tick and schedular to add an event to a queue"""

	def __init__(self, time_format=1):
		self.events = set()
		self.new_events = set()
		self.time_format = time_format


	def tick(self, elapsed_time):
		"""Call this each iteration of the game loop with an argument of the amount of time that has elapsed in seconds"""
		done_events = []
		for event in self.events:
			if event.should_run():
				event.run()
			if event.done:
				done_events.append(event)
			event.tick(elapsed_time*self.time_format)
		self.events = self.events | self.new_events
		self.new_events = set()
		[self.events.remove(e) for e in done_events]

	def schedule(self, function, delay=0, repeats=1, before_delay=False, name=None, *args, **kwargs):
		"""function is the name of the callback function that will run with the given arguments, delay is the amount of time to wait (0 for every tick), repeats is the amount of times the event will run (0 or less) for infinent, before_delay says that the function run before the delay, name is the title of the event, and the wrest are arguments for the function"""
		e = EventMaker(function, delay, repeats, before_delay, name, *args, **kwargs)
		self.new_events.add(e)

	def unschedule(self, event_name):
		"""Call this with the event name as a string to remove it from the queue"""
		events = self.events | self.new_events
		for i in events:
			if i.name == event_name:
				i.done = True

class EventMaker:
	"""This class is the event. It has all the functions to run the event."""
	def __init__(self, function, delay, repeats, before_delay, name, *args, **kwargs):
		"""function is the name of the callback function that will run with the given arguments, delay is the amount of time to wait (0 for every tick), repeats is the amount of times the event will run (0 or less) for infinent, before_delay says that the function run before the delay, name is the title of the event, and the wrest are arguments for the function"""
		self.function = function
		self.delay = delay
		self.repeats = repeats
		self.before_delay = before_delay
		self.name = name
		self.args = args
		self.kwargs = kwargs

		#Our operation variables:
		self.elapsed_time = 0
		self.done = False

	def tick(self, elapsed_time):
		"""adds time to the elapsed_time"""
		self.elapsed_time += elapsed_time

	def should_run(self):
		"""Checks if the event should run"""
		if self.before_delay and not self.elapsed_time and self.repeats:
			self.repeats += 1
			return True
		elif self.elapsed_time >= self.delay:
			return True

	def run(self):
		"""Runs the event"""
		self.repeats -= 1
		if self.repeats or not self.before_delay:
			self.function(*self.args, **self.kwargs)
		if self.repeats == 0:
			self.done = True
		self.elapsed_time = 0


if __name__ == '__main__':
	def hello(name):
		print("hello %s" % name)

	c = Scheduler(0.001)
	c.schedule(hello, 1, 2, True, name="Fred")

	import pygame
	pygame.init()
	fps = 30
	fpsClock = pygame.time.Clock()

	while c.events:
		c.tick(fpsClock.tick(fps))