# HackTJ 2015

from tkinter import *
from random import random, shuffle, randrange
from item import Item
from time import time
from person import Person
import text

color_coding = {"meat": "#993300", "topping": "#99FF66", "condiment": "#FFCC00",
	"bun": "#996600", "cheese": "#FFFF66", "blank": "#000000", "wall": "#FFFFFF"}

# def setUpCanvas(root, WIDTH, HEIGHT): # These are the REQUIRED magic lines to enter graphics mode.
# 	root.title("Cheeseburger")
# 	canvas = Canvas(root, width  = WIDTH, height = HEIGHT) #, bg = 'black')
# 	canvas.pack() #expand = YES, fill = BOTH)
# 	return canvas
position = (1, 1)
# MAZE = None ; CANVAS = None

def position_works(dx, dy):
	global position, maze
	new_x = dx + position[0]
	new_y = dy + position[1]
	if new_x < 0 or new_y < 0 or new_x > len(maze) - 1 or new_y > len(maze[0]) - 1: return False
	if maze[new_x][new_y] == "wall": return False
	#print("should move now")
	#print("pos: {} ; new_pos: {}".format(position, (new_x, new_y)))
	return True

def key(event):
	global position, canvas, maze, person, stopped
	"""shows key or tk code for the key"""
	if event.keysym == 'Escape' or event.keysym == "q":
		stopped = True
		root.quit()
	# if event.char == event.keysym:
	# 	if event.keysym == 'q':
	# 		stopped = True
	# 		exit()
	else:
		# f1 to f12, shift keys, caps lock, Home, End, Delete ...
		x = position[0]
		y = position[1]
		# print( 'Special Key %r' % event.keysym )
		if event.keysym == 'Up':
			if position_works(0, -1):
				position = (position[0], position[1] - 1)
		if event.keysym == 'Down':
			if position_works(0, 1):
				position = (position[0], position[1] + 1)
		if event.keysym == 'Right':
			if position_works(1, 0):
				position = (position[0] + 1, position[1])
		if event.keysym == 'Left':
			if position_works(-1, 0):
				position = (position[0] - 1, position[1])

		if x != position[0] or y != position[1]:
			person.move()
			canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = color_coding[maze[x][y]])
			if maze[position[0]][position[1]] != "blank" and maze[position[0]][position[1]] != "cheese":
				item = pick_item(maze[position[0]][position[1]])
				maze[position[0]][position[1]] = "blank"
				person.addToBackpack(item)
				# person.backpack.display()

def pick_item(category):
	global items
	while True:
		item = items[int(random() * len(items))]
		if item.category == category:
			return item

def pos_loop(canvas, root, M_WIDTH, M_HEIGHT, G_WIDTH, G_HEIGHT, maze, n = 4):
	global stopped
	if stopped:
		canvas.create_rectangle(0, 0, G_WIDTH, G_HEIGHT, fill = 'black')
		canvas.create_text(G_WIDTH / 2, G_HEIGHT / 2, text = u"\u2193Look at the console\u2193", font = ("Purisa", 72), fill = '#5858FA')
		return
	x = position[0] ; y = position[1]
	color = color_coding[maze[x][y]]
	if n % 4 != 0:
		canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = "#3366FF")
	else:
		canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = color)

	canvas.itemconfig(id2, text = "  position: ("+str(x) + ", " + str(y) + ")\n  hunger: {}/100 \n  happy: {}/10\n  [q] or [esc] to exit \n  runtime: {}".format(person.hunger, round(person.happy, 3), int(time() - START_TIME)))
	string = '  Stuff in Backpack'
	for k, item in enumerate(person.backpack.backpack):
		string += '\n\t-->' + item.name if k == active_item_index else '\n\t' + item.name
	canvas.itemconfig(id1, text=string)

	root.after(200, pos_loop, canvas, root, M_WIDTH, M_HEIGHT, G_WIDTH, G_HEIGHT, maze, (n + 1) % 4)

def make_maze(w = 10, h = 10):
	vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
	ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
	hor = [["+-"] * w + ['+'] for _ in range(h + 1)]
	def walk(x, y):
		vis[y][x] = 1
		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		shuffle(d)
		for (xx, yy) in d:
			if vis[yy][xx]: continue
			if xx == x: hor[max(y, yy)][x] = "+ "
			if yy == y: ver[y][max(x, xx)] = "  "
			walk(xx, yy)
	l=[]
	walk(randrange(w), randrange(h))
	for (a, b) in zip(hor, ver):
		l.append(''.join(a))
		l.append(''.join(b))
	m=[]
	for a in range(len(l)):
		n=[]
		s=l[a]
		for b in range(len(s)):
			if s[b]==" ":
				n.append("blank")
			else:
				n.append("wall")
		m.append(n)
	return m

def display_item(r, c, WIDTH, HEIGHT, items, canvas):
	print("howdy")
	img = PhotoImage(file=items[r * 3 + c].filename)
	idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)

#######################################################################

M_WIDTH = 51 ; M_HEIGHT = 35	
G_WIDTH = M_WIDTH * 20 ; G_HEIGHT = M_HEIGHT * 20
T_WIDTH = G_WIDTH + 200 ; T_HEIGHT = G_HEIGHT
START_TIME = time()

root = Tk()
root.bind_all('<Key>', key)

canvas = Canvas(root, width=T_WIDTH, height=T_HEIGHT)
canvas.pack()
CANVAS = canvas

maze = make_maze(int(M_HEIGHT*0.5), int(M_WIDTH*0.5-0.5))
items = Item.catalogue()

active_item_index = 0

person = Person()

string = '  Stuff in Backpack'
for item, n in enumerate(person.backpack.backpack):
	string += '\n\t-->' + item.name if n == active_item_index else '\n\t' + item.name
# canvas.create_rectangle(G_WIDTH, 0, T_WIDTH, T_HEIGHT, fill = "white")
id1 = canvas.create_text(G_WIDTH,20,anchor=NW,width=180,text=string)
status_text = "  hunger: {} \n  happy: {}\n  q or esc to exit \n  runtime: {}".format(person.hunger, person.happy, int(time() - START_TIME))
id2 = canvas.create_text(G_WIDTH, G_HEIGHT * 3 / 5, anchor = NW, text = status_text, font = "Purisa")

for y in range(M_HEIGHT):
	for x in range(M_WIDTH):
		item_color = color_coding["blank"]
		if maze[x][y] == "wall": #wall
			item_color = color_coding["wall"]
		elif random() < 0.1:
			item_index = int(random() * len(items))
			item = items[item_index]
			item_color = color_coding[item.category]
			maze[x][y] = item.category
		canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
			G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = item_color)

stopped = False
pos_loop(canvas, root, M_WIDTH, M_HEIGHT, G_WIDTH, G_HEIGHT, maze, stopped)
root.mainloop()

# string='Stuff in Backpack'
# for stuff in person.backpack.backpack:
# 	string+='\n\t'+stuff.name
# canvas.create_text(G_WIDTH+G_WIDTH/M_WIDTH*3,50,width=180,text=string)
# if __name__ == '__main__': main()
