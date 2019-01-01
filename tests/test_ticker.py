# Everything is run off pygame ticks here, so 1000 is one second
from pyaudiogame.ticker import Scheduler
event_queue = Scheduler(time_format=0.001)

def tick_seconds(seconds):
	"""Ticks the specified number of seconds"""
	fps = 30
	number_of_frames = int((seconds*1000)/fps)
	for i in range(number_of_frames):
		event_queue.tick(0.03)

