class Backpack():

	def __init__(self):
		self.backpack = []

	def display(self):
		print(self.backpack)

	def contents(self):
		return self.backpack

	def add(self, o):
		self.backpack.append(o)
		return self.backpack

	def remove(self, o):
		self.backpack.remove(o)
		return self.backpack

	def get(self, i):
		return self.backpack[i]

	def size(self):
		return len(self.backpack)