from DistanceGrid import DistanceGrid
from Algorithms.BinaryTree import BinaryTree

"""Python file to run Dijkstra and get distances from start cell to selected cell"""

grid = DistanceGrid(10,10)
bt = BinaryTree()
bt.On(grid)

start = grid.GetCell(0,0)

distances = start.Distances()

grid.distances = distances.cells

print(grid)

grid.distances = distances.PathTo(grid.GetCell(grid.rowCount -1, 0)).cells

print(grid)




