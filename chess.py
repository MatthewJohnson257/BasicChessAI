###############################################################################
#
# Main file of the program.  Will process input, generate an initial chess 
# board, and will create and call upon a chessGUI object
#
###############################################################################

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from board import Board
from boardState import boardState
from whiteComputerGUI import whiteComputerGUI
from chessGUI import chessGUI
from tkinter import *           # used for GUI
import argparse                 # used to process comand line inputs
import sys                      # used to print error messages
import copy


# These are the input states for new boards

inputA = [['_', '_', '_', '_', '_', '_', 'q', 'k'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', 'P', '_', 'p'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', 'Q', 'P'],
['_', '_', '_', '_', '_', 'P', 'P', '_'],
['_', '_', '_', '_', 'R', '_', 'K', '_']]

inputB = [['_', '_', 'B', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', 'K', '_', '_', '_', '_'],
['_', 'p', '_', '_', '_', '_', '_', '_'],
['_', '_', 'k', '_', '_', '_', '_', '_'],
['P', '_', '_', '_', '_', 'P', '_', '_'],
['_', 'B', '_', '_', '_', '_', '_', '_'],
['N', '_', '_', '_', '_', 'N', '_', '_']]

inputC = [['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', 'K', '_', '_', '_', '_'],
['_', '_', 'R', '_', 'P', '_', '_', '_'],
['_', 'P', '_', 'k', 'r', '_', '_', '_'],
['_', '_', '_', 'N', 'p', 'b', '_', '_'],
['_', '_', '_', '_', 'P', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', 'N', '_', '_']]

# regular chess board
inputFull = [['l', 'h', 'b', 'q', 'u', 'b', 'h', 'r'],
             ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
             ['L', 'H', 'B', 'Q', 'U', 'B', 'H', 'R']]

inputTest1 = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'N', 'p', 'p', 'p', '_', 'p'],
['P', '_', '_', 'P', '_', '_', 'R', '_'],
['_', '_', 'Q', 'B', 'N', '_', 'p', '_'],
['_', '_', '_', '_', 'K', '_', '_', 'P'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', 'P', 'P', '_', 'P', 'P', 'P', '_'],
['R', '_', 'B', '_', '_', '_', '_', '_']]

inputTest2 = [['_', '_', '_', '_', 'k', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', 'K', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_']]





###############################################################################
#                                    GLOBAL                                   #
###############################################################################

# command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('Arguments', metavar='N', type=int, nargs='+')
arguments = parser.parse_args()

# error messages
if(len(arguments.Arguments) != 2):
    sys.exit("    Error: Incorrect number of command line arguments supplied; 2 needed")
if(arguments.Arguments[0] < 1 or arguments.Arguments[0] > 6):
    sys.exit("    Error: Invalid value for first command line argument; must be in range(1,6)")
if(arguments.Arguments[1] < 1 or arguments.Arguments[1] > 2):
    sys.exit("    Error: Invalid value for second command line argument; must be in range(1,2)")

usedBoard = arguments.Arguments[0]              # which given puzzle to solve
explorationStrategy = arguments.Arguments[1]    # which exploration strategy to use


# determine which of the initial boards we are using
inputGrid = None
if(usedBoard == 4):
    inputGrid = inputA
elif(usedBoard == 2):
    inputGrid = inputB
elif(usedBoard == 3):
    inputGrid = inputC
elif(usedBoard == 1):
    inputGrid = inputFull
elif(usedBoard == 5):
    inputGrid = inputTest1
elif(usedBoard == 6):
    inputGrid = inputTest2

# maximum depth used for the alpha beta pruning tree
depth = 1

boardDefault = boardState(inputGrid)                        # create initial Board object
boardDefault.printBoard()                              # print to terminal the Board (text)
whiteComputerGUI(boardDefault, depth)     # create and launch chess GUI






