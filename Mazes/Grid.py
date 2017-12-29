from random import randint
from Cell import Cell


class Grid(object):
    """description of class"""

    def __init__(self, rows, columns):
        self.rowCount = rows
        self.columnCount = columns
        self.grid = self.PrepareGrid()

    def PrepareGrid(self):
        arr=[]
        for i in range(0,self.rowCount):
            x=[]
            for j in range(0,self.columnCount):
                x.append(Cell(i,j))
                arr.append(x)
        return arr

    def ConfigureCells(self):
        """ fix this to use EachCell method... easier than this """
        for row in self.rowCount:
            for col in self.columnCount:
                self.grid[row][col].north = self.grid[row - 1][col]
                self.grid[row][col].east = self.grid[row][col + 1]
                self.grid[row][col].south = self.grid[row + 1][col]
                self.grid[row][col].west = self.grid[row][col - 1]

    def GetCell(self, row, column):
        if 0 < row < self.rowCount - 1:
            if 0 < column < self.columnCount - 1:
                return self.grid[row][column]

        return None

    def GetRandomCell(self):
        row = randint(0,self.rowCount)
        col = randint(self.grid[row].count)

        return self.grid[row][col]

    def GetGridSize(self):
        return self.rowCount * self.columnCount

    def EachRow(self):
        for row in self.grid:
            yield row

    def EachCell(self):
        for row in self.grid:
            for cell in self.grid[row]:
                if cell is not None:
                    yield cell

