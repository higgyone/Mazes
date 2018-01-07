from Grid import Grid
from BinaryTree import BinaryTree
from Sidewinder import Sidewinder

grid = Grid(10,10)
bt = BinaryTree()
#bt.On(grid)

sw = Sidewinder()
sw.On(grid)

#print(grid)

grid.ToPng()