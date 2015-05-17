# HackTJ 2015

from tkinter import *
from random import random, shuffle, randrange
from item import Item
from time import time
from maze import Maze

color_coding = {"meat": "#993300", "topping": "#99FF66", "condiment": "#FFCC00",
	"bun": "#996600", "cheese": "#FFFF66", "blank": "#000000", "wall": "#FFFFFF"}

# def setUpCanvas(root, WIDTH, HEIGHT): # These are the REQUIRED magic lines to enter graphics mode.
# 	root.title("Cheeseburger")
# 	canvas = Canvas(root, width  = WIDTH, height = HEIGHT) #, bg = 'black')
# 	canvas.pack() #expand = YES, fill = BOTH)
# 	return canvas

position = (1, 1)
MAZE = None

def position_works(dx, dy):
	global position, MAZE
	new_x = dx + position[0]
	new_y = dy + position[1]
	if new_x < 0 or new_y < 0 or new_x > len(MAZE) - 1 or new_y > len(MAZE[0]): return False
	if MAZE[new_x][new_y] != "blank": return False
	print("should move now")
	print("pos: {} ; new_pos: {}".format(position, (new_x, new_y)))
	return True

def key(event):
	global position
	"""shows key or tk code for the key"""
	if event.keysym == 'Escape':
		root.destroy()
	if event.char == event.keysym:
		pass
	elif len(event.char) == 1:
		pass
	else:
		# f1 to f12, shift keys, caps lock, Home, End, Delete ...
		print( 'Special Key %r' % event.keysym )
		if event.keysym == 'Up':
			if position_works(0, -1):
				position = (position[0], position[1] - 1)
		if event.keysym == 'Down':
			if position_works(0, 1):
				position = (position[0], position[1] + 1)
		if event.keysym == 'Right':
			if position_works(0, 1):
				position = (position[0] + 1, position[1])
		if event.keysym == 'Left':
			if position_works(0, -1):
				position = (position[0] - 1, position[1])

def pos_loop(canvas, master, M_WIDTH, M_HEIGHT, G_WIDTH, G_HEIGHT, maze, even = True):
	x = position[0] ; y = position[1]
	color = color_coding[maze[x][y]]
	if even:
		canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = "#3366FF")
	else:
		canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = color)
	master.after(500, pos_loop, canvas, master, M_WIDTH, M_HEIGHT, G_WIDTH, G_HEIGHT, maze, not even)

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

def main():
	global MAZE
	M_WIDTH = 51 ; M_HEIGHT = 35	
	G_WIDTH = M_WIDTH * 20 ; G_HEIGHT = M_HEIGHT * 20
	T_WIDTH = G_WIDTH + 200 ; T_HEIGHT = G_HEIGHT

	master = Tk()
	master.bind_all('<Key>', key)

	canvas = Canvas(master, width=T_WIDTH, height=T_HEIGHT)
	canvas.pack()

	maze=make_maze(int(M_HEIGHT*0.5), int(M_WIDTH*0.5-0.5))
	MAZE = maze
	items = Item.catalogue()

	for y in range(M_HEIGHT):
		for x in range(M_WIDTH):
			# display_item(r, c, WIDTH, HEIGHT, items, canvas)
			# img = PhotoImage(file=items[r * 3 + c].filename)
			# idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)
# <<<<<<< HEAD
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


			# canvas.pack()
	pos_loop(canvas, master, M_WIDTH, M_HEIGHT, G_WIDTH, G_HEIGHT, maze)
	master.mainloop()

if __name__ == '__main__': main()