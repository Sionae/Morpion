from time import sleep
# import pygame
# from pygame.locals import *

from Classes import *
from Genes import *

Player1 = Player("Player 1", "O")
Player2 = Player("Player 2", "X")

winner = game(Player1, Player2, grid())
print(winner.name, "has won!")
