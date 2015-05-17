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

def display_item(r, c, WIDTH, HEIGHT, items, canvas):
	print("howdy")
	img = PhotoImage(file=items[r * 3 + c].filename)
	idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)

def main():
	M_WIDTH = 51 ; M_HEIGHT = 35
	G_WIDTH = M_WIDTH * 20 ; G_HEIGHT = M_HEIGHT * 20
	T_WIDTH = G_WIDTH + 200 ; T_HEIGHT = G_HEIGHT
	# maze, game, total

	maz = Maze(M_WIDTH, M_HEIGHT).getMaze()
	# maze = [[int(random() * 1.2) for c in range(M_WIDTH)] for r in range(M_HEIGHT)]



	master = Tk()

	canvas = Canvas(master, width=T_WIDTH, height=T_HEIGHT)
	canvas.pack()

	items = Item.catalogue()

	for y in range(M_HEIGHT):
		for x in range(M_WIDTH):
			# display_item(r, c, WIDTH, HEIGHT, items, canvas)
			# img = PhotoImage(file=items[r * 3 + c].filename)
			# idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)
			item_color = color_coding["blank"]
			if maz[x][y] == 1: #wall
				item_color = color_coding["wall"]
			elif random() < 0.1:
				item_index = int(random() * len(items))
				item = items[item_index]
				item_color = color_coding[item.category]
				maz[x][y] = item_index + 2
			canvas.create_rectangle(G_WIDTH / M_WIDTH * x, G_HEIGHT / M_HEIGHT * y, 
				G_WIDTH / M_WIDTH * (x + 1), G_HEIGHT / M_HEIGHT * (y + 1), fill = item_color)

			# canvas.pack()

	master.mainloop()
if __name__ == '__main__': main()