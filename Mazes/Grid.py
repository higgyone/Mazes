from random import randint
from Cell import Cell

from PIL import Image, ImageDraw


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

                contentOfCell = self.ContentsOf(cell)
                body = " " + contentOfCell + " "
                eastBoundary = " " if cell.IsLinked(cell.east) else "|"

                top += body + eastBoundary

                southBoundary = "   " if cell.IsLinked(cell.south) else "..."
                corner = "+"
                bottom += southBoundary + corner

            output += top + "\n"
            output += bottom + "\n"

        return output

    def ToPng(self, cellSize = 50, lineWidth = 5):
        imgWidth = cellSize * self.columnCount
        imgHeight = cellSize * self.rowCount

        img = Image.new('1',(imgWidth + 1,imgHeight + 1),0)
        draw = ImageDraw.Draw(img)

        cells = self.EachCell()
        for cell in cells:
            x1 = cell.column * cellSize
            y1 = cell.row * cellSize
            x2 = (cell.column + 1) * cellSize
            y2 = (cell.row + 1) * cellSize

            if cell.north is None:
                draw.line((x1,y1,x2,y1), fill = 128, width = lineWidth)
            if cell.west is None:
                draw.line((x1,y1,x1,y2), fill = 128, width = lineWidth)
            if not cell.IsLinked(cell.east):
                draw.line((x2,y1,x2,y2), fill = 128, width = lineWidth)
            if not cell.IsLinked(cell.south):
                draw.line((x1,y2,x2,y2), fill = 128, width = lineWidth)

        img.show()


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
        if 0 <= row < self.rowCount:
            if 0 <= column < self.columnCount:
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

    def ContentsOf(self, cell):
        return " "
