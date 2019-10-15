from game import TicTacToe
from learning import learning

gme = TicTacToe(True)
player1 = learning()
player2 = learning()
gme.startTraining(player1,player2)
gme.train(100000)
gme.saveStates()