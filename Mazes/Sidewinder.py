import random
from random import randint

class Sidewinder(object):
    """description of class"""

    def On(self, grid):   
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
                #shouldCloseOut = atEasternBoundary or ((not atNorthernBoundary) and (randint(0,1) == 0))

                if shouldCloseOut:
                    member = random.choice(run)
                    
                    if member.north:
                        member.link(member.north)

                    run.clear()

                else:
                   cell.link(cell.east)

        return grid



