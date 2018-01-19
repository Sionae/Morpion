from Classes import *
# from Genes import *

Player1 = Player("Samuel", "O")
Player2 = Player("Papa", "X")

Running = True
while Running:
	winner, Running = game(Player1, Player2, grid())
	if winner == Player1 or winner == Player2:
		print(winner.name, "has won!")
	else:
		print("Tie!")

	sleep(2)

pygame.quit()
