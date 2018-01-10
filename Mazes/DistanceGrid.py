from Grid import Grid
import numpy as np

class DistanceGrid(Grid):
    """description of class"""

    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        self.distances = None


    def ContentsOf(self, cell):
        if self.distances and cell in self.distances:
            dist = self.distances[cell]
            num = np.base_repr(dist, 36)
            return num
        else:
            return super().ContentsOf(cell)
            

    
            


