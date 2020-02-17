# chess.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from board import Board


inputA = [['_', '_', '_', '_', '_', '_', 'q', 'k'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', 'P', '_', 'p'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', 'Q', 'P'],
['_', '_', '_', '_', '_', 'P', 'P', '_'],
['_', '_', '_', '_', 'R', '_', 'K', '_']]

inputDefault = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'N', 'p', 'p', 'p', '_', 'p'],
['P', '_', '_', 'P', '_', '_', 'R', '_'],
['_', '_', '_', '_', 'N', '_', 'p', '_'],
['_', '_', '_', '_', '_', '_', '_', 'P'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', 'P', 'P', '_', 'P', 'P', 'P', '_'],
['R', '_', 'B', 'Q', 'K', 'B', '_', '_']]

# boardA = Board(inputA, True)
# boardA.printBoard()
# boardA.graphicalBoard()

boardDefault = Board(inputDefault, True)
boardDefault.printBoard()

boardDefault.graphicalBoard()








# List of things we need to implement/figure out:
#--------------------------------General Stuff--------------------------------#
# 1. He said it was important to figure out which moves to explore first, since
#    that determines which/how many nodes get pruned in A-B pruning
# 2.
# 3.
# 4.
#----------------------------------chess.py-----------------------------------#
# 1. Input of all the examples he gave us, also maybe just a regular chess board
# 2. All functionality related to alpha-beta pruning (where board is a state)
# 3. 
# 4. 
# 5.
# 6.
#----------------------------------board.py-----------------------------------#
# 1. Evalutation function (each board has instance variable named 'evalValue')
#    for this score
# 2. Functionality to check if the coordinates returned by a piece's move()
#    method represent a valid move (i.e. no pieces are in the way, the king is
#    not put in check)
# 3. Methods to check whether or not the kings are in check
# 4. 
# 5. 
# 6.
#----------------------------------piece.py-----------------------------------#
# 1. Implement functionality for each piece's move() method
# 2.
# 3.
# 4. 