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


	def __repr__(self):
		return("x=%i, y=%i, type = bungalow "%(self.left_bottom[0], self.left_bottom[1]))


	def score(self, closest):
		self.freeSpace = closest
		value = 399000 + (399000 * 0.04 * (self.freeSpace / 2))
		self.value = value
		return value


class Maison:
	name = 'maison'
	length = 33
	width = 34
	price = 610000
	marginalValue = 1.06

	def __init__(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return ("x=%i, y=%i, type = maison "%(self.left_bottom[0], self.left_bottom[1]))

	def score(self, closest):
		self.freeSpace = closest
		value = 610000 + (610000 * 0.06 * (self.freeSpace / 2))
		self.value = value
		return value
#
# class Water:
# 	total_area = 0.2 * 180 * 160
# 	min_ratio = 1
# 	max_ratio = 4
