def catalogue():
		items = []
		items.append(Item("tomato", topping, 10))
		items.append(Item("lettuce", topping, 10))
		items.append(Item("mushrooms", topping, 10))
		items.append(Item("pickles", topping, 10))
		items.append(Item("bacon", topping, 10))

		items.append(Item("ketchup", condiment, 10))
		items.append(Item("mustard", condiment, 10))
		items.append(Item("mayo", condiment, 10))
		items.append(Item("BBQ", condiment, 10))
		items.append(Item("horse radish", condiment, 10))

		items.append(Item("beef", meat, 10))
		items.append(Item("tofu", meat, 10))
		items.append(Item("fish", meat, 10))
		items.append(Item("portobello mushroooms", meat, 10))

		items.append(Item("regular", bun, 10))
		items.append(Item("sesame", bun, 10))

		return items

def gatherMaterials(chara, catalogue):
	for i in range(len(catalogue)):
		chara.addToBackpack(catalogue[i])

def makeCheeseburger(chara):
	for i in range(len(chara.backpackContents())):
		item = chara.viewItem()
		print(i+". "+item.__str__())
	topping =   input("enter...topping #: ")
	condiment = input("   ...condiment #: ")
	meat =      input("        ...meat #: ")
	bun =       input("         ...bun #: ")
	ingredients = [chara.backpackContents[topping], chara.backpackContents[condiment], chara.backpackContents[meat], chara.backpackContents[bun]]
	c = Cheeseburger()
	for i in ingredients:
		c.add(i)
		chara.removeFromBackpack(i)

def main():
	catalogue = catalogue()
	chara = Person()
	gatherMaterials(chara, catalogue)
	makeCheeseburger()

if __name__=='__main__': main()