# chess.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from board import Board
from tkinter import *
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

inputDefault = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'N', 'p', 'p', 'p', '_', 'p'],
['P', '_', '_', 'P', '_', '_', 'R', '_'],
['_', '_', 'Q', 'B', 'N', '_', 'p', '_'],
['_', '_', '_', '_', 'K', '_', '_', 'P'],
['_', '_', '_', '_', '_', '_', '_', '_'],
['_', 'P', 'P', '_', 'P', 'P', 'P', '_'],
['R', '_', 'B', '_', '_', '_', '_', '_']]

# takes in a board, produces a single window for a graphical representation of the board
def graphicalBoard(board):
    window = Tk()
    window.title("Our Chess Board")

    outsiders = [False, 0, 0]

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
        if(outsiders[0] == True):

            # if the select piece is not None and you didn't click the same place twice
            if(board.grid[outsiders[1]][outsiders[2]] != None and not (coords[0] == outsiders[1] and coords[1] == outsiders[2])):
                tempCoords = [coords[0], coords[1]]
                viableCoords = board.grid[outsiders[1]][outsiders[2]].move(board)
                #print("viableCoords:", viableCoords)
                if(tempCoords in viableCoords):

                    images[coords[0]][coords[1]] = images[outsiders[1]][outsiders[2]]
                    labels[coords[0]][coords[1]] = Label(window, image = images[coords[0]][coords[1]], bg = backgrounds[coords[0]][coords[1]])
                    labels[coords[0]][coords[1]].grid(row = coords[0], column = coords[1])
                    data = [coords[0], coords[1]]
                    labels[coords[0]][coords[1]].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    board.grid[coords[0]][coords[1]] = board.grid[outsiders[1]][outsiders[2]]
                    board.grid[coords[0]][coords[1]].i = coords[0]
                    board.grid[coords[0]][coords[1]].j = coords[1]

                    images[outsiders[1]][outsiders[2]] = PhotoImage(file = "blanksquare.png")
                    labels[outsiders[1]][outsiders[2]] = Label(window, image = images[outsiders[1]][outsiders[2]], bg = backgrounds[outsiders[1]][outsiders[2]])
                    labels[outsiders[1]][outsiders[2]].grid(row = outsiders[1], column = outsiders[2])
                    data = [outsiders[1], outsiders[2]]
                    labels[outsiders[1]][outsiders[2]].bind("<Button-1>", lambda event, arg=data: mouseClicked(event, arg))
                    board.grid[outsiders[1]][outsiders[2]] = None
                    for z in viableCoords:
                        labels[z[0]][z[1]].config(bg = backgrounds[z[0]][z[1]])
                    # for g in range(8):
                    #     for h in range(8):
                    #         labels[g][h].config(bg = backgrounds[g][h])
                        #labels[z[0]][z[1]].config(bg = "black")
                else:
                    for z in viableCoords:
                        labels[z[0]][z[1]].config(bg = backgrounds[z[0]][z[1]])
            elif (coords[0] == outsiders[1] and coords[1] == outsiders[2] and board.grid[coords[0]][coords[1]] != None):
                viableCoords = board.grid[outsiders[1]][outsiders[2]].move(board)
                for z in viableCoords:
                        labels[z[0]][z[1]].config(bg = backgrounds[z[0]][z[1]])
            outsiders[0] = False
            labels[outsiders[1]][outsiders[2]].config(bg = backgrounds[outsiders[1]][outsiders[2]])
            #print("Click Change")

        # when you click on a piece to select it
        else:
            outsiders[1] = coords[0]
            outsiders[2] = coords[1]
            outsiders[0] = True
            labels[outsiders[1]][outsiders[2]].config(bg = "gold")
            if(board.grid[outsiders[1]][outsiders[2]] != None):
                #print(board.grid[outsiders[1]][outsiders[2]].id)
                viableCoords = board.grid[outsiders[1]][outsiders[2]].move(board)
                #print("viableCoords:", viableCoords)
                for z in viableCoords:
                    labels[z[0]][z[1]].config(bg = "palegreen3")
            #print("Click Set")


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

# boardA = Board(inputA, True)
# boardA.printBoard()
# boardA.graphicalBoard()


boardDefault = Board(inputFull, True)
boardDefault.printBoard()
graphicalBoard(boardDefault)








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
