#Tests the ui.grid module
import unittest
from pyaudiogame.ui import grid
my_grid = grid.Grid(50, 50)

class TestGrid(unittest.TestCase):
	def test_wall(self):
		dumb_wall = grid.Wall(1,10, 0,1)
		self.assertEqual(dumb_wall.max_y, 1)
		self.assertEqual(dumb_wall.min_x, 1)
		self.assertEqual(dumb_wall.poly, [[1,0], [1,1], [10, 1], [10, 0]])

	def test_sides(self):
		self.assertEqual(my_grid.check(50, 1), True)
		self.assertEqual(my_grid.check(5,50), True)
		self.assertEqual(my_grid.check(5,5), None)
		#This is because the sides of the whole thing are just 1 square wide.
		self.assertEqual(my_grid.check(51,1), None)

	def test_adding_areas(self):
		my_grid.add_wall(4,6, 3,3)
		my_grid.add_wall(4,6, 6,6)
		my_grid.add_wall(4,4, 3,6)
		my_grid.add_wall(6,6, 3,4)
		#check inside the box
		self.assertEqual(my_grid.check(5,5), None)
		#test the wall
		self.assertEqual(my_grid.check(5,6), True)
		#test the door
		self.assertEqual(my_grid.check(6,5), None)

	def test_zones_tiles_without_substance(self):
		"""Test that you can make walls that you can walk through"""
		my_grid.add_wall(7,9, 2,5, lambda:None)
		my_grid.add_wall(20,25, 2,5, lambda:"pizza")
		self.assertEqual(my_grid.check(7,3), None)
		self.assertEqual(my_grid.check(22,4), "pizza")

	def test_point_in_polygon(self):
		point_in_polygon = grid.Grid.point_in_polygon
		poly_square = [
			[2,10], [10,10],
			[10,5], [2, 5],
		]
		# inside the polygon
		self.assertEqual(point_in_polygon(None, 4, 6, poly_square), True)
		# test the edges
		self.assertEqual(point_in_polygon(None, 2, 6, poly_square), True)
		# Check the corner
		self.assertEqual(point_in_polygon(None, 2, 5, poly_square), True)
		# Check a wall in the grid
		# tests the wall poly
		wall = grid.Wall(0,10, 0,1)
		self.assertEqual(point_in_polygon(None, 4, 1, wall.poly), True)
