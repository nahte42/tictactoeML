from game import TicTacToe, Human, RandomPlayer
from learning import learning

gme = TicTacToe()
player1 = Human()
player2 = learning()
gme.startGame(player1,player2)
gme.reset()
gme.render()
