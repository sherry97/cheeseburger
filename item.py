# HackTJ 2015
# Kevin

from Tkinter import Tk, Frame, BOTH

topping = "topping"
condiment = "condiment"
meat = "meat"
bun = "bun"

class Item():
  
	def __init__(self, name, category, calories):
		self.name = name
		self.category = category
		self.calories = calories

	def calories(self):
		return self.calories
	def name(self):
		return self.name
	def category(self):
		return self.category

	def __str__(self):
		return "<{}: {}; {} cal>".format(category, name, calories)

	def catalogue():
		items = []
		items.add(Item("tomato", topping, 10))
		items.add(Item("lettuce", topping, 10))
		items.add(Item("mushrooms", topping, 10))
		items.add(Item("pickles", topping, 10))
		items.add(Item("bacon", topping, 10))
		items.add(Item("ketchup", condiment, 10))
		items.add(Item("mustard", condiment, 10))
		items.add(Item("mayo", condiment, 10))
		items.add(Item("BBQ", condiment, 10))
		items.add(Item("horse radish", condiment, 10))
		items.add(Item("beef", meat, 10))
		items.add(Item("tofu", meat, 10))
		items.add(Item("fish", meat, 10))
		items.add(Item("portobello mushroooms", meat, 10))
		items.add(Item("regular", bun, 10))
		items.add(Item("sesame", bun, 10))
		return items


		

def main():
	pass


if __name__ == '__main__':
	main() 