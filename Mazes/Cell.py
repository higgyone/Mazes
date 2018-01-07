
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

        self.links.update({cell: True})

        if bidi:
            cell.link(self, False)

        return self

    def unlink(self, cell, bidi=True):
        del self.links[cell]

        if bidi:
            cell.unlink(self, False)

        return self

    def GetLinksKeys(self):
        return self.links.keys

    def IsLinked(self, cell):
        return cell in self.links

    def SetNeighbours(self):

        if self.north is not None:
            self.neighbours.append(self.north)
        if self.east is not None:
            self.neighbours.append(self.east)
        if self.south is not None:
            self.neighbours.append(self.south)
        if self.west is not None:
            self.neighbours.append(self.west)
