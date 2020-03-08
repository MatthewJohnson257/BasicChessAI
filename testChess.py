# testChess.py

from boardState import boardState
from debugGUI import debugGUI

inputFull = [['l', 'h', 'b', 'q', 'u', 'b', 'h', 'o'],
             ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
             ['_', '_', 'p', '_', 'p', '_', '_', '_'],
             ['_', '_', '_', 'P', '_', 's', '_', '_'],
             ['_', 'S', '_', '_', '_', 'r', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
             ['L', 'H', 'B', 'Q', 'U', 'B', 'H', 'O']]



ourBoard = boardState(inputFull)
ourBoard.printBoard()
# ourBoard.fPawnWhiteMoves(6, 4)
ourBoard.fPawnBlackMoves(1, 2)
debugGUI(ourBoard)