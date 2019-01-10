#todo: fix the on_add_to_grid function. Also figure out what is going on between Grid and AdvancedGrid.
#For making a grid
#a Wall or wall consists of the length of the x Wall and the length of the y Wall.
#MyGrid.add_wall(0,10, 10,10)
#the first two numbers are saying that our x Wall is from 0 to 10 on the grid. that means we have a Wall that is 10 squares long.
#the second two numbers say that we wish our y Wall to go up from 10 to 10. This means that it is just 1 square wide.
import math
from pyaudiogame.utils.array_math import magnitude, vector, dotProduct, sumArray

# imports for the AdvancedGrid class
from pyaudiogame import event_queue
from pyaudiogame import KeyMap
from pyaudiogame.mixer import SoundIterator, set_listener

class Grid(object):
	"""Call this class with the width and height, then check(x, y) to see if there is something where that x,y point is."""

	def __init__(self, width=50, height=50):
		self.width = width
		self.height = height

		#object list
		self.objects = []

		self.add_wall(0, width, 0, 0)
		self.add_wall(0, width, height, height)
		self.add_wall(0, 0, 0, height)
		self.add_wall(width, width, 0, height)

	def check(self, x, y):
		"""Checks to see if the passed point is in any of the specified polys"""
		for p in self.objects:
			on_move_event = self.get_move_event(x, y, p)
			p.on_move(on_move_event)
			if on_move_event  .in_poly:
				return p.callback()

	def check_rect(self, x, y):
		"""Checks if a point is in a rect"""
		for o in self.objects:
			if x >= o.min_x and x <= o.max_x and y >= o.min_y and y <= o.max_y:
				if o.callback:
					return o.callback()
				return True

	def get_move_event(self, x, y, p):
		"""x and y are the pos of the player. p is an object with a .poly attribute."""
		in_poly = self.point_in_polygon(x, y, p.poly)
		on_move_event = OnMoveEvent((x,y), in_poly, *self.distance_and_direction_to_polygon((x,y), p.poly))
		return on_move_event  

	def point_in_polygon(self, x, y, poly):
		"""Generic point in polygon function, polygon must be a set of x y tuples in a clockwise or counterclockwise order."""
		n = len(poly)
		inside = False
		try:
			p1x, p1y = poly[0]
		except IndexError:
			return None
		for i in range(n+1):
			p2x, p2y = poly[i % n]
			if len(poly) == 2 and x >= min(p1x,p2x) and x <= max(p1x,p2x) and y >= min(p1y,p2y) and y <= max(p1y,p2y): # it is a single line
				return True
			if x == p2x and y == p2y: #it is on a point
				return True
			if y > min(p1y, p2y):
				if y <= max(p1y,p2y):
					if x < max(p1x, p2x):
						if p1y != p2y:
							xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
						if p1x == p2x or x <= xinters:
