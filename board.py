# board.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board():

    # this is the constructor: it takes in 'grid', which is a 2d array of char
    # then scans it for the values, and creates the appropriate 'Piece' object,
    # but a blank space is given the value 'None', which is Python's version of
    # null
    # 
    # For reference: 
    #       - any method that says '__init__' is a constructor.
    #       - 'self' just references to the specific object's instance, kind of
    #           like Java's 'this'
#a = [[0 for x in range(columns)] for y in range(rows)]

    def __init__(self, grid, newBoard):
        if(newBoard == True):
            self.grid = [[None for x in range(0,8)] for y in range(0,8)]
            for i in range(0,8):
                for j in range(0,8):
                    if(grid[i][j] == '_' or grid[i][j] == '-'):
                        self.grid[i][j] = None
                    elif(grid[i][j] == 'P'):
                        self.grid[i][j] = Pawn(i, j, 'w', 'P')
                    elif(grid[i][j] == 'p'):
                        self.grid[i][j] = Pawn(i, j, 'b', 'p')
                    elif(grid[i][j] == 'N'):
                        self.grid[i][j] = Knight(i, j, 'w', 'N')
                    elif(grid[i][j] == 'n'):
                        self.grid[i][j] = Knight(i, j, 'b', 'n')
                    elif(grid[i][j] == 'B'):
                        self.grid[i][j] = Bishop(i, j, 'w', 'B')
                    elif(grid[i][j] == 'b'):
                        self.grid[i][j] = Bishop(i, j, 'b', 'b')
                    elif(grid[i][j] == 'Q'):
                        self.grid[i][j] = Queen(i, j, 'w', 'Q')
                    elif(grid[i][j] == 'q'):
                        self.grid[i][j] = Queen(i, j, 'b', 'q')
                    elif(grid[i][j] == 'K'):
                        self.grid[i][j] = King(i, j, 'w', 'K')
                    elif(grid[i][j] == 'k'):
                        self.grid[i][j] = King(i, j, 'b', 'k')
        else:
            self.grid = grid


    # takes in which color's turn it is, generates all valid moves for that player
    #
    # we will more fully implement this after we get all the move() methods in Piece.py done
    def generateMoves(self, color):
        if(color == 'b'):
            GucciMane = 1 # just here as a temporary placeholder so no errors are thrown

            # STUB - search the entire grid for black pieces, call move() for each of them
            # then check to see if what is returned are valid coordinate moves for that piece
            # (this will be more clear when you see what I wrote in Piece.py)

        if(color == 'w'):
            GucciMane = 1 # just here as a temporary placeholder so no errors are thrown
            # STUB



    def printBoard(self):

        #print(" 0 1 2 3 4 5 6 7 ")
        print("    ◘----------------◘")
        for i in range(0,8):
            print('    |', end = '')
            for j in range(0,8):
                if(self.grid[i][j] == None):
                    print(" ", end = ' ')
                else:
                    print(self.grid[i][j].id, end = ' ')
            print('|', end = '')
            print()
        print("    ◘----------------◘")