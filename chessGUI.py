# chessGUI.py
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from board import Board
import copy
from decisionTree import decisionTree
from tkinter import *

class chessGUI():

    # takes in a board, produces a single window for a graphical representation of the board
    def __init__(self, board, explorationStrategy, depth):
        self.window = Tk()
        self.window.title("Our Chess Board")
        self.explorationStrategy = explorationStrategy
        self.selected = [False, 0, 0]
        self.board = board
        self.ourTree = None
        self.depth = depth

        self.initialClick = False
        self.images = [[None for x in range(8)] for y in range(8)]
        self.backgrounds = [[None for x in range(8)] for y in range(8)]
        for i in range(0,8):
                for j in range(0,8):
                    if ((i + j) % 2 == 0):
                        self.backgrounds[i][j] = "slategray1"
                    else:
                        self.backgrounds[i][j] = "mediumpurple1"

        self.labels = [[None for x in range(8)] for y in range(8)]
        self.window = self.initializePhotos(self.board)

        self.window.mainloop()



    def computerMove(self):
        self.ourTree = None
        self.ourTree = decisionTree(self.board, self.explorationStrategy, self.depth, 'w')

        print("The AI is selecting a move -- PLEASE WAIT, DON'T CLICK ANYTHING PLEASE")
        self.board = self.ourTree.alphaBetaPruning()
        print("The AI has selected a move!")
        if(self.board != None and self.board.isBlackInCheckmate()):
            for i in range(8):
                for j in range(8):
                    if(self.board.grid[i][j] != None):
                        if(self.board.grid[i][j].id == 'k'):
                            self.backgrounds[i][j] = "red"
        self.initializePhotos(self.board)



    
    def mouseClicked(self, event, coords, newBoard):

        # the program requires one initial click to begin
        if(self.initialClick == False):
            self.initialClick = True
            self.computerMove()

        else:

            # When you click where to move
            if(self.selected[0] == True):

                # if the selected piece is not None and you didn't click the same place twice
                if(self.board.grid[self.selected[1]][self.selected[2]] != None and self.board.grid[self.selected[1]][self.selected[2]].color == 'b'):
                    if(self.board.grid[self.selected[1]][self.selected[2]] != None and not (coords[0] == self.selected[1] and coords[1] == self.selected[2])):
                        tempCoords = [coords[0], coords[1]]
                        viableCoords = self.board.grid[self.selected[1]][self.selected[2]].move(self.board)
                        
                        if(tempCoords in viableCoords):

                            self.images[coords[0]][coords[1]] = self.images[self.selected[1]][self.selected[2]]
                            self.labels[coords[0]][coords[1]] = Label(self.window, image = self.images[coords[0]][coords[1]], bg = self.backgrounds[coords[0]][coords[1]])
                            self.labels[coords[0]][coords[1]].grid(row = coords[0], column = coords[1])
                            data = [coords[0], coords[1]]
                            self.labels[coords[0]][coords[1]].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                            self.board.grid[coords[0]][coords[1]] = self.board.grid[self.selected[1]][self.selected[2]]
                            self.board.grid[coords[0]][coords[1]].i = coords[0]
                            self.board.grid[coords[0]][coords[1]].j = coords[1]

                            self.images[self.selected[1]][self.selected[2]] = PhotoImage(file = "blanksquare.png")
                            self.labels[self.selected[1]][self.selected[2]] = Label(self.window, image = self.images[self.selected[1]][self.selected[2]], bg = self.backgrounds[self.selected[1]][self.selected[2]])
                            self.labels[self.selected[1]][self.selected[2]].grid(row = self.selected[1], column = self.selected[2])
                            data = [self.selected[1], self.selected[2]]
                            self.labels[self.selected[1]][self.selected[2]].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                            self.board.grid[self.selected[1]][self.selected[2]] = None
                            for z in viableCoords:
                                self.labels[z[0]][z[1]].config(bg = self.backgrounds[z[0]][z[1]])
                            self.initialClick = False
                        else:
                            for z in viableCoords:
                                self.labels[z[0]][z[1]].config(bg = self.backgrounds[z[0]][z[1]])
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
                self.labels[self.selected[1]][self.selected[2]].config(bg = "gold")
                if(self.board.grid[self.selected[1]][self.selected[2]] != None and self.board.grid[self.selected[1]][self.selected[2]].color == 'b'):
                    viableCoords = self.board.grid[self.selected[1]][self.selected[2]].move(self.board)
                    for z in viableCoords:
                        self.labels[z[0]][z[1]].config(bg = "palegreen3")


    # takes a board object, and will refresh the entire GUI to reflect that board
    # each square in the grid gets a 'Label' object, which holds the picture
    # also, a 'Button' is bound to each square so that it can be clicked on
    def initializePhotos(self, newBoard):
        self.board = newBoard
        for i in range(0,8):
            for j in range(0,8):
                if(newBoard.grid[i][j] != None):
                    if(newBoard.grid[i][j].id == 'P'):
                        self.images[i][j] = PhotoImage(file = "whitepawn.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'p'):
                        self.images[i][j] = PhotoImage(file = "blackpawn.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'N'):
                        self.images[i][j] = PhotoImage(file = "whiteknight.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'n'):
                        self.images[i][j] = PhotoImage(file = "blackknight.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'B'):
                        self.images[i][j] = PhotoImage(file = "whitebishop.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'b'):
                        self.images[i][j] = PhotoImage(file = "blackbishop.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'Q'):
                        self.images[i][j] = PhotoImage(file = "whitequeen.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'q'):
                        self.images[i][j] = PhotoImage(file = "blackqueen.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'K'):
                        self.images[i][j] = PhotoImage(file = "whiteking.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'k'):
                        self.images[i][j] = PhotoImage(file = "blackking.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'R'):
                        self.images[i][j] = PhotoImage(file = "whiterook.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                    elif(newBoard.grid[i][j].id == 'r'):
                        self.images[i][j] = PhotoImage(file = "blackrook.png")
                        self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                        self.labels[i][j].grid(row = i, column = j)
                        data = [i, j]
                        self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
                else:
                    self.images[i][j] = PhotoImage(file = "blanksquare.png")
                    self.labels[i][j] = Label(self.window, image = self.images[i][j], bg = self.backgrounds[i][j])
                    self.labels[i][j].grid(row = i, column = j)
                    data = [i, j]
                    self.labels[i][j].bind("<Button-1>", lambda event, arg=data: self.mouseClicked(event, arg, newBoard))
        return(self.window)
