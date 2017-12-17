# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains the classes of the buildings, the water and a map class.

import helpers

class House:
	name = 'house'
	length = 20
	width = 20
	price = 285000
	marginalValue = 1.03

	def __init__(self, x, y):
		# self.price = 285.000
		# self.marginalValue = 1.03
		# self.location = (x, y)
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return("x=%i, y=%i, type = house "%(self.left_bottom[0], self.left_bottom[1]))

	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# Dit is nog cumulatief, en dat mag niet!
	def score(self, closest):
		self.freeSpace = closest
		value = 285000 + (285000 * 0.03 * (self.freeSpace / 2))
		self.value = value
		return value


class Bungalow:
	name = 'bungalow'
	length = 21
	width = 26
	price = 399000
	marginalValue = 1.04

	def __init__(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]
		# self.score = 0

	def top_right(self):
		return [self.x+self.width, self.y+self.length]

	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def rotate(self):
		self.length, self.width = self.width, self.length
		self.update(self.left_bottom[0], self.left_bottom[1])

	def __repr__(self):
		return ("x=%i, y=%i, type = bungalow "%(self.left_bottom[0], self.left_bottom[1]))

	def score(self, closest):
		self.freeSpace = closest
		value = 399000 + (399000 * 0.04 * (self.freeSpace / 2))
		self.value = value
		return value


class Maison:
	name = 'maison'
	length = 34
	width = 33
	price = 610000
	marginalValue = 1.06

	def __init__(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return ("x=%i, y=%i, type = maison "%(self.left_bottom[0], self.left_bottom[1]))

	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def rotate(self):
		self.length, self.width = self.width, self.length
		self.update(self.left_bottom[0], self.left_bottom[1])

	def score(self, closest):
		self.freeSpace = closest
		value = 610000 + (610000 * 0.06 * (self.freeSpace / 2))
		self.value = value
		return value


class Water:
	name = 'water'

	def __init__(self, x, y, width, length):
		self.width = width
		self.length = length
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return ("x=%i, y=%i, type = water "%(self.left_bottom[0], self.left_bottom[1]))

class Map:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.buildings = []
		self.waters = []

	def score(self):
		total_value = 0
		for current_building in self.buildings:
			closest = helpers.closest_distance(current_building, self.buildings)
			total_value += current_building.score(closest)

		return total_value

	def add_water(self, variation):

		# one water stroke in the middle of the map
		if variation == 1:
			water = Water(100, 88.5, 161, 143)
			self.waters.append(water)

		# # two strokes of water parralel positioned at 1/4 of the length from the top and bottom
		# elif variation == 2:
		# 	water1 = classes.Water(x, y, width, length)
		# 	water2 = classes.Water(x, y, width, length)
	    #
		# # two strokes of water parralel positioned at 1/3 of the length from the top and bottom
		# elif variation == 3:
		# 	water1 = classes.Water(x, y, width, length)
		# 	water2 = classes.Water(x, y, width, length)
	    #
		# # four strokes of water parralel for x and parralel for y positioned at 1/4 of the respective width and length from the outside of the map
		# elif variation == 4:
		# 	water1 = classes.Water(x, y, width, length)
		# 	water2 = classes.Water(x, y, width, length)
		# 	water3 = classes.Water(x, y, width, length)
		# 	water4 = classes.Water(x, y, width, length)
	    #
		# # four pooles of water positioned at 1/4 of diagonal to the inside of the corners of the map
		# elif variation == 5:
		# 	water1 = classes.Water(x, y, width, length)
		# 	water2 = classes.Water(x, y, width, length)
		# 	water3 = classes.Water(x, y, width, length)
		# 	water4 = classes.Water(x, y, width, length)
