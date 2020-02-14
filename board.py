# board.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board():
    def __init__(self, grid):
        for i in grid:
            for j in grid[0]:
                if(grid[i][j] == '-'):
                    grid[i][j] = None
                elif(grid[i][j] == 'P'):
                    grid[i][j] = Pawn(j, i, 'w')
                elif(grid[i][j] == 'p'):
                    grid[i][j] = Pawn(j, i, 'b')
                elif(grid[i][j] == 'N'):
                    grid[i][j] = Knight(j, i, 'w')
                elif(grid[i][j] == 'n'):
                    grid[i][j] = Knight(j, i, 'b')
                elif(grid[i][j] == 'B'):
                    grid[i][j] = Bishop(j, i, 'w')
                elif(grid[i][j] == 'b'):
                    grid[i][j] = Bishop(j, i, 'b')
                elif(grid[i][j] == 'Q'):
                    grid[i][j] = Queen(j, i, 'w')
                elif(grid[i][j] == 'q'):
                    grid[i][j] = Queen(j, i, 'b')
                elif(grid[i][j] == 'K'):
                    grid[i][j] = King(j, i, 'w')
                elif(grid[i][j] == 'k'):
                    grid[i][j] = King(j, i, 'b')

                    