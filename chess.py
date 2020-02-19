# chess.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from board import Board
from tkinter import *
import argparse         # used to process comand line inputs
import sys              # used to print error messages
import copy


inputA = [['_', '_', '_', '_', '_', '_', 'q', 'k'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', 'P', '_', 'p'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', 'Q', 'P'],
['_', '_', '_', '_', '_', 'P', 'P', '_'],
['_', '_', '_', '_', 'R', '_', 'K', '_']]

inputFull = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

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

# takes in a board, produces a single window for a graphical representation of the board
def graphicalBoard(board):
    window = Tk()
    window.title("Our Chess Board")
    board.generateAllWhiteMoves()
    selected = [False, 0, 0]

    images = [[None for x in range(8)] for y in range(8)]
    backgrounds = [[None for x in range(8)] for y in range(8)]
    for i in range(0,8):
            for j in range(0,8):
                if ((i + j) % 2 == 0):
                    backgrounds[i][j] = "slategray1"
                else:
                    backgrounds[i][j] = "mediumpurple1"

    labels = [[None for x in range(8)] for y in range(8)]

    def mouseClicked(event, coords):

        # When you click where to move
        if(selected[0] == True):

            # if the select piece is not None and you didn't click the same place twice
            if(board.grid[selected[1]][selected[2]] != None and not (coords[0] == selected[1] and coords[1] == selected[2])):
                tempCoords = [coords[0], coords[1]]
                viableCoords = board.grid[selected[1]][selected[2]].move(board)
                 
                if(tempCoords in viableCoords):

                    images[coords[0]][coords[1]] = images[selected[1]][selected[2]]
                    labels[coords[0]][coords[1]] = Label(window, image = images[coords[0]][coords[1]], bg = backgrounds[coords[0]][coords[1]])
                    labels[coords[0]][coords[1]].grid(row = coords[0], column = coords[1])
                    data = [coords[0], coords[1]]
                    labels[coords[0]][coords[1]].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    board.grid[coords[0]][coords[1]] = board.grid[selected[1]][selected[2]]
                    board.grid[coords[0]][coords[1]].i = coords[0]
                    board.grid[coords[0]][coords[1]].j = coords[1]

                    images[selected[1]][selected[2]] = PhotoImage(file = "blanksquare.png")
                    labels[selected[1]][selected[2]] = Label(window, image = images[selected[1]][selected[2]], bg = backgrounds[selected[1]][selected[2]])
                    labels[selected[1]][selected[2]].grid(row = selected[1], column = selected[2])
                    data = [selected[1], selected[2]]
                    labels[selected[1]][selected[2]].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    board.grid[selected[1]][selected[2]] = None
                    for z in viableCoords:
                        labels[z[0]][z[1]].config(bg = backgrounds[z[0]][z[1]])
                else:
                    for z in viableCoords:
                        labels[z[0]][z[1]].config(bg = backgrounds[z[0]][z[1]])
            elif (coords[0] == selected[1] and coords[1] == selected[2] and board.grid[coords[0]][coords[1]] != None):
                viableCoords = board.grid[selected[1]][selected[2]].move(board)
                for z in viableCoords:
                        labels[z[0]][z[1]].config(bg = backgrounds[z[0]][z[1]])
            selected[0] = False
            labels[selected[1]][selected[2]].config(bg = backgrounds[selected[1]][selected[2]])



        # when you click on a piece to select it
        else:
            selected[1] = coords[0]
            selected[2] = coords[1]
            selected[0] = True
            labels[selected[1]][selected[2]].config(bg = "gold")
            if(board.grid[selected[1]][selected[2]] != None):
                viableCoords = board.grid[selected[1]][selected[2]].move(board)
                for z in viableCoords:
                    labels[z[0]][z[1]].config(bg = "palegreen3")


    def updatePhotos():
        for i in range(0,8):
            for j in range(0,8):
                if(board.grid[i][j] != None):
                    if(board.grid[i][j].id == 'P'):
                        images[i][j] = PhotoImage(file = "whitepawn.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'p'):
                        images[i][j] = PhotoImage(file = "blackpawn.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'N'):
                        images[i][j] = PhotoImage(file = "whiteknight.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'n'):
                        images[i][j] = PhotoImage(file = "blackknight.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'B'):
                        images[i][j] = PhotoImage(file = "whitebishop.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'b'):
                        images[i][j] = PhotoImage(file = "blackbishop.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'Q'):
                        images[i][j] = PhotoImage(file = "whitequeen.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'q'):
                        images[i][j] = PhotoImage(file = "blackqueen.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'K'):
                        images[i][j] = PhotoImage(file = "whiteking.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'k'):
                        images[i][j] = PhotoImage(file = "blackking.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'R'):
                        images[i][j] = PhotoImage(file = "whiterook.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    elif(board.grid[i][j].id == 'r'):
                        images[i][j] = PhotoImage(file = "blackrook.png")
                        labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                        labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                else:
                    images[i][j] = PhotoImage(file = "blanksquare.png")
                    labels[i][j] = Label(window, image = images[i][j], bg = backgrounds[i][j])
                    labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    labels[i][j].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
        return(window)


    window = updatePhotos()
    window.mainloop()




###############################################################################
#                                    GLOBAL                                   #
###############################################################################

# command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('Arguments', metavar='N', type=int, nargs='+')
arguments = parser.parse_args()

# error messages
if(len(arguments.Arguments) != 1):
    sys.exit("    Error: Incorrect number of command line arguments supplied; 1 needed")

usedBoard = arguments.Arguments[0]             # which given puzzle to solve

inputGrid = None
if(usedBoard == 1):
    inputGrid = inputA
elif(usedBoard == 2):
    inputGrid = inputFull
elif(usedBoard == 3):
    inputGrid = inputTest1
elif(usedBoard == 4):
    inputGrid = inputTest2



boardDefault = Board(inputGrid, True)
boardDefault.printBoard()
graphicalBoard(boardDefault)






