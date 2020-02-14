# board.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board():
    def __init__(self, grid):
        for i in grid:
            for j in grid[0]:
                if(grid[i][j] == '-'):
                    break
                elif(grid[i][j] == 'P'):
                    grid[i][j] = Pawn(i, j, 'w')
                    