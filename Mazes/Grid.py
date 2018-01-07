from random import randint
from Cell import Cell


class Grid(object):
    """description of class"""

    def __init__(self, rows, columns):
        self.rowCount = rows
        self.columnCount = columns
        self.grid = self.PrepareGrid()
        self.ConfigureCells()

    def __str__(self):
        output = "+" + "---+" * self.columnCount + "\n"

        er = self.EachRow()
        for row in er:
            top = "|"
            bottom = "+"

            for cell in row:
                if cell is None:
                    cell = Cell(-1,-1)

                body = "   "
                eastBoundary = " " if cell.IsLinked(cell.east) else "|"

                top += body + eastBoundary

                southBoundary = "   " if cell.IsLinked(cell.south) else "..."
                corner = "+"
                bottom += southBoundary + corner

            output += top + "\n"
            output += bottom + "\n"

        return output



    def PrepareGrid(self):
        arr=[]
        for i in range(0,self.rowCount):
            x=[]
            for j in range(0,self.columnCount):

                x.append(Cell(i,j))
            
            arr.append(x)
        return arr

    def ConfigureCells(self):
        cells = self.EachCell()
        for cell in cells:
            row = cell.row
            col = cell.column

            rowMinusOne = row -1
            colMinusOne = col - 1

            rowPlusOne = row + 1
            colPlusOne = col + 1

            if rowMinusOne >= 0:
                cellNorth = self.grid[row-1][col]
                cell.north = cellNorth
            
            if colPlusOne < self.columnCount:
                cellEast = self.grid[row][col + 1]
                cell.east = cellEast

            if rowPlusOne < self.rowCount:
                cellSouth = self.grid[row + 1][col]
                cell.south = cellSouth

            if colMinusOne >= 0:
                cellWest = self.grid[row][col - 1]
                cell.west = cellWest                   
            

    def GetCell(self, row, column):
        if 0 <= row < self.rowCount - 1:
            if 0 <= column < self.columnCount - 1:
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
            for cell in row:
                if cell is not None:
                    yield cell


