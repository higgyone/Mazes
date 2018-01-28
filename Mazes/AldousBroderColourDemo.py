from ColouredGrid import ColouredGrid
from Algorithms.AldousBroder import AldousBroder

"""
Run the Aldous Broder colour demo 5 times
"""

for i in range(0,5):
    grid = ColouredGrid(25, 25)
    ab = AldousBroder()
    ab.On(grid)

    middle = grid.GetCell(int(grid.rowCount/2), int(grid.columnCount/2))
    grid.Distances(middle.Distances())

    grid.ToPng()


