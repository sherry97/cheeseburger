from item import Item

class Cheeseburger():

	def __init__(self):
		self.calories = 0
		self.delish = 0
		self.size = 0
		self.content = []

	def __init__(self, calories=0, delish=0, size=0, content=[]):
		self.calories = calories
		self.delish = delish
		self.size = size
		self.content = content

	def calories(self):
		return self.calories

	def delish(self):
		return self.delish

	def add(self, o):
		self.content.append(o)
		self.calories += o.calories
		rawdelish = self.delish*self.size+o.delish
		self.size += 1
		self.delish = rawdelish/self.size

	def remove(self, o):
		self.content.remove(o);
		self.calories -= o.calories
		rawdelish = self.delish*self.size-o.delish
		self.size -= 1
		self.delish = rawdelish/self.size

	def display(self):
		print(self.content)
