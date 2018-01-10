import Distances as Dist

class Cell(object):
    """description of class"""

    def __init__(self, row, column):
        """Initialiser"""
        self.row = row
        self.column = column
        self.neighbours = []

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.links = {}

    def link(self, cell, bidi=True):
        """Links the cell to this one"""
        self.links.update({cell: True})

        if bidi:
            cell.link(self, False)

        return self

    def unlink(self, cell, bidi=True):
        """Unlinks the cell from this one"""
        del self.links[cell]

        if bidi:
            cell.unlink(self, False)

        return self

    def GetLinksKeys(self):
        """Returns the linked cells"""
        return self.links.keys

    def IsLinked(self, cell):
        """Return True if the cell is linked to this one"""
        return cell in self.links

    def SetNeighbours(self):
        """Set the neighbour cells"""
        if self.north is not None:
            self.neighbours.append(self.north)
        if self.east is not None:
            self.neighbours.append(self.east)
        if self.south is not None:
            self.neighbours.append(self.south)
        if self.west is not None:
            self.neighbours.append(self.west)

    def Distances(self):
        distances = Dist.Distances(self)
        frontier = [self]
 
        while frontier:
            newFrontier = []

            for cell in frontier:
                for linked in cell.links:
                    if linked in distances.cells:
                        continue
                    
                    distances.cells[linked] = distances.cells[cell] + 1
                    #distances.SetCellDistance(linked, distances.GetCellDistance(cell) + 1)
                    newFrontier.append(linked)

            frontier = newFrontier

        return distances.cells

    


