def goTable():
	print('\nYou take a few steps towards the other side of the room to the small table with your outside clothes. Your coat used to hang on the wall here, before the hooks disappeared under layers of synthetic rugs and quilts. You struggle briefly with the thick black pants. Soon you are buried under layers of fleece and polyester, your feet snug in a pair of snow boots.')

def goCouch():
	print('\nYou lift the right end of the couch and walk sideways, turning the couch until the door is clear.')

def goPicture():
	print('\nYou stand next to the table and reach for the picture. Your fingers brush it, and you pull away. It’s too painful.')

def goFireplace():
	print('\nThe fire is burning brightly now. It should last while you’re out.')

def goOutside():
	print('\nYou lift the plank of wood and unlatch the door before opening it. A biting wind blasts your face as you stumble outside, yanking the door shut behind you.')	
		
def lookAround():
	print('\nEverything is white. The houses and the debris are all covered in snow. The figures of fallen trees are only bumps, covered in layers of ice. The street is filled with empty cars, stuck in the permafrost.')
	input()
	print('\n You look up at the sky, but no bird silhouette interrupts the unending gray. You haven’t seen one in a while now.')
	input()
	
def focus():
	print('\nThe snow crunches under your boots as you step towards the street. You have to go much further than usual today.')
	input()
	print('\nIn a few minutes you pass the convenience store with the truck lodged in its front entrance. There is a path cleared of snow and glass that you made at the beginning.')
	input()
	print('\nWithout its tasteless food you would have starved to death a long time ago. But there are other places. Better places, with better food. That’s where you are going today, for better food. For a cheeseburger.')
	print('\n(a) Walk to the supermarket.')
	input('enter letter: ')
	walkToMarket()

def walkToMarket():
	print('\nThe overcast skies are slumbering today, like everything else. You pass by obliterated houses, some smashed, as if by a giant fist, some dissolved into rubble.')
	input()
	print('\nAt last you reach the supermarket. The walls are more holes than plaster. You hope they don’t choose today to fall. You step inside.')
	input()

def main():
	print("\nYou add a log to the fire. Your poker glows red-orange as the fire begins to consume the new log. You place the poker into its holder next to the fireplace, a few feet away from the blanket-covered walls.")
	input()
	print('\nThe room is tiny. Next to the fireplace is a small beige door. Across from the fireplace is the door to the outside, blocked by a long white couch, spanning almost the entire wall.')
	input()
	print("\nSqueezed between the left end of the couch and the wall is a wooden table with your clothes for outside and a framed picture laying down.")
	input()
	table = False
	couch = False
	focused = False
	while not table:
		print('\n(a) Gear up. \n(b) Look at the picture. \n(c) Look at the fireplace.')
		opt = input('enter letter: ')
		if opt == 'a':
			goTable()
			table = True
		elif opt == 'b':
			goPicture()
		elif opt == 'c':
			goFireplace()
		else:
			print("\nInvalid option.")
	while not couch:
		print("\n(a) Move the couch. \n(b) Look at the picture. \n(c) Look at the fireplace.")
		opt = input('enter letter: ')
		if opt == 'a':
			goCouch()
			couch = True
		elif opt == 'b':
			goPicture()
		elif opt == 'c':
			goFireplace()
		else:
			print("\nInvalid option.")
	print('\n(a) Go outside.')
	opt = input('enter letter: ')
	goOutside()

	while not focused:
		print('\n(a) Look around. \n(b) Focus.')
		opt = input('enter letter: ')
		if opt == 'a':
			lookAround()
		elif opt == 'b':
			focus()
			focused = True
	#MAZE GAME BEGINS


if __name__ == '__main__': main()