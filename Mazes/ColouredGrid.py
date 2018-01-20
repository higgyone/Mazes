from Grid import Grid
from PIL import Image, ImageDraw
from Distances import Distances

class ColouredGrid(Grid):
    """Colours the grid depending on how far cells are from the maximum cell distance"""

    def __init__(self, rows, columns):
         super().__init__(rows, columns)
         self.distances = None
         self.farthest = None
         self.maximum = None

    def Distances(self, Distances):
        """Get the distances furthest and maximum from the Distances object"""
        self.distances = Distances
        self.farthest, self.maximum = self.distances.Max()

    def BackgroundColourFor(self, cell):
        """get the intenstiy RGB values corresponding to distance the cell is from the maximum distance in maze"""
        distance = self.distances.cells[cell]

        if distance is None:
            return None

        intensity = float((self.maximum - distance))/self.maximum
        dark = int(255 * intensity)
        brightness = 128 + (int(127 * intensity))
        
        return dark, brightness, dark

