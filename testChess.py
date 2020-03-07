# testChess.py

from boardState import boardState


inputFull = [['l', 'h', 'b', 'q', 'u', 'b', 'h', 'r'],
             ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
             ['L', 'H', 'B', 'Q', 'U', 'B', 'H', 'R']]



ourBoard = boardState(inputFull)
ourBoard.printBoard()
# ourBoard.fPawnWhiteMoves(6, 4)
ourBoard.fPawnBlackMoves(1, 2)