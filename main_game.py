# HackTJ 2015

from tkinter import *
from random import random
from item import Item
from time import time

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
	M_WIDTH = 50 ; M_HEIGHT = 35
	WIDTH = M_WIDTH * 20 ; HEIGHT = M_HEIGHT * 20

	master = Tk()

	canvas = Canvas(master, width=WIDTH, height=HEIGHT)
	canvas.pack()

	items = Item.catalogue()

	for y in range(M_HEIGHT):
		for x in range(M_WIDTH):
			# display_item(r, c, WIDTH, HEIGHT, items, canvas)
			# img = PhotoImage(file=items[r * 3 + c].filename)
			# idd = canvas.create_image(WIDTH / 3 * r, HEIGHT / 3 * c, anchor=NW, image=img)
			item = items[int(random() * len(items))]
			item_color = color_coding[item.category]
			canvas.create_rectangle(WIDTH / M_WIDTH * x, HEIGHT / M_HEIGHT * y, 
				WIDTH / M_WIDTH * (x + 1), HEIGHT / M_HEIGHT * (y + 1), fill = item_color)

			# canvas.pack()

	master.mainloop()
if __name__ == '__main__': main()