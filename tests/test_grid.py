#Tests the ui.grid module
from pyaudiogame.ui import grid
my_grid = grid.Grid(50, 50)

def test_wall():
	dumb_wall = grid.Wall(1,10, 0,1)
	assert dumb_wall.max_y == 1
	assert dumb_wall.min_x == 1

def test_sides():
	assert my_grid.check(50, 1) == True
	assert my_grid.check(5,50) == True
	assert my_grid.check(5,5) == None
	#This is because the sides of the whole thing are just 1 square wide.
	assert my_grid.check(51,1) == None

def test_adding_areas():
	my_grid.add_wall(4,6, 3,3)
	my_grid.add_wall(4,6, 6,6)
	my_grid.add_wall(4,4, 3,6)
	my_grid.add_wall(6,6, 3,4)
	#check inside the box
	my_grid.check(5,5) == None
	#test the wall
	assert my_grid.check(5,6) == True
	#test the door
	assert my_grid.check(6,5) == None

def test_zones_tiles_without_substance():
	"""Test that you can make walls that you can walk through"""
	global passed
	passed = False
	def ran(p=None):
		global passed
		passed = True
		return p
	my_grid.add_wall(7,9, 2,5, ran)
	my_grid.add_wall(20,25, 2,5, ran, True)
	assert my_grid.check(7,3) == None
	assert passed == True
	passed = False
	assert my_grid.check(22,4) == True
	assert passed == True
