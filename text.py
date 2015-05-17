def goOutside():
	print('\nYou lift the plank of wood and unlatch the door before opening it. A biting wind blasts your face as you stumble outside, yanking the door shut behind you.')
	print('\n(a) Look around. \n(b) Focus.')
	opt = input('enter letter: ')
	if opt == 'a':
		print('\nEverything is white. The houses and the debris are all covered in snow. The figures of fallen trees are only bumps, covered in layers of ice. The street is filled with empty cars, stuck in the permafrost. Your miniscule shack squats out of place in a line of what used to be mansions. Most of their second floors lay on the ground now. You look up at the sky, but no bird silhouette interrupts the unending gray. You haven’t seen one in a while now.')
	print('\nThe snow crunches under your boots as you step towards the street. You have to go much further than usual today. In a few minutes you pass the convenience store with the truck lodged in its front entrance. There is a path cleared of snow and glass that you made at the beginning. You have mixed feelings about this convenience store. Without its tasteless food you would have starved to death a long time ago. But there are other places. Better places, with better food. That’s where you are going today, for better food. For a cheeseburger.')
	print('\nThe overcast skies withhold their slow wrath today. Perhaps they are slumbering, like everything else. You pass by countless obliterated houses, like a giant fist smashed into their roofs, some dissolved into rubble. The cold pierces through your layers of clothes. At last you reach the supermarket. The walls are more holes than plaster. You hope they don’t choose today to fall. You step inside.')

def main():
	print("\nYou add a log to the fire. Your poker glows red-orange as the fire begins to consume the new log. You place the poker into its holder next to the fireplace, a few feet away from the blanket-covered walls. ")
	print('\nThe room is tiny and sparsely decorated. The only breaks in the wall-carpets are the fireplace and two doors. Across from the fireplace is the smaller door. In front of the other door, the one to outside, is a long white couch that almost spans that entire wall. Squeezed between the left end of the couch and the wall is a wooden table with your clothes for outside. Against the fourth wall is a desk. A framed picture lays facedown on it.')
	print('\n(a) Go to the wooden table. \n(b) Move the couch. \n(c) Look at the picture. \n(d) Look at the fireplace.')
	opt = input('enter letter: ')
	if opt == 'a':
		print('\nYou take a few steps towards the other side of the room to the small table with your outside clothes. Your coat used to hang on the wall here, before the hooks disappeared under layers of synthetic rugs and quilts. You struggle briefly with the thick black pants. Soon you are buried under layers of fleece and polyester, your feet snug in a pair of snow boots.')
		goOutside()
	if opt == 'b':
		print('\nYou lift the right end of the couch and walk sideways, turning the couch until the door is clear.')
		goOutside()
	if opt == 'c':
		print('\nYou walk up to the desk, reaching for the picture. Your fingers brush it, and you pull away. It’s too painful.')
		print('\n(a) Go to the wooden table. \n(b) Move the couch. \n(c) Look at the fireplace.')
		opt = input('enter letter: ')
		if opt == 'a':
			print('\nYou take a few steps towards the other side of the room to the small table with your outside clothes. Your coat used to hang on the wall here, before the hooks disappeared under layers of synthetic rugs and quilts. You struggle briefly with the thick black pants. Soon you are buried under layers of fleece and polyester, your feet snug in a pair of snow boots.')
			goOutside()
		if opt == 'b':
			print('\nYou lift the right end of the couch and walk sideways, turning the couch until the door is clear.')
			goOutside()
		if opt == 'c':
			print('\nThe fire is burning brightly now. It should last while you’re out.')
			print('\n(a) Go to the wooden table. \n(b) Move the couch.')
			opt = input('enter letter: ')
			if opt == 'a':
				print('\nYou take a few steps towards the other side of the room to the small table with your outside clothes. Your coat used to hang on the wall here, before the hooks disappeared under layers of synthetic rugs and quilts. You struggle briefly with the thick black pants. Soon you are buried under layers of fleece and polyester, your feet snug in a pair of snow boots.')
				goOutside()
			if opt == 'b':
				print('\nYou lift the right end of the couch and walk sideways, turning the couch until the door is clear.')
				goOutside()
	if opt == 'd':
		print('\nThe fire is burning brightly now. It should last while you’re out.')
		print('\n(a) Go the wooden table. \n(b) Move the couch. \n(c) Look at the picture.')
		opt = input('enter letter: ')
		if opt == 'a':
			print('\nYou take a few steps towards the other side of the room to the small table with your outside clothes. Your coat used to hang on the wall here, before the hooks disappeared under layers of synthetic rugs and quilts. You struggle briefly with the thick black pants. Soon you are buried under layers of fleece and polyester, your feet snug in a pair of snow boots.')
			goOutside()
		if opt == 'b':
			print('\nYou lift the right end of the couch and walk sideways, turning the couch until the door is clear.')
			goOutside()
		else:
			print('\nYou walk up to the desk, reaching for the picture. Your fingers brush it, and you pull away. It’s too painful.')
			print('\n(a) Go to the wooden table. \n(b) Move the couch.')
			opt = input('enter letter: ')
			if opt == 'a':
				print('\nYou take a few steps towards the other side of the room to the small table with your outside clothes. Your coat used to hang on the wall here, before the hooks disappeared under layers of synthetic rugs and quilts. You struggle briefly with the thick black pants. Soon you are buried under layers of fleece and polyester, your feet snug in a pair of snow boots.')
				goOutside()
			if opt == 'b':
				print('\nYou lift the right end of the couch and walk sideways, turning the couch until the door is clear.')
				goOutside()

if __name__ == '__main__': main()