#							print("ran: ", ([p1x, p1y], [p2x, p2y]))
							inside = not inside
			p1x, p1y = p2x, p2y
		return inside

	def distance_and_direction_to_polygon(self, point, poly):
		"""gets the distance and direction in angles to the polygon"""
		if self.point_in_polygon(*point, poly):
			return [0, 0, tuple(point)]
		minDist = 10000000000
		minAngle = 0
		finalNearestPoint = poly[0]
		p1 = poly[0]
		for i in range(1, len(poly)+1):
			p2 = poly[i % len(poly)]
			distance = 0
			lineVec = vector(p2, p1)
			perpVec = [lineVec[1], lineVec[0]*-1]
			dot = dotProduct(perpVec, vector(point, p1))
			distPointToLine = dot / magnitude(perpVec)
			perpVecMagnitude = magnitude(perpVec)
			normalizedPerpVec = [p/perpVecMagnitude for p in perpVec]
			dotSignedPerpVec = [p * -1 for p in normalizedPerpVec]
			intersectionPoint = sumArray([p*distPointToLine for p in dotSignedPerpVec], point)
			# get the distance between each of the points
			p1_intersectionPoint_dist = magnitude(vector(p1, intersectionPoint))
			p2_intersectionPoint_dist = magnitude(vector(p2, intersectionPoint))
			p1_p2_dist = magnitude(vector(p1, p2))
			# check if the intersectionPoint is on the p1_p2 line
			online = p1_intersectionPoint_dist + p2_intersectionPoint_dist == p1_p2_dist
			nearestPoint = intersectionPoint
			if not online:
				nearestPoint = p1 if p1_intersectionPoint_dist > p2_intersectionPoint_dist else p2
			point_to_nearest_point = vector(nearestPoint, point)
			distance = magnitude(point_to_nearest_point)
			# get the angle the point is to the line
			vecRight = [1,0]
			radAngle = math.atan2((point_to_nearest_point[0]*vecRight[1]) - (point_to_nearest_point[1]*vecRight[0]), (point_to_nearest_point[0] * vecRight[0]) + (point_to_nearest_point[1]*vecRight[1]))
			degree = radAngle * (180/math.pi)
			minDist = min(distance, minDist)
			minAngle = degree if minDist == distance else minAngle
			finalNearestPoint = nearestPoint if minDist == distance else  finalNearestPoint
			p1 = p2
		return [minDist, minAngle*-1, tuple(finalNearestPoint)]

	def add_wall(self, min_x, max_x, min_y, max_y, callback=lambda:True, on_move=lambda e:True, sound=None):
		"""Adds a Wall object to the object list"""
		new_wall = Wall(min_x, max_x, min_y, max_y, callback, on_move, sound)
		self.objects.append(new_wall)
		return new_wall

	def add_polygon(self, poly, callback=lambda:True, on_move=lambda e:True, sound=None):
		"""Creates a Polygon and adds it to the objects list"""
		if type(poly) == list or type(poly) == tuple:
			p = Polygon(poly, callback, on_move, sound)
		else:
			p = poly
		self.objects.append(p)
		return p

class OnMoveEvent(object):
	def __init__(self, current_pos, in_poly, distance, angle, nearest_point):
		self.current_pos = current_pos
		self.in_poly = in_poly
		self.distance = distance
		self.angle = angle
		self.nearest_point = nearest_point


class Polygon(object):
	def __init__(self, poly, callback=lambda:True, on_move=lambda e:True, sound=None):
		self.poly = poly
		self.callback = callback
		self._on_move = on_move
		self.sound = sound
		self.grid = None

	def on_add_to_grid(self, grid):
		"""Runs when an object is added to a grid."""
		self.grid = grid
		event = grid.get_move_event(*grid.pos, self)
		if self.sound:
			self.sound.set_pos(*event.nearest_point)

	def on_move(self, event):
		if self.sound:
			self.sound.set_pos(*event.nearest_point)
		self._on_move(event)

	def __repr__(self):
		return self.poly

class Wall(Polygon):
	"""This just has the properties for basic Wall (rect) objects"""
	def __init__(self, min_x, max_x, min_y, max_y, callback=lambda:True, on_move=lambda e:True, sound=None):
		self.min_x = min_x
		self.max_x = max_x
		self.min_y = min_y
		self.max_y = max_y
		self.poly = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]
		self.callback = callback
		self._on_move = on_move
		poly_set = list(set(self.poly))
		if len(poly_set) == 2:
			self.poly = poly_set
		self.sound = sound
		self.grid = None

	def __repr__(self):
		"""Call this class to see the below returned"""
		return "WallObject:x(%d, %d)y(%d, %d)" % (self.min_x, self.max_x, self.min_y, self.max_y)

