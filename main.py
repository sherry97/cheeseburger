import text
from person import Person
from cheeseburger import Cheeseburger

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
#	text.intro()
	import main_game
	person = main_game.person
	c = makeCheeseburger(person)
#	print(person.hunger, person.happy)
	person.eat(c)
#	print(person.hunger, person.happy)
	if person.hunger == 0: text.outro(1)
	elif person.hunger > 0 and person.happy == 0: text.outro(3)
	elif person.hunger > 0 and person.happy > 0: text.outro(2)
	else: text.outro(0)

if __name__ == '__main__': main()