#For making a grid
#a Wall or wall consists of the length of the x Wall and the length of the y Wall.
#MyGrid.add_wall(0,10, 10,10)
#the first two numbers are saying that our x Wall is from 0 to 10 on the grid. that means we have a Wall that is 10 squares long.
#the second two numbers say that we wish our y Wall to go up from 10 to 10. This means that it is just 1 square wide.

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
		"""Call this to see if there is an object"""
		for o in self.objects:
			if x >= o.min_x and x <= o.max_x and y >= o.min_y and y <= o.max_y:
				return True

	def add_wall(self, min_x=1, max_x=10, min_y=5, max_y=5):
		"""Adds a Wall object to the object list"""
		new_wall = Wall(min_x, max_x, min_y, max_y)
		self.objects.append(new_wall)
		return new_wall


class Wall(object):
	"""This just has the properties for basic Wall objects"""
	def __init__(self, min_x, max_x, min_y, max_y):
		self.min_x = min_x
		self.max_x = max_x
		self.min_y = min_y
		self.max_y = max_y

	def __repr__(self):
		"""Call this class to see the below returned"""
		return "WallObject:x(%d, %d)y(%d, %d)" % (self.min_x, self.max_x, self.min_y, self.max_y)

