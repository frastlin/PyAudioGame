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
		"""Checks to see if the passed point is in any of the specified polys"""
		point_in_polygon = self.point_in_polygon
		for p in self.objects:
			if point_in_polygon(x, y, p.poly):
				if p.callback:
					return p.callback()
				return True

	def check_rect(self, x, y):
		"""Checks if a point is in a rect"""
		for o in self.objects:
			if x >= o.min_x and x <= o.max_x and y >= o.min_y and y <= o.max_y:
				if o.callback:
					return o.callback()
				return True

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
							print("ran: ", ([p1x, p1y], [p2x, p2y]))
							inside = not inside
			p1x, p1y = p2x, p2y
		return inside

	def add_wall(self, min_x, max_x, min_y, max_y, callback=None):
		"""Adds a Wall object to the object list"""
		new_wall = Wall(min_x, max_x, min_y, max_y, callback)
		self.objects.append(new_wall)
		return new_wall

	def add_polygon(self, poly, callback=None):
		"""Creates a Polygon and adds it to the objects list"""
		p = Polygon(poly, callback)
		self.objects.append(p)
		return p

class Wall(object):
	"""This just has the properties for basic Wall objects"""
	def __init__(self, min_x, max_x, min_y, max_y, callback=None):
		self.min_x = min_x
		self.max_x = max_x
		self.min_y = min_y
		self.max_y = max_y
		self.poly = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]
		self.callback = callback
		poly_set = list(set(self.poly))
		if len(poly_set) == 2:
			self.poly = poly_set

	def __repr__(self):
		"""Call this class to see the below returned"""
		return "WallObject:x(%d, %d)y(%d, %d)" % (self.min_x, self.max_x, self.min_y, self.max_y)

class Polygon(object):
	def __init__(self, poly, callback=None):
		self.poly = poly
		self.callback = None

	def __repr__(self):
		return self.poly

if __name__ == '__main__':
	my_grid = Grid(50, 50)
	o = my_grid.objects[3]
	x, y = (50, 1)
	print(o.poly)
	print(x >= o.min_x and x <= o.max_x and y >= o.min_y and y <= o.max_y)
	print(my_grid.point_in_polygon(x, y, o.poly))
	print(my_grid.point_in_polygon(x, y, [[50, 0], [50, 50]]))