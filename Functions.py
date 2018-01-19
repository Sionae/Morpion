from random import randint
import pygame
from pygame.locals import *
from time import sleep

def grid():
    return [[None, None, None], [None, None, None], [None, None, None]]


def buttonPosOnGrid(grid, buttonPos, windowSize):
    bPx = buttonPos[0] /windowSize[0]
    bPy = buttonPos[1]/windowSize[1]

    if bPx < 1/3:
        #First column
        col = 0
    elif bPx >= 1/3 and bPx < 2/3:
        #Second column
        col = 1
    else:
        #Third column
        col = 2

    if bPy < 1/3:
        #First row
        row = 0
    elif bPy >= 1/3 and bPy < 2/3:
        #Second row
        row = 1
    else:
        #Third row
        row = 2

    return row, col


def correctPlay(grid, buttonPos, windowSize):
    row, col = buttonPosOnGrid(grid, buttonPos, windowSize)
    if grid[row][col] == None:
        return True
    else:
        return False




def showFig(grid, window, buttonPos, windowSize, t):
    """t stands for the type of figure to draw (X or O)"""
    row, col = buttonPosOnGrid(grid, buttonPos, windowSize)

    if t == "X":
        #Draw X
        pygame.draw.line(window, (0, 255, 0), (col*windowSize[0]/3 + windowSize[0]//8,
                                                row*windowSize[1]/3 + windowSize[1]//8),
                                                ((col+1)*windowSize[0]/3 - windowSize[0]//8,
                                                ((row+1)*windowSize[1]/3 - windowSize[1]//8)),
                                                5)
        pygame.draw.line(window, (0, 255, 0), (col*windowSize[0]/3 + windowSize[0]//8,(row+1)*windowSize[1]/3 - windowSize[1]//8),
                                                ((col+1)*windowSize[0]/3 - windowSize[0]//8,
                                                (row*windowSize[1]/3 + windowSize[1]//8)),
                                                5)

    elif t == "O" :
        #Draw O
        middle = (int((col*windowSize[0]/3 + (col+1)*windowSize[1]/3)/2), int((row*windowSize[0]/3 + (row+1)*windowSize[1]/3)//2))
        pygame.draw.circle(window, (255, 0, 0), middle, min(windowSize[0], windowSize[1])//8, 5)

    return [row, col]


def Draw(grid):
    count = 0
    for row in range(0, len(grid)):
        for cols in range(0, len(grid)):
            if grid[row][cols] == None:
                return False


    return True




def showGrid(window, windowSize):
    LineX = 0
    LineY = 0

    #Drawing lines for rows
    pygame.draw.line(window, (0, 0, 0),
                    (LineX, LineY+windowSize[1]/3),
                    (windowSize[0], LineY+windowSize[1]/3), 5)
    pygame.draw.line(window, (0, 0, 0),
                    (LineX, LineY+2*windowSize[1]/3),
                    (windowSize[0], LineY+2*windowSize[1]/3), 5)


    #Drawing lines for columns
    pygame.draw.line(window, (0, 0, 0),
                    (LineX+windowSize[0]/3, LineY),
                    (LineX+windowSize[0]/3, windowSize[1]), 5)
    pygame.draw.line(window, (0, 0, 0),
                    (LineX+2*windowSize[0]/3, LineY),
                    (LineX+2*windowSize[0]/3, windowSize[1]), 5)





def game(Player1, Player2, grid):
    playerTurn = Player1

    pygame.init()
    window = pygame.display.set_mode((800, 800), RESIZABLE)
    windowSize = pygame.display.get_surface().get_size()
    window.fill((255, 255, 255))

    showGrid(window, windowSize)
    pygame.display.flip()

    c = True
    while c:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                c = False
                return False, False
                break
            elif event.type == MOUSEBUTTONDOWN:
                buttonPos = event.pos
                Playcorrect = correctPlay(grid, buttonPos, windowSize)
                if Playcorrect:
                    movex, movey = showFig(grid, window, buttonPos, windowSize, playerTurn.fig)
                    fig = playerTurn.move([movex, movey], grid)
                    grid[movex][movey] = fig

                    pygame.display.flip()

                    if playerTurn.won(grid):
                        return playerTurn, True
                    elif Draw(grid):
                        return False, True

                    if playerTurn == Player1:
                        playerTurn = Player2
                    else:
                        playerTurn = Player1
