from backpack import Backpack
from cheeseburger import Cheeseburger

class Person():

#	def __init__(self):
#		self.hunger = 50
#		self.happy = 5
#		self.backpack = Backpack();

	def __init__(self, hunger=50, happy=5, backpack=Backpack()):
		self.hunger = hunger
		self.happy = happy
		self.backpack = backpack

	def eat(self, c):
		self.hunger += c.calories//10
		self.happy += c.delish
		if self.hunger > 100: self.hunger = 100
		if self.happy > 10: self.happy = 10

	def move(self):
		self.hunger -= .5
		self.happy -= .01

	def sethunger(self, val):
		self.hunger = val
		return self.hunger

	def sethappy(self, val):
		self.happy = val
		return self.happy

	def viewItem(self, i):
		return self.backpack.get(i)

	def backpack(self):
		self.backpack.display();

	def backpackContents(self):
		return self.backpack.contents();

	def addToBackpack(self, o):
		self.backpack.add(o)

	def removeFromBackpack(self, o):
		self.backpack.remove(o)
