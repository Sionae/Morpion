def grid():
    return [[None, None, None], [None, None, None], [None, None, None]]

def print_grid(grid):
    for line in grid:
        print(line)

def game(Player1, Player2, grid):
    playerTurn = Player1

    while 1:
        print_grid(grid)
        row = int(input("Row position : "))
        col = int(input("Column position : "))

        correctPlay, grid = playerTurn.move([row, col], grid)
        while not correctPlay:
            row = int(input("Row position : "))
            col = int(input("Column position : "))
            correctPlay, grid = playerTurn.move([row, col], grid)

        if playerTurn.won(grid):
            return playerTurn

        if playerTurn == Player1:
            playerTurn = Player2
        else:
            playerTurn = Player1
