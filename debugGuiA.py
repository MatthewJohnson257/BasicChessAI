# debugGUI

import copy
from tkinter import *

class debugGuiA():

    def __init__(self, board):
        self.window = Tk()                              # window object
        self.window.title("Our Chess Board")
        self.selected = [False, 0, 0]                   # used when processing mouse clicks
        self.board = board                              # starting board for GUI

        # images in the GUI for different pieces
        self.images = [[None for x in range(8)] for y in range(8)]

        # background colors for the grid squares
        self.backgrounds = [[None for x in range(8)] for y in range(8)]
        for i in range(0,8):
                for j in range(0,8):
                    if ((i + j) % 2 == 0):
                        self.backgrounds[i][j] = "slategray1"
                    else:
                        self.backgrounds[i][j] = "mediumpurple1"

        # GUI label objects
        self.labels = [[None for x in range(8)] for y in range(8)]

        # initialize given board
        self.window = self.initializePhotos(self.board)

        # launch window, run indefinitely
        self.window.mainloop()



    ###############################################################################
    #
    # Handles an event when a mouse is clicked by the player, highlighting the
    # appropriate square(s) in the grid
    #
    ###############################################################################
    def mouseClicked(self, event, coords, newBoard):

        if(self.selected[0] == False):
            self.selected[1] = coords[0]
            self.selected[2] = coords[1]
            self.selected[0] = True

            self.labels[self.selected[1]][self.selected[2]].config(bg = "gold")
            viableCoords = []
            if(self.board.grid[self.selected[1]][self.selected[2]] == 'P'):
                viableCoords = self.board.pPawnWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'p'):
                viableCoords = self.board.pPawnBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'F'):
                viableCoords = self.board.fPawnWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'f'):
                viableCoords = self.board.fPawnBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'S'):
                viableCoords = self.board.sPawnWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 's'):
                viableCoords = self.board.sPawnBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'Q'):
                viableCoords = self.board.qQueenWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'q'):
                viableCoords = self.board.qQueenBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'K'):
                viableCoords = self.board.kKingWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'k'):
                viableCoords = self.board.kKingBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'U'):
                viableCoords = self.board.uKingWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'u'):
                viableCoords = self.board.uKingBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'B'):
                viableCoords = self.board.bBishopWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'b'):
                viableCoords = self.board.bBishopBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'O'):
                viableCoords = self.board.oRookWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'o'):
                viableCoords = self.board.oRookBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'L'):
                viableCoords = self.board.lRookWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'l'):
                viableCoords = self.board.lRookBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'R'):
                viableCoords = self.board.rRookWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'r'):
                viableCoords = self.board.rRookBlackMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'H'):
                viableCoords = self.board.hKnightWhiteMoves(self.selected[1], self.selected[2])
            elif(self.board.grid[self.selected[1]][self.selected[2]] == 'h'):
                viableCoords = self.board.hKnightBlackMoves(self.selected[1], self.selected[2])


            for z in viableCoords:
                self.labels[z[0]][z[1]].config(bg = "palegreen3")

        else:
            self.selected[0] = False

            # reset backgrounds
            for i in range(8):
                for j in range(8):
                    self.labels[i][j].config(bg = self.backgrounds[i][j])
            
            # if you didn't select the same square twice
            if(coords[0] != self.selected[1] or coords[1] != self.selected[2]):

                # move the piece; it can move anywhere.  Even a blank square can move!
                self.images[coords[0]][coords[1]] = self.images[self.selected[1]][self.selected[2]]
                self.labels[coords[0]][coords[1]] = Label(self.window, image = self.images[coords[0]][coords[1]], bg = self.backgrounds[coords[0]][coords[1]])
                self.labels[coords[0]][coords[1]].grid(row = coords[0], column = coords[1])
                data = [coords[0], coords[1]]

                self.labels[coords[0]][coords[1]].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                self.board.grid[coords[0]][coords[1]] = self.board.grid[self.selected[1]][self.selected[2]]
                

                # set old position to blank
                self.images[self.selected[1]][self.selected[2]] = PhotoImage(file = "blanksquare.png")
                self.labels[self.selected[1]][self.selected[2]] = Label(self.window, image = self.images[self.selected[1]][self.selected[2]], bg = self.backgrounds[self.selected[1]][self.selected[2]])
                self.labels[self.selected[1]][self.selected[2]].grid(row = self.selected[1], column = self.selected[2])
                data = [self.selected[1], self.selected[2]]
                self.labels[self.selected[1]][self.selected[2]].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                self.board.grid[self.selected[1]][self.selected[2]] = '_'



    ###############################################################################
    #
    # takes a board object, and will refresh the entire GUI to reflect that board
    # each square in the grid gets a 'Label' object, which holds the picture.
    # Also, a 'Button' is bound to each square so that it can be clicked on
    #
    ###############################################################################
    def initializePhotos(self, newBoard):
        self.board = newBoard
        for i in range(0,8):
            for j in range(0,8):
                if(newBoard.grid[i][j] == '_'):
                    self.images[i][j] = PhotoImage(file = "blanksquare.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'P' or newBoard.grid[i][j] == 'F' or newBoard.grid[i][j] == 'S'):
                    self.images[i][j] = PhotoImage(file = "whitepawn.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'p' or newBoard.grid[i][j] == 'f' or newBoard.grid[i][j] == 's'):
                    self.images[i][j] = PhotoImage(file = "blackpawn.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'H'):
                    self.images[i][j] = PhotoImage(file = "whiteknight.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'h'):
                    self.images[i][j] = PhotoImage(file = "blackknight.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'B'):
                    self.images[i][j] = PhotoImage(file = "whitebishop.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'b'):
                    self.images[i][j] = PhotoImage(file = "blackbishop.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'Q'):
                    self.images[i][j] = PhotoImage(file = "whitequeen.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'q'):
                    self.images[i][j] = PhotoImage(file = "blackqueen.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'K' or newBoard.grid[i][j] == 'U'):
                    self.images[i][j] = PhotoImage(file = "whiteking.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'k' or newBoard.grid[i][j] == 'u'):
                    self.images[i][j] = PhotoImage(file = "blackking.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'O' or newBoard.grid[i][j] == 'L' or newBoard.grid[i][j] == 'R'):
                    self.images[i][j] = PhotoImage(file = "whiterook.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                elif(newBoard.grid[i][j] == 'o' or newBoard.grid[i][j] == 'l' or newBoard.grid[i][j] == 'r'):
                    self.images[i][j] = PhotoImage(file = "blackrook.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
        return(self.window)