from Functions import *

class Player:
    """Initializing Player class"""

    def __init__(self, name, fig):
        """fig corresponds to the figure to place, i.e. cross or circle"""
        self.name = name
        self.win = False
        self.fig = fig

    def move(self, move, grid):
        """move corresponds to a [row, col] pos"""

        if grid[move[0]][move[1]] == None:
            grid[move[0]][move[1]] = self.fig
            return True, grid

        else:
            #The place is already taken
            return False, grid

    def won(self, grid):
        """Winning conditions"""
        diagTopLeft = grid[0][0] == self.fig and grid[1][1] == self.fig and grid[2][2] == self.fig
        diagBotLeft = grid[2][0] == self.fig and grid[1][1] == self.fig and grid[0][2] == self.fig

        if diagBotLeft or diagTopLeft:
            self.win = True
            return self.win

        self.rows = grid
        for row in self.rows:
            if row == [self.fig, self.fig, self.fig]:
                self.win = True
                return self.win

        self.cols = []

        for x in range(0, len(self.rows)):
            tempcols = []
            for row in self.rows:
                tempcols.append(row[x])

            self.cols.append(tempcols)

        for col in self.cols:
            if col == [self.fig, self.fig, self.fig]:
                self.win = True
                return self.win

        return False
