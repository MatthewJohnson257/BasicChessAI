###############################################################################
#
# This file handles all necessary items related to the GUI, mouse clicks, and
# also dictates the turns between the player and the computer AI.
#
###############################################################################
from board import Board
import copy
from decisionTree import decisionTree
from tkinter import *



###############################################################################
#
# class for the GUI elements and mouse event clicking components
#
###############################################################################
class whiteComputerGUI():

    ###############################################################################
    #
    # chessGUI constructor takes in a board, produces a single window for a
    # graphical representation of the board.  Initializes the backgrounds (blue or
    # purple) and starting images for the grids squares, and launches the windows
    #
    ###############################################################################
    def __init__(self, board, depth):
        self.window = Tk()                              # window object
        self.window.title("Our Chess Board")
        self.selected = [False, 0, 0]                   # used when processing mouse clicks

        self.board = board                              # starting board for GUI
        self.ourTree = None                             # alpha beta tree
        self.depth = depth

        self.isComputersTurn = True                     # for taking terns

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
    # Used when it is the computer's turn to move.  AI looks at the board, creates
    # a decisionTree to find the optimal move, then changes the board to reflect
    # that move decision
    #
    ###############################################################################
    def computerMove(self):
        self.ourTree = None

        # create alpha beta tree
        self.ourTree = decisionTree(self.board, self.depth, 'w')

        print("****The AI is selecting a move -- PLEASE WAIT, DON'T CLICK ANYTHING PLEASE****")

        # run alpha beta h minimax algorithm
        self.board = self.ourTree.alphaBetaPruning()
        print("The AI has selected a move!")

        # if checkmate occurs, highlight the king in red
        if(self.board != None and (self.board.isBlackInCheckmate() or self.board.isWhiteInCheckmate())):
            for i in range(8):
                for j in range(8):
                    if(self.board.grid[i][j] != None):
                        if((self.board.grid[i][j].id == 'k' and self.board.isBlackInCheckmate()) or (self.board.grid[i][j].id == 'K' and self.board.isWhiteInCheckmate())):
                            self.backgrounds[i][j] = "red"
        self.initializePhotos(self.board)



    ###############################################################################
    #
    # Handles an event when a mouse is clicked by the player, highlighting the
    # appropriate square(s) in the grid
    #
    ###############################################################################
    def mouseClicked(self, event, coords, newBoard):

        # the program requires one initial click before the AI can make a move
        if(self.isComputersTurn == True):
            self.isComputersTurn = False
            self.computerMove()


        # if it is the player's move:
        else:

            # When you click where to move
            if(self.selected[0] == True):

                # if the selected piece is not None and you didn't click the same place twice
                if(self.board.grid[self.selected[1]][self.selected[2]] != None and self.board.grid[self.selected[1]][self.selected[2]].color == 'b'):
                    if(self.board.grid[self.selected[1]][self.selected[2]] != None and not (coords[0] == self.selected[1] and coords[1] == self.selected[2])):

                        # the coordinates of where you clicked
                        tempCoords = [coords[0], coords[1]]

                        # find the coordinates where the selected piece can move
                        viableCoords = self.board.grid[self.selected[1]][self.selected[2]].move(self.board)

                        # if it is a valid move, adjust the board and redraw the window to reflect that move
                        if(tempCoords in viableCoords):

                            self.images[coords[0]][coords[1]] = self.images[self.selected[1]][self.selected[2]]
                            self.labels[coords[0]][coords[1]] = Label(self.window, image = self.images[coords[0]][coords[1]], bg = self.backgrounds[coords[0]][coords[1]])
                            self.labels[coords[0]][coords[1]].grid(row = coords[0], column = coords[1])
                            data = [coords[0], coords[1]]
                            self.labels[coords[0]][coords[1]].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                            self.board.grid[coords[0]][coords[1]] = self.board.grid[self.selected[1]][self.selected[2]]
                            self.board.grid[coords[0]][coords[1]].i = coords[0]
                            self.board.grid[coords[0]][coords[1]].j = coords[1]

                            # set old position to blank
                            self.images[self.selected[1]][self.selected[2]] = PhotoImage(file = "blanksquare.png")
                            self.labels[self.selected[1]][self.selected[2]] = Label(self.window, image = self.images[self.selected[1]][self.selected[2]], bg = self.backgrounds[self.selected[1]][self.selected[2]])
                            self.labels[self.selected[1]][self.selected[2]].grid(row = self.selected[1], column = self.selected[2])
                            data = [self.selected[1], self.selected[2]]
                            self.labels[self.selected[1]][self.selected[2]].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                            self.board.grid[self.selected[1]][self.selected[2]] = None

                            # reset the background colors
                            for z in viableCoords:
                                self.labels[z[0]][z[1]].config(bg = self.backgrounds[z[0]][z[1]])
                            self.isComputersTurn = True

                        # if it is not a valid move, reset the backgrounds
                        else:
                            for z in viableCoords:
                                self.labels[z[0]][z[1]].config(bg = self.backgrounds[z[0]][z[1]])

                    # if you selected the same square twice
                    elif (coords[0] == self.selected[1] and coords[1] == self.selected[2] and self.board.grid[coords[0]][coords[1]] != None):
                        viableCoords = self.board.grid[self.selected[1]][self.selected[2]].move(self.board)
                        for z in viableCoords:
                                self.labels[z[0]][z[1]].config(bg = self.backgrounds[z[0]][z[1]])
                self.selected[0] = False
                self.labels[self.selected[1]][self.selected[2]].config(bg = self.backgrounds[self.selected[1]][self.selected[2]])


            # when you click on a piece to select it
            else:
                self.selected[1] = coords[0]
                self.selected[2] = coords[1]
                self.selected[0] = True

                # highlight the piece, and the places where the piece can move
                self.labels[self.selected[1]][self.selected[2]].config(bg = "gold")
                if(self.board.grid[self.selected[1]][self.selected[2]] != None and self.board.grid[self.selected[1]][self.selected[2]].color == 'b'):
                    viableCoords = self.board.grid[self.selected[1]][self.selected[2]].move(self.board)
                    for z in viableCoords:
                        self.labels[z[0]][z[1]].config(bg = "palegreen3")


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