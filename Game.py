from TicTacToe import board
from CompPlayer import CompPlayer
from HumPlayer import HumPlayer

class Game:
    def __init__(self):
        self.TicBoard = board()
        self.Human = HumPlayer(self.TicBoard)
        self.Computer = CompPlayer(self.TicBoard)
        self.playagain = True
    
    def start(self):
        self.TicBoard.clear()
        print("")
        print('Tic Tac Toe')
        print('By: Vineeth Sendilraj')
        print("")
        answer = input('Do you want to go first:')
        if answer == 'Yes' or answer == 'yes':
            self.Human.HumanPlayerMove('X')
            self.Computer.FirstMove('O')
            while(self.TicBoard.WinOrTie == False):
                self.Human.HumanPlayerMove('X')
                self.Computer.ComputerPlayerMove('O')

        elif answer == 'No' or answer == 'no':
            self.Computer.FirstMoveStart()
            while(self.TicBoard.WinOrTie == False):
                self.Human.HumanPlayerMove('O')
                self.Computer.ComputerPlayerMove('X')
        else:
            print('You can only answer Yes or No')
            self.start()

    def playAgain(self):
        answer = input('Do you want to play again? ')
        if answer == 'Yes' or answer == 'yes':
            self.start()
        elif answer == 'No' or answer == 'no':
            print('To play again run the code again')
            self.playagain = False
        else:
            print('You can only answer Yes or No')
            self.playAgain()

TicTacToeGame = Game()

TicTacToeGame.start()
TicTacToeGame.playAgain()
while (TicTacToeGame.playagain == True):
    TicTacToeGame.playAgain()