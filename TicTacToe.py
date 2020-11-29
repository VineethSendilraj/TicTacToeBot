import sys 
class board:
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.options = {}
        self.WinOrTie = False
        self.corners = [[0, 0], [0, 2], [2, 0], [2, 2]]

    def status(self):
        self.WinOrTie = True
        for row in range(3):
            print (self.board[row])
            print ("------------------")
            for col in range(3):
                if (self.board[row][col] == None):
                    self.WinOrTie = False


    def replace(self, row, col, player):
        self.board[row-1][col-1] = player

    def clear(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    @classmethod
    def convertToNumber (cls, cell, player):
        if (cell == player):
            return 3
        elif cell != None :
            return -1
        return 0

    def GetEmptyCell(self, operationMethod, number):
        if (operationMethod == "Row"):
            return [number, [col for col in range(3) if self.board[number][col] == None][0]]
        if (operationMethod == "Col"):
            return [[row for row in range(3) if self.board[row][number] == None][0], number]
        if (operationMethod == "Diag" and number == 1):
            row = [row for row in range(3) if self.board[row][row] == None][0]
            return [row, row]    
        if (operationMethod == "Diag" and number == 2):
            row = [row for row in range(3) if self.board[row][2-row] == None][0]
            return [row, 2-row]

    @classmethod
    def simpleCheck(cls, cells, player ):
        nCount = sum(board.convertToNumber(cells[c], player) for c in range(3))
        return nCount
    
    def addRank (self, ranking, operationMethod, number, player):
        if (ranking == 9 ):
            self.WinOrTie = True
            print('Player ' + player + ' wins' )
            return (ranking , True)
        if (ranking == -3 ):
            self.WinOrTie = True
            print('You win')
            return (ranking , True)
        if (ranking == 5 or ranking == 1):
            return (ranking,False)
        emptyCell = self.GetEmptyCell(operationMethod, number)
        self.options[ranking] = emptyCell
 
        return (ranking,False)

    def check(self, player):
        self.options.clear()
        for row in range(3): # Row Checking
            ranking = board.simpleCheck(self.board[row], player)
            if ranking == -2:
                newranking = ranking + 6
                self.addRank(newranking,"Row", row, player)
            else:
                self.addRank(ranking,"Row", row, player)
        for col in range(3): # Row Checking
            ranking = board.simpleCheck([self.board[row][col] for row in range(3)], player)
            if ranking == -2:
                newranking = ranking + 6
                self.addRank(newranking,"Col", col, player)
            else:
                self.addRank(ranking,"Col", col, player)
        
        ranking = board.simpleCheck([self.board[row][row] for row in range(3)], player)
        if ranking == -2:
            newranking = ranking + 6
            self.addRank(newranking,"Diag", 1, player)
        else:
            self.addRank(ranking,"Diag", 1, player)

        ranking = board.simpleCheck([self.board[row][2-row] for row in range(3)], player)
        if ranking == -2:
            newranking = ranking + 6
            self.addRank(newranking,"Diag", 2, player)
        else:
            self.addRank(ranking,"Diag", 2, player)
        if ( self.WinOrTie == True):
            return "WinOrTie"
        self.maxOption(player)
        return "Move"

    def firstMove(self, player):
        for x in range(4):
            if self.board[self.corners[x][0]][self.corners[x][1]] != None:
                self.replace(2, 2, player)
            else:
                for x in range(4):
                    if self.corners[x] == None:
                        self.replace(self.corners[x][0], self.corners[x][1], player)
                        
    def maxOption(self,player):
        if (len(self.options) == 0):
            return
        maxValue = max(self.options, key=lambda x: abs(x))
        rowCol = self.options[maxValue]
        self.board[rowCol[0]][rowCol[1]] = player