class AdvancedGrid(Grid):
	"""This is an advanced grid that will take cair of location, handling input, and playing sounds."""
	def __init__(self, width=50, height=50, step_sounds=[], hit_sounds=[], speed=1, grid=None, starting_pos=(1,1), delay=0.3, start_with_step=True, on_step=None, on_hit=None, move_listener=True, keymap=[{'key':'up', 'event':'up'},{'key':'down', 'event':'down'},{'key':'left','event':'left'},{'key':'right','event':'right'}]):
		"""arguments:
			width and height are the dimensions of the grid in an int. They both default to 50.
			speed is the amount of tiles the pos moves each check in a float
			starting_pos is the starting position of the player in a tuple.
			step_sounds are sounds that play each time the player moves. Either a list of file names can be passed in, or a SoundIterator can be passed in.
			hit_sounds are sound that play each time the player hits an impassable obstical. Either a list of file names can be passed in, or a SoundIterator can be passed in.
			keymap is a list of default keyboard mappings that will be used in the grid's local keymap. These can be modified or changed by using the keymap object at self.keymap.
			grid is a Grid object. If not passed in, then it will default to creating a new Grid object with the width and height.
			self.delay is the amount of time inbetween each step.
			start_with_step is a bool that is by default True. It means that the user will always step as soon as they press a movement key. If it is False, then there will be a loop that runs every delay and if the running variable is true, then the user will take a step. otherwise, nothing will happen. This prevents users from spamming movement keys, but is not very good for testing.
			on_hit is a callback function that runs when the user hits an object. It is passed self.
			on_step is a callback that runs when the user takes a step. It is passed self.
			move_listener is a boolian that is True by default. If true, the listener object in pyaudiogame.mixer is moved along with the point.
		"""

		self.height = height
		self.width = width
		self.speed = speed
		self.pos = starting_pos
		self.step_sounds = step_sounds if type(step_sounds) != list else SoundIterator(*step_sounds)
		self.hit_sounds = hit_sounds if type(hit_sounds) != list else SoundIterator(*hit_sounds)
		self.keymap = KeyMap(keymap)
		self.grid = grid if grid else Grid(width, height)
		self.delay = delay
		self.start_with_step = start_with_step
		self.on_hit = on_hit if on_hit else lambda s: True
		self.on_step = on_step if on_step else lambda s: True
		self.move_listener = move_listener

		# operation variables
		self.moving = False
		self._id = "AdvancedGrid%s" % id(self)
		self._current_event = None
		if not start_with_step:
			event_queue.schedule(function=self._move_callback, name=self._id, delay=self.delay, repeats=-1, before_delay=False)

	def move(self, event):
		"""This will start the player moving if they are not moving and stop the player if they are moving. Each step will be a self.delay apart."""
		state = self.keymap.getEvent(event.key, event.mods, state=1)
		if self.moving and state and event.state == 0:
			self.moving = False
			if self.start_with_step:
				event_queue.unschedule(self._id)
		elif state:
			self._current_event = event
			self.moving = True
			if self.start_with_step:
				event_queue.schedule(function=self._move_callback, name=self._id, delay=self.delay, repeats=-1, before_delay=True)

	def _move_callback(self):
		if self.moving:
			self.move_once(self._current_event)

	def set_pos(self, x, y, play_hit_sounds=False, play_step_sounds=False):
		"""Sets the player in the given pos"""
		if not self.grid.check(x, y):
			self.pos = (x, y)
			if play_step_sounds: self.step_sounds.play()
			self.on_step(self)
			if self.move_listener:
				set_listener(x, y, 90)
			return False
		else:
			if play_hit_sounds: self.hit_sounds.play()
			self.on_hit(self)
			return True

	def move_once(self, event):
		"""Pass the event object in from an EventHandler that has events from the global_keymap and this will move the player once."""
		state = self.keymap.getEvent(key=event.key, mods=event.mods, state=event.state)
		if state:
			x, y = self.pos
			if state == "up":
				y += self.speed
			elif state == "down":
				y -= self.speed
			elif state == "right":
				x += self.speed
			elif state == "left":
				x -= self.speed
			if not self.grid.check(x, y):
				self.pos = (x, y)
				self.step_sounds.play()
				self.on_step(self)
				if self.move_listener:
					set_listener(x, y, 90)
				return False
			else:
				self.hit_sounds.play()
				self.on_hit(self)
				return True

	def add_wall(self, min_x, max_x, min_y, max_y, callback=lambda:True, on_move=lambda e:True, sound=None):
		"""Adds a Wall object to the object list in the grid"""
		p = self.grid.add_wall(min_x, max_x, min_y, max_y, callback, on_move, sound)
		p.on_add_to_grid(self)
		return p

	def add_polygon(self, poly, callback=lambda:True, on_move=lambda e:True, sound=None):
		"""Creates a Polygon and adds it to the objects list"""
		p = self.grid.add_polygon(poly, callback, on_move, sound)
		p.on_add_to_grid(self)
		return p


if __name__ == '__main__':
	my_grid = Grid(50, 50)
	o = my_grid.objects[3]
	x, y = (50, 1)
	print(o.poly)
	print(x >= o.min_x and x <= o.max_x and y >= o.min_y and y <= o.max_y)
	print(my_grid.point_in_polygon(x, y, o.poly))
	print(my_grid.point_in_polygon(x, y, [[50, 0], [50, 50]]))