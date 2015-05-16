# HackTJ 2015
# Kevin

from Tkinter import Tk, Frame, BOTH

topping = "topping"
condiment = "condiment"
meat = "meat"
bun = "bun"
cheese = "cheese"

class Item():
  
	def __init__(self, name, category, calories, delish, filename):
		self.name = name
		self.category = category
		self.calories = calories
		self.delish = delish
		self.filename = filename
		# filename is the name of a jpg file

	def calories(self):
		return self.calories
	def name(self):
		return self.name
	def delish(self):
		return self.delish
	def category(self):
		return self.category

	def __str__(self):
		return "<{}: {}; {} cal>".format(category, name, calories)

	def catalogue():
		items = []
		# name, category, calories, delishness, filename
		items.append(Item("tomato", topping, 6, 5, "tomato.png"))
		items.append(Item("lettuce", topping, 2, 5, "lettuce.jpeg"))
		items.append(Item("mushrooms", topping, 7, 5, "mushrooms.jpeg"))
		items.append(Item("pickles", topping, 4, 10, "pickle.jpeg"))
		items.append(Item("bacon", topping, 10, 5, "bacon.jpeg"))
		items.append(Item("ketchup", condiment, 10, 5, "ketchup.jpeg"))
		items.append(Item("mustard", condiment, 10, 5, "mustard.jpeg"))
		items.append(Item("mayo", condiment, 10, 5, "mayo.jpeg"))
		items.append(Item("BBQ", condiment, 10, 5, "bbq.jpeg"))
		items.append(Item("horse radish", condiment, 10, 5, "horse.jpeg"))
		items.append(Item("beef", meat, 10, 5, "cow.jpeg"))
		items.append(Item("tofu", meat, 10, 5, "tofu.jpeg"))
		items.append(Item("fish", meat, 10, 5, "fish.jpeg"))
		# items.append(Item("portobello mushrooms", meat, 10, 5, "xxx.jpeg"))
		items.append(Item("regular", bun, 10, 5, "regular.png"))
		items.append(Item("sesame", bun, 10, 5, "sesame.png"))
		return items