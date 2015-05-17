# HackTJ 2015

from tkinter import *
from random import random
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
from random import shuffle, randrange

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
				n.append(0)
			else:
				n.append(1)
		m.append(n)
	return m

def display_item(r, c, WIDTH, HEIGHT, items, canvas):
	print("howdy")
	img = PhotoImage(file=items[r * 3 + c].filename)
	idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)

def main():
	M_WIDTH = 51 ; M_HEIGHT = 35	
	WIDTH = M_WIDTH * 20 ; HEIGHT = M_HEIGHT * 20

	master = Tk()

	canvas = Canvas(master, width=T_WIDTH, height=T_HEIGHT)
	canvas.pack()

	maze=make_maze(int(M_HEIGHT*0.5), int(M_WIDTH*0.5-0.5))

	items = Item.catalogue()

	for y in range(M_HEIGHT):
		for x in range(M_WIDTH):
			# display_item(r, c, WIDTH, HEIGHT, items, canvas)
			# img = PhotoImage(file=items[r * 3 + c].filename)
			# idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)
# <<<<<<< HEAD
# 			item_color = color_coding["blank"]
# 			if maz[x][y] == 1: #wall
# 				item_color = color_coding["wall"]
# 			elif random() < 0.1:
# 				item_index = int(random() * len(items))
# 				item = items[item_index]
# 				item_color = color_coding[item.category]
# 				maz[x][y] = item_index + 2
# 			canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
# 				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = item_color)
# =======
			#item = items[int(random() * len(items))]

			#item = items[int(random() * len(items))]
			item_color = ("#000000" if maze[x][y]==0 else "#FFFFFF")
			#item_color = color_coding[item.category]
			canvas.create_rectangle(WIDTH / M_WIDTH * x, HEIGHT / M_HEIGHT * y, 
				WIDTH / M_WIDTH * (x + 1), HEIGHT / M_HEIGHT * (y + 1), fill = item_color)


			# canvas.pack()

	master.mainloop()

if __name__ == '__main__': main()