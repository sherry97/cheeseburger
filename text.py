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
	input('\nEverything is white. The houses and the debris are all covered in snow. The figures of fallen trees are only bumps, covered in layers of ice. The street is filled with empty cars, stuck in the permafrost.')
	input('\n You look up at the sky, but no bird silhouette interrupts the unending gray. You haven’t seen one in a while now.')
	
def focus():
	input('\nThe snow crunches under your boots. In a few minutes you pass the convenience store. There is a path cleared of snow and glass that you made just after it happened.')
	input('\nYou hate and love its tasteless food. But there are better places, further away. That’s where you are going today, for better food. For a cheeseburger.')
	print('\n(a) Walk to the supermarket.')
	input('enter letter: ')
	walkToMarket()

def walkToMarket():
	input('\nThe overcast skies are slumbering today, like everything else. You pass by obliterated houses.')
	input('\nAt last you reach the supermarket. The walls are more holes than plaster. You hope they don’t choose today to fall. You step inside.')

def intro():
	input("Your poker glows red-orange as the fire begins to consume the new log. You place the poker into its holder next to the fireplace, a few feet away from the blanket-covered walls. ")
	input('\nThe room is tiny. Next to the fireplace is a small beige door. Across from the fireplace is the door to the outside, blocked by a long white couch, spanning almost the entire wall.')
	input("\nSqueezed between the left end of the couch and the wall is a wooden table with your clothes for outside and a framed picture laying down.")
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

def outro(i):
	if i == 0:
		print('\nBy the time you begin walking home, the sun has set. The distant noises start getting louder--closer. You drop everything and run, but you won’t make it. You see your shack on the horizon as the Horde catches up to you. You think of your sick little girl as the monsters descend upon you and the last dregs of starlight are ripped from the sky by bloody hands.')
	elif i == 1:
		print('\nYour legs start trembling, then your knees fall out from under you. You think that this wasn’t the way things were supposed to end as you fall to the ground. The food tumbles from your hands and your world goes dark. In the distance, you can hear the ungodly shuffling of the Horde assembling in the twilight.')
	elif i == 2:
		input('\nYou enter your small shack as the sun is setting, shutting the door as quickly as possible. You breath out a relieved sigh and take off your snow-covered jacket. You stoke the fire, add another log, and position your makeshift oven over it. You pull out the food and cook it over the fire. Half an hour later, a delicious smell wafts through the room, and you move the burger onto a plate.')
		input('\nYou take the burger to the small door. You open it and enter the bedroom. A young girl lays on the bed, sweating. She wakes up slowly, mumbling something.')
		input('\n“I’m here, lady bug. Look what I brought you.”')
		input('\nHer voice is hoarse and unintelligible.')
		input('\n“Rest your voice.” You place the burger on her nightstand. You stroke her hair and coax her into a sitting position. “Happy birthday sweetie. I brought your favorite. Remember how much you used to love these?” She manages to take a bite.')
		print('\nHer face lights up as she closes her eyes and chews slowly. She finishes the burger and you’re glad she’s eating again.')
	elif i == 3:
		input('\nYou enter your small shack as the sun is setting, shutting the door as quickly as possible. You breath out a relieved sigh and take off your snow-covered jacket. You stoke the fire, add another log, and position your makeshift oven over it. You pull out the food and cook it over the fire. Half an hour later, a delicious smell wafts through the room, and you move the burger onto a plate.')
		input('\nYou take the burger to the small door. You open it and enter the bedroom. A young girl lays on the bed, sweating. She wakes up slowly, mumbling something.')
		input('\n“I’m here, lady bug. Look what I brought you.”')
		input('\nHer voice is hoarse and unintelligible.')
		input('\n“Rest your voice.” You place the burger on her nightstand. You stroke her hair and coax her into a sitting position. “Happy birthday sweetie. I brought your favorite. Remember how much you used to love these?” She manages to take a bite.')
		print('\nShe tries to hide a grimace, smiling at you. “Thanks,” she barely forces out. You wish you had remembered what she liked a little better.')








