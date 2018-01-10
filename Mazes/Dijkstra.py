from DistanceGrid import DistanceGrid
from BinaryTree import BinaryTree

grid = DistanceGrid(10,10)
bt = BinaryTree()
bt.On(grid)

start = grid.GetCell(0,0)

distances = start.Distances()

grid.distances = distances

print(grid)




