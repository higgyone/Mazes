from DistanceGrid import DistanceGrid
from BinaryTree import BinaryTree

grid = DistanceGrid(10,10)
bt = BinaryTree()
bt.On(grid)

start = grid.GetCell(0,0)

distances = start.Distances()
grid.distances = distances.cells

# Get furthest cell from root
newStart, distance = distances.Max()

# Then get furthest cell from furthest cell from root
newDistances = newStart.Distances()
goal, distance = newDistances.Max()

# fid the path between the furthest 2 cells
grid.distances = newDistances.PathTo(goal).cells

print(grid)

