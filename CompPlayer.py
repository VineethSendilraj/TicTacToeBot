from TicTacToe import board

class CompPlayer:
    def __init__(self, board):
        self.TicBoard = board

    def FirstMove(self, player):
        print ("Computer Move")
        self.TicBoard.firstMove(player)

    def ComputerPlayerMove(self, player):
        self.TicBoard.status()
        print ("")
        print ("Computer Move")
        self.TicBoard.check(player)

    def FirstMoveStart(self):
        self.TicBoard.replace(2, 2, 'X')