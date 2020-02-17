# board.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from tkinter import *

class Board():

    # this is the constructor: it takes in 'grid', which is a 2d array of char
    # then scans it for the values, and creates the appropriate 'Piece' object,
    # but a blank space is given the value 'None', which is Python's version of
    # null
    #
    # For reference:
    #       - any method that says '__init__' is a constructor.
    #       - 'self' just references to the specific object's instance, kind of
    #           like Java's 'this'
#a = [[0 for x in range(columns)] for y in range(rows)]

    def __init__(self, grid, newBoard = False, whiteInCheck = False, blackInCheck = False):
        if(newBoard == True):
            self.grid = [[None for x in range(0,8)] for y in range(0,8)]
            for i in range(0,8):
                for j in range(0,8):
                    if(grid[i][j] == '_' or grid[i][j] == '-'):
                        self.grid[i][j] = None
                    elif(grid[i][j] == 'P'):
                        self.grid[i][j] = Pawn(i, j, 'w', 'P')
                    elif(grid[i][j] == 'p'):
                        self.grid[i][j] = Pawn(i, j, 'b', 'p')
                    elif(grid[i][j] == 'N'):
                        self.grid[i][j] = Knight(i, j, 'w', 'N')
                    elif(grid[i][j] == 'n'):
                        self.grid[i][j] = Knight(i, j, 'b', 'n')
                    elif(grid[i][j] == 'B'):
                        self.grid[i][j] = Bishop(i, j, 'w', 'B')
                    elif(grid[i][j] == 'b'):
                        self.grid[i][j] = Bishop(i, j, 'b', 'b')
                    elif(grid[i][j] == 'Q'):
                        self.grid[i][j] = Queen(i, j, 'w', 'Q')
                    elif(grid[i][j] == 'q'):
                        self.grid[i][j] = Queen(i, j, 'b', 'q')
                    elif(grid[i][j] == 'K'):
                        self.grid[i][j] = King(i, j, 'w', 'K')
                    elif(grid[i][j] == 'k'):
                        self.grid[i][j] = King(i, j, 'b', 'k')
                    elif(grid[i][j] == 'R'):
                        self.grid[i][j] = Rook(i, j, 'w', 'R')
                    elif(grid[i][j] == 'r'):
                        self.grid[i][j] = Rook(i, j, 'b', 'r')
            self.whiteInCheck = self.isWhiteInCheck()
            self.blackInCheck = self.isBlackInCheck()
        else:
            self.grid = grid
            self.whiteInCheck = whiteInCheck
            self.blackInCheck = blackInCheck

        self.evalValue = self.evaluationFunction()            
        #self.testMoveMethodWhitePawn()
        #self.testMoveMethodWhiteRook()
        self.testMoveMethodWhiteKnight()


    # takes in which color's turn it is, generates all valid moves for that player
    #
    # we will more fully implement this after we get all the move() methods in Piece.py done
    def generateMoves(self, color):
        if(color == 'b'):
            GucciMane = 1 # just here as a temporary placeholder so no errors are thrown

            # STUB - search the entire grid for black pieces, call move() for each of them
            # then check to see if what is returned are valid coordinate moves for that piece
            # (this will be more clear when you see what I wrote in Piece.py)

        if(color == 'w'):
            GucciMane = 1 # just here as a temporary placeholder so no errors are thrown
            # STUB

    # temporary method to test move() methods
    def testMoveMethodWhitePawn(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'P'):
                        print(self.grid[i][j].move(self))

    def testMoveMethodWhiteRook(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'R'):
                        print(self.grid[i][j].move(self))

    def testMoveMethodWhiteKnight(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'N'):
                        print(self.grid[i][j].move(self))

    def evaluationFunction(self):
        whiteCount = 0
        blackCount = 0

        for i in range(8):
            for j in range(8):
                if self.grid[i][j] != None:
                    if self.grid[i][j].color == 'w':
                        if self.grid[i][j].id == 'P':
                            whiteCount = whiteCount + 1
                        elif self.grid[i][j].id == 'N':
                            whiteCount = whiteCount + 3
                        elif self.grid[i][j].id == 'B':
                            whiteCount = whiteCount + 3.07
                        elif self.grid[i][j].id == 'Q':
                            whiteCount = whiteCount + 9
                        elif self.grid[i][j].id == 'R':
                            whiteCount = whiteCount + 5
                    if self.grid[i][j].color == 'b':
                        if self.grid[i][j].id == 'p':
                            blackCount = blackCount + 1
                        elif self.grid[i][j].id == 'n':
                            blackCount = blackCount + 3
                        elif self.grid[i][j].id == 'b':
                            blackCount = blackCount + 3.07
                        elif self.grid[i][j].id == 'q':
                            blackCount = blackCount + 9
                        elif self.grid[i][j].id == 'r':
                            blackCount = blackCount + 5

        return(whiteCount-blackCount) # STUB





    def isWhiteInCheck(self):

        # find where the white king is
        iKing = 0
        jKing = 0
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None and self.grid[i][j].id == 'K'):
                    iKing = i
                    jKing = j
                    break


        # check for horizontal attacks from left

        # check for horizontal attacks from right

        # check for vertical attacks from above

        # check for vertical attacks from below

        # check for diagonal from top left

        # check for diagonal from bottom left

        # check for diagonal from top right

        # check for diagonal from bottom left

        # check for knights attacking


        return(False) # STUB


    def isBlackInCheck(self):
        GucciMane = 1 # just here as a temporary placeholder so no errors are thrown
        return(False) # STUB





    # takes in a board, and prints to output a character representation of that board
    def printBoard(self):
        print("    ◘----------------◘")
        for i in range(0,8):
            print('    |', end = '')
            for j in range(0,8):
                if(self.grid[i][j] == None):
                    print(" ", end = ' ')
                else:
                    print(self.grid[i][j].id, end = ' ')
            print('|', end = '')
            print()
        print("    ◘----------------◘")



    # takes in a board, produces a single window for a graphical representation of the board
    def graphicalBoard(self):
        window = Tk()
        window.title("Our Chess Board")

        images = [[None for x in range(8)] for y in range(8)]
        backgrounds = [[None for x in range(8)] for y in range(8)]
        for i in range(0,8):
            for j in range(0,8):
                if ((i + j) % 2 == 0):
                    backgrounds[i][j] = "white"
                else:
                    backgrounds[i][j] = "mediumpurple1"
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'P'):
                        images[i][j] = PhotoImage(file = "whitepawn.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'p'):
                        images[i][j] = PhotoImage(file = "blackpawn.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'N'):
                        images[i][j] = PhotoImage(file = "whiteknight.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'n'):
                        images[i][j] = PhotoImage(file = "blackknight.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'B'):
                        images[i][j] = PhotoImage(file = "whitebishop.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'b'):
                        images[i][j] = PhotoImage(file = "blackbishop.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'Q'):
                        images[i][j] = PhotoImage(file = "whitequeen.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'q'):
                        images[i][j] = PhotoImage(file = "blackqueen.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'K'):
                        images[i][j] = PhotoImage(file = "whiteking.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'k'):
                        images[i][j] = PhotoImage(file = "blackking.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'R'):
                        images[i][j] = PhotoImage(file = "whiterook.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                    elif(self.grid[i][j].id == 'r'):
                        images[i][j] = PhotoImage(file = "blackrook.png")
                        Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)
                else:
                    images[i][j] = PhotoImage(file = "blanksquare.png")
                    Label(window, image = images[i][j], bg = backgrounds[i][j]).grid(row = i, column = j)

        # b = Button(window, text="OK", command=callback)
        window.mainloop()
        # print("WOEIRJEIJ")
