# debugGuiC

import copy
from tkinter import *
from boardState import boardState
from adversarialTree import adversarialTree

class debugGuiC():

    def __init__(self, board):
        self.window = Tk()                              # window object
        self.window.title("Our Chess Board")
        self.selected = [False, 0, 0]                   # used when processing mouse clicks
        self.board = board                              # starting board for GUI
        self.ourTree = None

        self.isComputersTurn = True                     # for taking turns

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

        # create adversarial search tree
        self.ourTree = adversarialTree(self.board, 4, 'w')

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

        #self.board.printBoard()
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

            if(self.selected[0] == False):
                self.selected[1] = coords[0]
                self.selected[2] = coords[1]
                self.selected[0] = True

                self.labels[self.selected[1]][self.selected[2]].config(bg = "gold")
                viableCoords = []
                viableCoords = self.board.move(self.selected[1], self.selected[2], self.board.grid[self.selected[1]][self.selected[2]])          


                for z in viableCoords:
                    self.labels[z[0]][z[1]].config(bg = "palegreen3")

            else:
                self.selected[0] = False

                # reset backgrounds
                for i in range(8):
                    for j in range(8):
                        self.labels[i][j].config(bg = self.backgrounds[i][j])
                
                viableCoords = []
                viableCoords = self.board.move(self.selected[1], self.selected[2], self.board.grid[self.selected[1]][self.selected[2]])          


                # if you didn't select the same square twice
                if(coords[0] != self.selected[1] or coords[1] != self.selected[2]):

                    # if the selected square represents a valid move
                    for y in viableCoords:
                        if(coords[0] == y[0] and coords[1] == y[1]):
                            
                            nextBoard = self.board.convertCoordsToBoards(self.selected[1], self.selected[2], [y])

                            # reset entire board
                            self.initializePhotos(nextBoard[0])
                    
                            self.isComputersTurn = True




    ###############################################################################
    #
    # takes a boardState object, and will refresh the entire GUI to reflect that 
    # board each square in the grid gets a 'Label' object, which holds the picture.
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