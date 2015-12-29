from graphics import *
import random

class Conway:
    blobSize = 20

    def __init__(self, gridSize, gridInit):
        self.gridSize = gridSize
        self.grid = [[0 for i in range(gridSize)] for j in range(gridSize)]
        self.newGrid = [[0 for i in range(gridSize)] for j in range(gridSize)]
        if gridInit == 'random':
            self.randomGrid()
        else:
            self.parseInputGrid(gridInit)
        self.circles = [[Circle(Point(self.blobSize + i * self.blobSize, self.blobSize + j * self.blobSize), self.blobSize // 2) for i in range(gridSize)] for j in range(gridSize)]
        self.window = GraphWin("Conway", self.blobSize + gridSize * self.blobSize, self.blobSize + gridSize * self.blobSize, autoflush=False)
        self.drawGrid(True)

    def randomGrid(self):
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                self.grid[i][j] = 1 if round(random.random()) > 0.5 else 0

    def parseInputGrid(self, gridInit):
        offset = 0
        for j, line in enumerate(gridInit.strip().splitlines()):
            offset = self.gridSize // 2 - len(line) // 2 if offset == 0 else offset
            for i, char in enumerate(line.strip()):
                self.grid[i+offset][j+offset] = 1 if char == 'o' else 0

    def printGrid(self):
        print('-' * self.gridSize)
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                print('O' if self.grid[i][j] == 1 else '.', end='')
            print('\n')

    def nextGen(self):
        allDead = True
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                neighbours = self.countNeighbours(i, j)
                if neighbours == 2 and self.grid[i][j] == 1:
                    self.newGrid[i][j] = 1
                elif neighbours == 3:
                    self.newGrid[i][j] = 1
                else:
                    self.newGrid[i][j] = 0
                allDead = allDead and self.newGrid[i][j] == 0
        self.grid, self.newGrid = self.newGrid, self.grid
        cont = not allDead and self.window.checkMouse() is None
        return cont

    def countNeighbours(self, x, y):
        x1m = (x - 1) % self.gridSize
        x1p = (x + 1) % self.gridSize
        y1m = (y - 1) % self.gridSize
        y1p = (y + 1) % self.gridSize
        neighbours = self.grid[x1m][y1m] + self.grid[x][y1m] + self.grid[x1p][y1m] + \
                     self.grid[x1m][y] + self.grid[x1p][y] + \
                     self.grid[x1m][y1p] + self.grid[x][y1p] + self.grid[x1p][y1p]

        return neighbours

    def doSim(self):
        while self.nextGen():
            self.drawGrid()

    def drawGrid(self, doDraw = False):
        for i in range(0, self.gridSize):
            for j in range(0, self.gridSize):
                if self.grid[i][j] == 1:
                    self.circles[i][j].setFill('red')
                else:
                    self.circles[i][j].setFill('white')
                if doDraw:
                    self.circles[i][j].draw(self.window)
        self.window.update()



glider = '''
.o.
..o
ooo'''


conway = Conway(50, 'random')
conway.doSim()
