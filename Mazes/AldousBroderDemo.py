from Grid import Grid
from Algorithms.AldousBroder import AldousBroder

grid = Grid(25, 25)
ab = AldousBroder()
ab.On(grid)

grid.ToPng()


