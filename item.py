# HackTJ 2015
# Kevin

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
	def filename(self):
		return self.filename

	def __str__(self):
		return "<{}: {}; {} cal>".format(self.category, self.name, self.calories)

	def catalogue():
		items = []
		# name, category, calories, delishness, filename
		items.append(Item("tomato", topping, 6, 5, "tomato.png"))
		items.append(Item("lettuce", topping, 2, 5, "lettuce.png"))
		items.append(Item("mushrooms", topping, 7, 5, "mushrooms.png"))
		items.append(Item("pickles", topping, 4, 10, "pickle.png"))
		items.append(Item("bacon", topping, 10, 5, "bacon.png"))
		items.append(Item("ketchup", condiment, 10, 5, "ketchup.png"))
		items.append(Item("mustard", condiment, 10, 5, "mustard.png"))
		items.append(Item("mayo", condiment, 10, 5, "mayo.png"))
		items.append(Item("BBQ", condiment, 10, 5, "bbq.png"))
		items.append(Item("horse radish", condiment, 10, 5, "horse.png"))
		items.append(Item("beef", meat, 10, 5, "cow.png"))
		items.append(Item("tofu", meat, 10, 5, "tofu.png"))
		items.append(Item("fish", meat, 10, 5, "fish.png"))
		# items.append(Item("portobello mushrooms", meat, 10, 5, "xxx.png"))
		items.append(Item("regular", bun, 10, 5, "regular.png"))
		items.append(Item("sesame", bun, 10, 5, "sesame.png"))
		return items

def main():
	from tkinter import Tk, Frame, BOTH, PhotoImage, Label
	from random import random
	root = Tk()
	root.title("Testing images")
	items = Item.catalogue()
	photo = PhotoImage(file = items[int(random() * len(items))].filename)
	label = Label(root, image=photo)
	label.grid()
	root.mainloop()

if __name__ == '__main__': main()