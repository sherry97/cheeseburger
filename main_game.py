# HackTJ 2015

from tkinter import Tk, Frame, BOTH, PhotoImage, Label
from random import random
from item import Item

def main():
	root = Tk()
	root.title("Testing images")
	items = Item.catalogue()
	photo = PhotoImage(file = items[int(random() * len(items))].filename)
	label = Label(root, image=photo)
	label.grid()
	root.mainloop()
if __name__ == '__main__': main()