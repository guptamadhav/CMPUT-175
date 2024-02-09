#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |          
        board_n = self.board[:]  
        for i in range(self.size):
            board_n[i] = [" " if j == 0 else j for j in board_n[i]]
        print('    0   1   2')
        for i in range(self.size):
            print(f'{i}  {board_n[i][0]} | {board_n[i][1]} | {board_n[i][2]}')
            if i < (self.size-1):
                print('  '+'-'*11)
        

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        # TO DO: delete pass and complete method
        
        if self.board[row][col] > 0:
            return False

        return True
    
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        # TO DO: delete pass and complete method
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True

        return False

    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        # TO DO: delete pass and complete method
        for i in self.board:
            for j in i:
                if j != 0:
                    return True
                else:
                    return False
                    break
        
        return False
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass and complete method
        win = False
        for i in range(self.size):
            if (self.board[i][0] + self.board[i][1] + self.board[i][2]) == 15:
                win = True
                break
            elif (self.board[0][i] + self.board[1][i] + self.board[2][i]) == 15:
                win = True
                break
            elif (self.board[0][0] + self.board[1][1] + self.board[2][2]) == 15 or (self.board[0][2] + self.board[1][1] + self.board[2][0]) == 15:
                win = True
                break
        return win
     

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    myBoard.drawBoard()
    # does the empty board display properly?


    # assign a number to an empty square and display
    
    # try to assign a number to a non-empty square. What happens?
    
    # check if the board has a winner. Should there be a winner after only 1 entry?
    
    # check if the board is full. Should it be full after only 1 entry?
    
    # add values to the board so that any line adds up to 15. Display
    
    # check if the board has a winner
    
    # check if the board is full
    
    # write additional tests, as needed
    # status = myBoard.update(0, 0, 7)
    # status = myBoard.update(1, 0, 8)
    # status = myBoard.update(2, 0, 9)
    # status = myBoard.update(0, 1, 4)
    # status = myBoard.update(1, 1, 5)
    # status = myBoard.update(2, 1, 3)
    # status = myBoard.update(0, 2, 2)
    # status = myBoard.update(1, 2, 1)
    # status = myBoard.update(2, 2, 4)
    
    # myBoard.drawBoard()
    # print(myBoard.boardFull())
    # print(myBoard.isWinner())