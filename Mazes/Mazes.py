from Grid import Grid
from Algorithms.BinaryTree import BinaryTree
from Algorithms.Sidewinder import Sidewinder

"""Python file to basic grid algorithms"""

grid = Grid(10,10)
#bt = BinaryTree()
#bt.On(grid)

#print(grid)

sw = Sidewinder()
sw.On(grid)

##print(grid)

grid.ToPng()