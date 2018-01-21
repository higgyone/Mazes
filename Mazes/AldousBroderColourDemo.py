from ColouredGrid import ColouredGrid
from Algorithms.AldousBroder import AldousBroder

for i in range(0,6):
    grid = ColouredGrid(25, 25)
    ab = AldousBroder()
    ab.On(grid)

    middle = grid.GetCell(int(grid.rowCount/2), int(grid.columnCount/2))
    grid.Distances(middle.Distances())

    grid.ToPng()


