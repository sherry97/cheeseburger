class Person():
	hunger = 50
	happy = 5
	backpack = Backpack();

	def __init__():
		self.hunger = hunger
		self.happy = happy
		self.backpack = Backpack();

	def eat(c):
		hunger += c.calories();
		happy += c.delish();
		if hunger > 100: hunger = 100
		if happy > 10: happy = 10
		return hunger

	def move():
		hunger -= 5
		happy -= .5

	def hunger():
		return hunger

	def happy():
		return happy

	def sethunger(val):
		hunger = val
		return hunger

	def sethappy(val):
		happy = val
		return happy

	def viewItem(i):
		return backpack.get(i)

	def backpack():
		backpack.display();

	def backpackContents():
		return backpack.contents();

	def addToBackpack(o):
		backpack.add(o)

	def removeFromBackpack(o):
		backpack.remove(o)
