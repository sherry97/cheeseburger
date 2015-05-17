import random
import sys

class Maze():
	def visited(self, tup):
		x = tup[0] ; y = tup[1]
		self.grid[x][y] = 1
		self.visitedCoords.append((x, y))

	def getneighbors(self, tup):
		x = tup[0] ; y = tup[1]
		neighbors = []
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				if dx == 0 and dy == 0: continue
				if x + dx < 0 or x + dx > self.MAZE_WIDTH - 1: continue
				if y + dy < 0 or y + dy > self.MAZE_HEIGHT - 1: continue
				neighbors.append((x + dx, y + dy))
		return neighbors

	def fillMaze(self, neighbors):
		if len(neighbors) <= 0: return
		for i in range(len(neighbors)//3):
			choice = neighbors.pop(random.randint(0, len(neighbors)-1))
			self.visited(choice)
			neighbors = self.getneighbors(choice)
			self.fillMaze(neighbors)

	def __init__(self, width = 20, height = 20):
		sys.setrecursionlimit(100000)
		self.MAZE_WIDTH = width
		self.MAZE_HEIGHT = height
		self.visitedCoords = []
		self.grid = [[0 for y in range(self.MAZE_HEIGHT)] for x in range(self.MAZE_WIDTH)]
		cur = (0,0)
		self.visited(cur)
		neighbors = self.getneighbors(cur)
		self.fillMaze(neighbors)

	def getMaze(self):
		return self.grid

