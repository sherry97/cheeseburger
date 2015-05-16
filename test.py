from item import Item
from backpack import Backpack
from cheeseburger import Cheeseburger 
from person import Person

def setUpCatalogue():
		return Item.catalogue()

def gatherMaterials(chara, catalogue):
	for i in range(len(catalogue)):
		print(catalogue[i])
		chara.addToBackpack(catalogue[i])

def makeCheeseburger(chara):
	contents = chara.backpackContents()
	for i in range(len(contents)):
		item = chara.viewItem(i)
		print(str(i)+". "+item.__str__())
	topping =   int(input("enter...topping #: "))
	condiment = int(input("   ...condiment #: "))
	meat =      int(input("        ...meat #: "))
	bun =       int(input("         ...bun #: "))
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