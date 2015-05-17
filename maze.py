import random

class Maze():
	def visited(self, (x, y)):
		self.grid[x, y] = 1
		self.visitedCoords.append((x, y))

	def getneighbors(self, (x, y)):
		neighbors = []
		if self.grid[x-1][y-1] == 0: neighbors.append((x-1, y-1))
		if self.grid[x-1][y] == 0: neighbors.append((x-1, y))
		if self.grid[x-1][y+1] == 0: neighbors.append((x-1, y+1))
		if self.grid[x][y-1] == 0: neighbors.append((x, y-1))
		if self.grid[x][y+1] == 0: neighbors.append((x, y+1))
		if self.grid[x+1][y-1] == 0: neighbors.append((x+1, y-1))
		if self.grid[x+1][y] == 0: neighbors.append((x+1, y))
		if self.grid[x+1][y+1] == 0: neighbors.append((x+1, y+1))
		for (x, y) in neighbors:
			if x<0 or x>self.MAZE_WIDTH or y<0 or y>self.MAZE_HEIGHT:
				neighbors.remove((x,y))
		return neighbors

	def fillMaze(self, neighbors):
		if len(neighbors)<0: return
		for i in range(len(neighbors)//3):
			choice = neighbors.pop(random.randint(0, len(neighbors)-1))
			visited(choice)
			neighbors = getneighbors(self, choice)
			fillMaze(self, neighbors)

	def __init__(self, width = 20, height = 20):
		self.MAZE_WIDTH = width
		self.MAZE_HEIGHT = height
		self.visitedCoords = []
		self.grid = [[0 for x in range(self.MAZE_WIDTH)] for y in range(self.MAZE_HEIGHT)]
		cur = (0,0)
		visited(self, cur)
		neighbors = getneighbors(cur)
		fillMaze(self, neighbors)

	def getMaze(self):
		return self.grid

