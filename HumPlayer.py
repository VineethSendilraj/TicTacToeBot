from TicTacToe import board

class HumPlayer:
    def __init__(self,board):
        self.TicBoard = board

    def HumanPlayerMove(self, player):
        print ("")
        self.TicBoard.status()
        print ("")
        print ( "Its your turn ")
        row = input("Enter row:")
        col = input ("Enter col:")
        self.TicBoard.replace(int(row), int(col), player)
        print ("")
