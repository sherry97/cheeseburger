class Cheeseburger():
	calories = 0
	delish = 0
	size = 0
	content = []

	def __init__():
		self.calories = calories
		self.delish = delish
		self.size = size
		self.content = content

	def calories():
		return calories

	def delish():
		return delish

	def add(o):
		content[-1] = o
		calories += o.calories()
		rawdelish = delish*size+o.delish()
		size += 1
		delish = rawdelish/size

	def remove(o):
		content.remove(o);
		calories -= o.calories()
		rawdelish = delish*size-o.delish()
		size -= 1
		delish = rawdelish/size

	def display():
		print(content)
