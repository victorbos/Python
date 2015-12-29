from graphics import *
import random


class Conway:
    blobSize = 15
    colors = ['white', 'red']

    def __init__(self, gridSize, gridInit):
        self.gridSize = gridSize
        self.grid = [[0 for i in range(gridSize)] for j in range(gridSize)]
        self.newGrid = [[0 for i in range(gridSize)] for j in range(gridSize)]
        if gridInit == 'random':
            self.randomGrid()
        else:
            self.parseInputGrid(gridInit)
        self.circles = [
            [Circle(Point(self.blobSize + i * self.blobSize, self.blobSize + j * self.blobSize), self.blobSize // 2)
             for i in range(gridSize)] for j in range(gridSize)]
        self.window = GraphWin("Conway", self.blobSize + gridSize * self.blobSize,
                               self.blobSize + gridSize * self.blobSize, autoflush=False)
        self.drawGrid(True)

    def randomGrid(self):
        self.grid = [[1 if round(random.random()) > 0.5 else 0
                      for i in range(self.gridSize)] for j in range(self.gridSize)]

    def parseInputGrid(self, gridInit):
        offset = 0
        for j, line in enumerate(gridInit.strip().splitlines()):
            offset = self.gridSize // 2 - len(line) // 2 if offset == 0 else offset
            for i, char in enumerate(line.strip()):
                self.grid[i + offset][j + offset] = 1 if char == 'o' else 0

    def nextGen(self):
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                neighbours = self.countNeighbours(i, j)
                self.newGrid[i][j] = 1 if neighbours == 3 or (neighbours == 2 and self.grid[i][j] == 1) else 0

        self.grid, self.newGrid = self.newGrid, self.grid
        cont = self.window.checkMouse() is None
        return cont

    def countNeighbours(self, x, y):
        n = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (i == x and j == y):
                    n += self.grid[i % self.gridSize][j % self.gridSize]
        return n

    def doSim(self):
        while self.nextGen():
            self.drawGrid()

    def drawGrid(self, init=False):
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                if self.grid[i][j] != self.newGrid[i][j] or init:
                    self.circles[i][j].setFill(self.colors[self.grid[i][j]])
                if init:
                    self.circles[i][j].draw(self.window)
        self.window.update()


rnd = 'random'

glider = '''
.o.
..o
ooo'''

conway = Conway(50, rnd)
conway.doSim()
