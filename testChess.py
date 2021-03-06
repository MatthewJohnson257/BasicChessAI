# testChess.py

from boardState import boardState
from debugGuiA import debugGuiA
from debugGuiB import debugGuiB
from debugGuiC import debugGuiC

inputFull = [['l', 'h', 'b', 'q', 'u', 'b', 'h', 'o'],
             ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
             ['L', 'H', 'B', 'Q', 'U', 'B', 'H', 'O']]



ourBoard = boardState(inputFull)
ourBoard.printBoard()
# ourBoard.fPawnWhiteMoves(6, 4)
ourBoard.fPawnBlackMoves(1, 2)
#debugGuiA(ourBoard)
#debugGuiB(ourBoard)
debugGuiC(ourBoard)