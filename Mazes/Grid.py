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
        """Return the to string of the grid for console output"""
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
        """Create a .png of the grid"""
        imgWidth = cellSize * self.columnCount
        imgHeight = cellSize * self.rowCount

        background = 'white'
        wall = 'black'

        img = Image.new('RGB',(imgWidth + 1,imgHeight + 1),background)
        draw = ImageDraw.Draw(img)

        modes = ['background', 'walls']

        for mode in modes:
            # need to reset cells for each mode otherwise will not work on second mode pass
            cells = self.EachCell()
            for cell in cells:
                x1 = cell.column * cellSize
                y1 = cell.row * cellSize
                x2 = (cell.column + 1) * cellSize
                y2 = (cell.row + 1) * cellSize

                if mode == 'background':
                    colour = self.BackgroundColourFor(cell)
                    if colour is not None:
                        draw.rectangle((x1, y1, x2, y2), colour, colour)
                else:
                    if cell.north is None:
                        draw.line((x1, y1, x2, y1), fill = wall, width = lineWidth)
                    if cell.west is None:
                        draw.line((x1, y1, x1, y2), fill = wall, width = lineWidth)
                    if not cell.IsLinked(cell.east):
                        draw.line((x2, y1, x2, y2), fill = wall, width = lineWidth)
                    if not cell.IsLinked(cell.south):
                        draw.line((x1, y2, x2, y2), fill = wall, width = lineWidth)

        img.show()


    def PrepareGrid(self):
        """Setup the initial grid that the maze is made from """
        arr=[]
        for i in range(0,self.rowCount):
            x=[]
            for j in range(0,self.columnCount):

                x.append(Cell(i,j))
            
            arr.append(x)
        return arr

    def ConfigureCells(self):
        """configure the cells to know what cells are linked to which cell 
        North, South, East and West"""
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
        """Get a set cell in the grid. Retuns none if not in the grid"""
        if 0 <= row < self.rowCount:
            if 0 <= column < self.columnCount:
                return self.grid[row][column]

        return None

    def GetRandomCell(self):
        """Get a random cell from the grid"""
        row = randint(0,self.rowCount)
        col = randint(0, self.columnCount)

        return self.grid[row][col]

    def GetGridSize(self):
        """Get the grid area"""
        return self.rowCount * self.columnCount

    def EachRow(self):
        """iterator for getting each row in the grid"""
        for row in self.grid:
            yield row

    def EachCell(self):
        """Iterator to iterate through each cell in the grid"""
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    yield cell

    def ContentsOf(self, cell):
        """Overridable to return the contents of the cell. Returns None unless overridden"""
        return " "

    def BackgroundColourFor(self, cell):
        """Overridable to return cell background colour. Returns None unless overriden"""
        return None
