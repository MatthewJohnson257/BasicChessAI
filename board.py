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
    def __init__(self, grid):
        for i in grid:
            for j in grid[0]:
                if(grid[i][j] == '-'):
                    grid[i][j] = None
                elif(grid[i][j] == 'P'):
                    grid[i][j] = Pawn(i, j, 'w')
                elif(grid[i][j] == 'p'):
                    grid[i][j] = Pawn(i, j, 'b')
                elif(grid[i][j] == 'N'):
                    grid[i][j] = Knight(i, j, 'w')
                elif(grid[i][j] == 'n'):
                    grid[i][j] = Knight(i, j, 'b')
                elif(grid[i][j] == 'B'):
                    grid[i][j] = Bishop(i, j, 'w')
                elif(grid[i][j] == 'b'):
                    grid[i][j] = Bishop(i, j, 'b')
                elif(grid[i][j] == 'Q'):
                    grid[i][j] = Queen(i, j, 'w')
                elif(grid[i][j] == 'q'):
                    grid[i][j] = Queen(i, j, 'b')
                elif(grid[i][j] == 'K'):
                    grid[i][j] = King(i, j, 'w')
                elif(grid[i][j] == 'k'):
                    grid[i][j] = King(i, j, 'b')


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


