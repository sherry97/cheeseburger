def goOutside():
	print('You lift the plank of wood and unlatch the door before opening it. A biting wind blasts your face as you stumble outside, yanking the door shut behind you.')
	opt = input('\n(a) Look around. \n(b) Focus.')
	if opt == 'a':
		print('Everything is white. The houses and the debris are all covered in snow. The figures of fallen trees are only bumps, covered in layers of ice. The street is filled with empty cars, stuck in the permafrost. Your miniscule shack squats out of place in a line of what used to be mansions. Most of their second floors lay on the ground now. You look up at the sky, but no bird silhouette interrupts the unending gray. You haven’t seen one in a while now.')
	print('The snow crunches under your boots as you step towards the street. You have to go much further than usual today. In a few minutes you pass the convenience store with the truck lodged in its front entrance. There is a path cleared of snow and glass that you made at the beginning. You have mixed feelings about this convenience store. Without its tasteless food you would have starved to death a long time ago. But there are other places. Better places, with better food. That’s where you are going today, for better food. For a cheeseburger.')
	print('The overcast skies withhold their slow wrath today. Perhaps they are slumbering, like everything else. You pass by countless obliterated houses, like a giant fist smashed into their roofs, some dissolved into rubble. The cold pierces through your layers of clothes. At last you reach the supermarket. The walls are more holes than plaster. You hope they don’t choose today to fall. You step inside.')

def main():
	print("You add a log to the fire. Your poker glows red-orange as the fire begins to consume the new log. You place the poker into its holder next to the fireplace, a few feet away from the blanket-covered walls. ")
	print('The room is tiny and sparsely decorated. The only breaks in the wall-carpets are the fireplace and two doors. Across from the fireplace is the smaller door. In front of the other door, the one to outside, is a long white couch that almost spans that entire wall. Squeezed between the left end of the couch and the wall is a wooden table with your clothes for outside. Against the fourth wall is a desk. A framed picture lays facedown on it.')
	opt = input('\n(a) Go to the wooden table. \n(b) Move the couch. \n(c) Look at the picture. \n(d) Look at the fireplace.')
	if opt == 'a' or opt == 'b':
		goOutside()
	if opt == 'c':
		print('You walk up to the desk, reaching for the picture. Your fingers brush it, and you pull away. It’s too painful.')
		opt = input('\n(a) Go to the wooden table. \n(b) Move the couch. \n(c) Look at the fireplace.')
		if opt == 'a' or opt == 'b':
			goOutside()
		if opt == 'c':
			print('The fire is burning brightly now. It should last while you’re out.')
			opt = input('\n(a) Go to the wooden table. \n(b) Move the couch.')
			goOutside()
	if opt == 'd':
		print('The fire is burning brightly now. It should last while you’re out.')
		opt = input('\n(a) Go the wooden table. \n(b) Move the couch. \n(c) Look at the picture.')
		if opt == 'a' or opt == 'b':
			goOutside()
		else:
			print('You walk up to the desk, reaching for the picture. Your fingers brush it, and you pull away. It’s too painful.')
			opt = input('\n(a) Go to the wooden table. \n(b) Move the couch.')
			goOutside()
if __name__ == '__main__': main()