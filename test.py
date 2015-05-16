from item import Item
from backpack import Backpack
from cheeseburger import Cheeseburger 
from person import Person

def setUpCatalogue():
		return Item.catalogue()

def gatherMaterials(chara, catalogue):
	for i in range(len(catalogue)):
		chara.addToBackpack(catalogue[i])

def makeCheeseburger(chara):
	contents = chara.backpackContents()
	prevcat = ''
	for i in range(len(contents)):
		item = chara.viewItem(i)
		if not item.category == prevcat: print()
		print(str(i)+". "+item.__str__())
		prevcat = item.category
	topping =   int(input("\nenter...topping #: "))
	condiment = int(input("   ...condiment #: "))
	meat =      int(input("        ...meat #: "))
	bun =       int(input("         ...bun #: "))
	print()
	ingredients = [contents[topping], contents[condiment], contents[meat], contents[bun]]
	c = Cheeseburger()
	for i in ingredients:
		c.add(i)
		chara.removeFromBackpack(i)
	return c

def main():
	catalogue = setUpCatalogue()
	chara = Person()
	gatherMaterials(chara, catalogue)
	burger = makeCheeseburger(chara)
	chara.eat(burger)
	print('hunger = '+str(chara.hunger))
	print('happy  = '+str(chara.happy))

if __name__=='__main__': main()