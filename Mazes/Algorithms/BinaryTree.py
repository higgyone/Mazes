from random import randint
import random

class BinaryTree(object):
    """description of class"""

    def On(self, grid):
        cells = grid.EachCell()
        for cell in cells:
            neighbours = []
            if cell.north is not None:
                neighbours.append(cell.north)

            if cell.east is not None:
                neighbours.append(cell.east)

            # check the list is populated otherwise random.choice throws index error
            if neighbours:
                # random.choice returns one object from the list whereas random.sample returns a list
                neighbour = random.choice(neighbours)
                cell.link(neighbour)


