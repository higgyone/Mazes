from ColouredGrid import ColouredGrid
from Algorithms.BinaryTree import BinaryTree
from Algorithms.Sidewinder import Sidewinder

"""Python file to run coloured grids"""

grid = ColouredGrid(25, 25)
#bt = BinaryTree()
#bt.On(grid)

sw = Sidewinder().On(grid)

start = grid.GetCell(int(grid.rowCount/2) , int(grid.columnCount/2))

grid.Distances(start.Distances())

grid.ToPng()
