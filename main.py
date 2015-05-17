import text
from person import Person
from cheeseburger import Cheeseburger
import threading
from subprocess import call

def makeCheeseburger(chara):
	contents = chara.backpackContents()
	cat = ["topping", "condiment", "meat", "bun"]
	cont = [0, 0, 0, 0]
	for c in range(len(cat)):
		for i in range(len(contents)):
			item = chara.viewItem(i)
			if item.category == cat[c]:
				print(str(i)+". "+item.__str__())
				cont[c]+=1
		print()

	print(" "*10+"-"*30+" "*10)
	ingredients = []
	for i in range(len(cat)):
		while cont[i]>0:
			c = int(input("%10s"%cat[i]+" #: "))
			if contents[c].category == cat[i]:
				ingredients.append(contents[c])
				break
			print("Error: invalid input.")
	c = Cheeseburger()
	for i in ingredients:
		c.add(i)
		chara.removeFromBackpack(i)
	return c

def displayCheeseburgerStat(c):
	print("     calories: "+str(c.calories))
	print("       energy: "+str(c.calories//10))
	print("deliciousness: "+str(c.delish))

def main():
#	t = threading.Thread(target = call, args = (["afplay", "hanging_tree.wav"],))
#	t.start()
	print("Press [enter] to continue.")
	print("-"*50)
	text.intro()
	print("-"*50)
	print("  Use arrow keys to navigate. Collect food as")
	print(" you go, but keep an eye on your health status.")
	print("-"*50)
	import main_game
	person = main_game.person
	cause = main_game.cause
	if cause == "time":
		text.outro(0)
		return
	elif cause == "hunger":
		text.outro(1)
		return
	print("-"*50)
	print("            MAKE YOUR OWN CHEESEBURGER")
	print("   choose one item from each of the following")
	print("     categories to add to your cheeseburger")
	print(" "*10+"-"*30+" "*10)
	c = makeCheeseburger(person)
	print(" "*10+"-"*30+" "*10)
	displayCheeseburgerStat(c)
	print("-"*50)
	person.eat(c)
	if person.hunger > 2 and person.happy <= 7:
		input("Press [enter] to continue.")
		text.outro(3)
	elif person.hunger > 2 and person.happy > 7:
		input("Press [enter] to continue.")
		text.outro(2)
	print()

if __name__ == '__main__': main()