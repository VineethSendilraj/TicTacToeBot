class board:
    def __init__(self):
        self.key = {9:'Player 1 Wins', 6:'Potential win for player 1', 5:'Potential Block for player 1', 3:'First player 1 chip in the row',\
        -4:'Player 2 Wins', -3:'Potential win for player 2', -2:'Potential Block for player 1', -1:'First player 2 chip in the row',\
        0:'No coins have been placed in this Row/Column/Diagnal', 2:'Lane already contains both players Chips'}
        self.options = {}
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.j = 0

    def status(self):
        return self.board

    def replace(self, row, col, player):
        self.board[row-1][col-1] = player
    
    def maxOption(self):
        maxValue= max(self.options, key=lambda x: abs(x))
        return self.options[maxValue]

    def keycheck(self, sum, player):
        if sum == 6 and player == 'X':
            return self.key[sum]
        elif sum == 6 and player == 'O': 
            return self.key[sum-8]
        elif sum == -2 and player == 'O':
            return self.key[sum-1]
        elif sum == -2 and player == 'X':
            return self.key[sum+7]
        elif sum == -3:
            return self.key[sum-1]
        else: return self.key[sum]

    def check(self, player):
        self.options.clear()
        sum = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 'X':
                    sum += 3
                elif self.board[row][col] != None:
                    sum -= 1
            if sum == 5 or sum == 1: 
                self.j+=1
            else: self.options.__setitem__(sum, self.keycheck(sum, player))
        sum = 0
        for col in range(3):
            for row in range(3): 
                if self.board[row][col] == 'X':
                    sum += 3 
                elif self.board[row][col] != None:
                    sum -= 1
            if sum == 5 or sum == 1: 
                self.j+=1
            else: self.options.__setitem__(sum, self.keycheck(sum, player))
        sum = 0
        for row in range(3): 
            if self.board[row][row] == 'X':
                sum += 3
            elif self.board[row][row] != None:
                sum -= 1
        if sum == 5 or sum == 1: 
            self.j+=1
        else: self.options.__setitem__(sum, self.keycheck(sum, player))
        sum = 0
        for row in range(3): 
            if self.board[row][2-row] == 'X':
                sum += 3
            elif self.board[row][2-row] != None:
                sum -= 1
        if sum == 5 or sum == 1: 
            self.j+=1
        else: self.options.__setitem__(sum, self.keycheck(sum, player))
        return(self.maxOption())
    


    def check(self, player, checker):
        self.options.clear()

        for row in range(3): # Row Checking
            Ncount = sum(1 for col in range(3) if self.board[row][col] == player)# How many times the players coin is in a row
            if Ncount == 3:# Player Win condition
                return (True, 'Won on Row' + " " + str(row+1))
            elif Ncount == 2: 
                for c in range(3):  # If the count is 2 and the is a None square in the row it will print Potential Winner
                    if self.board[row][c] == None:
                        if player == checker:
                            self.options.__setitem__(2,(row,c))
                        else: 
                            self.options.__setitem__(1,(row,c))

        for col in range(3): # Column Checking
            Ncount = sum(1 for row in range(3) if self.board[row][col] == player) # How many times the players coin is in a column
            if Ncount == 3: # Player Win condition
                return (True, 'Won on Column' + " " + str(col+1))
            elif Ncount == 2: 
                for c in range(3): 
                    if self.board[c][col] == None: # If the count is 2 and the is a None square in the row it will print Potential Winner/Blocker
                        if player == checker: 
                            self.options.__setitem__(2, (c,col))
                        else: 
                            self.options.__setitem__(1,(c,col))



        Ncount = sum(1 for row in range(3) if self.board[row][row] == player) # Diagonal 1 Checking
        if Ncount == 3:
            return (True, 'Won on Diagonal 1')
        elif Ncount == 2: 
            for row in range(3): 
                if self.board[row][row] == None: # If the count is 2 and the is a None square in the row it will print Potential Winner/Blocker
                    if player == checker:
                        self.options.__setitem__(2,(row,row))   
                    else:
                        self.options.__setitem__(1,(row,row))



        Ncount = sum(1 for row in range(3) if self.board[row][2-row] == player) # Diagnal 2 Checking
        if Ncount == 3:
            return (True, 'Won on Diagonal 2')
        elif Ncount == 2: 
            for row in range(3): 
                if self.board[row][2-row] == None: # If the count is 2 and the is a None square in the row it will print Potential Winner/Blocker
                    if player == checker:
                        self.options.__setitem__(2,(row,2-row))   
                    else:
                        self.options.__setitem__(1,(row,2-row))

        return self.maxOption(player)
        
# TicBoard = board()
# TicBoard.replace(3, 1, 'O')
# TicBoard.replace(2, 1, 'O')


# print(TicBoard.check('X'))
# print(TicBoard.options)
