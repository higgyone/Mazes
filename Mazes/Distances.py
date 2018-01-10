class Distances(object):
    """description of class"""

    def __init__(self, root):
        self.root = root
        self.cells = {}

        """Root cell is distance 0"""
        self.cells[root] = 0

    def GetCellDistance(self, cell):
        """Gets the cell distance from the root cell"""
        dist = self.cells.get(cell)
        return dist

    def SetCellDistance(self, cell, distance):
        """Sets the cell distance from the root cell"""
        self.cells[cell] = distance

    def GetCellsPresent(self):
        """Returns a list of the cells present"""
        return self.cells.keys

