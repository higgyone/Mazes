from random import randint
import random

class BinaryTree(object):
    """description of class"""

    def On(grid):
        cells = grid.EachCell
        for cell in cells:
            neighbours = []
            if cell.north is not None:
                neighbours.append(cell.north)

            if cell.east is not None:
                neighbours.append(cell.east)

                neighbour = random.sample(neighbours,1)

                # this below may not be needed
                #index = randint(0, neighbours.count)
                #neighbour = neighbours[index]

                if neighbour is not None:
                    cell.link(neighbour)




