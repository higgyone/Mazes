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

    def PathTo(self, goal):
        """Figures out the path to goal from the original starting cell"""
        current = goal

        breadcrumbs = Distances(self.root)
        
        breadcrumbs.cells[current] = self.cells[current]

        while current != self.root:
            for neighbour in current.links:
                if self.cells[neighbour] < self.cells[current]:
                    breadcrumbs.cells[neighbour] = self.cells[neighbour]
                    current = neighbour
                    break

        return breadcrumbs

    def Max(self):
        """Get the furthest cell and its distance from the root cell"""
        maxDistance = 0
        maxCell = self.root

        for cell, distance in self.cells.items():
            if distance > maxDistance:
                maxCell = cell
                maxDistance = distance

        return maxCell, maxDistance


