import random
from random import randint

class Sidewinder(object):
    """description of class"""

    def On(self, grid):   
        """ Runs the sidewinder algorithm to create a grid and return it"""

        er = grid.EachRow()
        for row in er:
            run = []

            for cell in row:
                run.append(cell)

                atEasternBoundary = (cell.east == None)
                atNorthernBoundary = (cell.north == None)

                ht = randint(0,1)
                htb = ht == 0
                nanb = not atNorthernBoundary

                shouldCloseOut = atEasternBoundary or (nanb and htb)

                if shouldCloseOut:
                    member = random.choice(run)
                    
                    if member.north:
                        member.link(member.north)

                    run.clear()

                else:
                   cell.link(cell.east)

        return grid



