#Player template

class Player(object):
	"""There are some basic functions and variables that a player may need"""
	def __init__(self, name="Fred", location=(1, 1)):
		self.name = name
		self.location = location

		#settings
		self.map = None

	def move(self, actions, map=None):
		"""call this to move the player"""
		if not map:
			map = self.map
		x = self.location[0]
		y = self.location[1]
		key = actions['key']
		if key == "up":
			y += 1
		elif key == "down":
			y -= 1
		elif key == "right":
			x += 1
		elif key == "left":
			x -= 1
		if not map.check(x, y):
			self.location = (x, y)
			return False
		return True

