# HackTJ 2015
# Kevin

topping = "topping"
condiment = "condiment"
meat = "meat"
bun = "bun"
cheese = "cheese"

class Item():
	def __init__(self, name, category, calories, delish):
		self.name = name
		self.category = category
		self.calories = calories
		self.delish = delish
		# filename is the name of a jpg file

	def __str__(self):
		return "<{}: {}; {} cal>".format(self.category, self.name, self.calories)
	def __repr__(self):
		return "<{}: {}; {} cal>".format(self.category, self.name, self.calories)
	def catalogue():
		items = []
		# name, category, calories, delishness, filename
		items.append(Item("tomato", topping, 6, 5))
		items.append(Item("lettuce", topping, 2, 5))
		items.append(Item("mushrooms", topping, 7, 5))
		items.append(Item("jalapenos", topping, 4, 10))

		items.append(Item("ketchup", condiment, 9, 7))
		items.append(Item("mustard", condiment, 8, 5))
		items.append(Item("mayo", condiment, 20, 5))
		items.append(Item("BBQ sauce", condiment, 11, 5))
		items.append(Item("horse radish", condiment, 10, 5))

		items.append(Item("beef", meat, 400, 5))
		items.append(Item("tofu", meat, 250, 4))
		items.append(Item("fish", meat, 250, 5))
		items.append(Item("chicken", meat, 300, 5))
		items.append(Item("veg", meat, 200, 4))

		items.append(Item("white bread", bun, 150, 5))
		items.append(Item("rye bread", bun, 152, 10))
		items.append(Item("wheat bread", bun, 152, 10))
		return items

	def describe():
		descriptions = {}
		descriptions['tomato'] = 'Aha! A tomato! You have found the vegetable section. Or is it a fruit? You look around for an indication, but all of the nearby shelves are smashed to bits.'
		descriptions['lettuce'] = 'You salvaged iceberg lettuce once. When you thawed it, it turned to mush. Something about its high water content. And it has no nutrition anyway. But the romaine is a bit thicker. It’ll be at least a little crispy when you thaw it.'
		descriptions['mushrooms'] = 'You don’t know how long you’ve spent searching through this section. You know there won’t be anything here. There are markings all over the shelves. Whatever was once edible is no longer. But you can tell this is the mushroom section. The day everything changed, that’s what you were eating. Creamy mushroom soup at the corner of Randolph and 9th. You can still remember that feeling of total satisfaction, that last moment of normalcy, when suddenly the windows turned--Wait. What’s that? A single container of portobello mushrooms at the bottom of this stack of debris! It won’t even take mush-room in your pack.'
		descriptions['jalapenos'] = 'You like jalapenos. They warm you up.'

		descriptions['ketchup'] = 'Ah, the red ambrosia. What was a burger without ketchup? To be fair, your coworker Anna didn’t put ketchup on her burgers, or even her fries. But she had only liked plain foo. Like cheese-with-rice plain food. Well she was probably gone now. Like everyone else.'
		descriptions['mustard'] = 'Ketchup’s Luigi. On hot dogs or burgers, mustard is good. Just not as good.'
		descriptions['mayo'] = 'You find a jar of Mayonnaise. Did people even put this on burgers? You can’t remember. It gets a little harder each time to remember how things were before.'
		descriptions['BBQ sauce'] = '‘Hot dogs, ribs, pizza, tonkatsu…’ The list goes on and on. BBQ sauce can definitely go on burgers too.'
		descriptions['horse radish'] = 'Horseradish. Mmmm. You can feel your sinuses buzzing already. How did they not smell this out? Maybe they don’t eat it...'
		
		descriptions['beef'] = 'You heave the fallen section of the ceiling to the side with enormous effort. It lands on the floor with a loud thud. You desperately search the revealed debris, and at last, your effort is rewarded. You can hear the angelic chorus singing down in a column of light. A real hamburger patty. Made with Certified ® Angus Beef.'
		descriptions['tofu'] = 'You never understood why people liked tofu. It was so bland, little better than the convenience store food. But it’s nutritious. And it doesn’t taste bad, either.'
		descriptions['fish'] = 'Even frozen, its smell permeates the air, leading you straight to it. The fish section. Under the counter you find an untouched piece of tuna, just the right size for a burger.'
		descriptions['chicken'] = 'People used to complain “what part of the chicken was the chicken patty” or something like that. But you’re glad to find any edible part of a chicken. Really any edible part of--well, anything edible, really.'
		descriptions['veg'] = 'Even your vegetarian friends didn’t eat these concoctions. Especially this brand. How did this company stay in business?'

		descriptions['white bread'] = 'White bread. It’s plain, but good. White, brown--you don’t discriminate.'
		descriptions['rye bread'] = 'The sight of rye bread curves the corners of your mouth up.'
		descriptions['wheat bread'] = 'Wheat bread. Necessary for any burger. And brown or white, you don’t discriminate.'

		return descriptions

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
