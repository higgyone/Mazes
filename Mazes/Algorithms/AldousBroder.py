import random

class AldousBroder(object):
    """Aldous & Broder implementation"""
    
    def On(self, grid):
        """ Run the Aldous & Broder algorithm over the grid to get the maze"""
        cell = grid.GetRandomCell()
        unvisited = grid.GetGridSize() - 1

        while unvisited > 0:
            
            if not cell.neighbours:
                cell.SetNeighbours()

            neighbour = random.choice(cell.neighbours)

            if not neighbour.links:
                cell.link(neighbour)
                unvisited -= 1

            cell = neighbour

        return grid


