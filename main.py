import text
from person import Person
from cheeseburger import Cheeseburger

def makeCheeseburger(chara):
	contents = chara.backpackContents()
	cat = ["topping", "condiment", "meat", "bun"]
	for c in cat:
		for i in range(len(contents)):
			item = chara.viewItem(i)
			if item.category == c: print(str(i)+". "+item.__str__())
		print()

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
	print("Press [enter] to continue.")
	print("-"*50)
#	text.intro()
	import main_game
	person = main_game.person
	print("-"*50)
	print("            MAKE YOUR OWN CHEESEBURGER")
	print("   choose one item from each of the following")
	print("     categories to add to your cheeseburger")
	print("-"*50)
	c = makeCheeseburger(person)
	print("-"*50)
	print("Based on the nutritional content of your cheeseburger, you recieved ending #", end="")
	person.eat(c)
	if person.hunger == 0:
		print("1.")
		text.outro(1)
	elif person.hunger > 0 and person.happy == 0:
		print("3.")
		print("Press [enter] to continue.")
		text.outro(3)
	elif person.hunger > 0 and person.happy > 0:
		print("2.")
		print("Press [enter] to continue.")
		text.outro(2)
	else:
		print("0.")
		text.outro(0)
	print()

if __name__ == '__main__': main()