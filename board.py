# board.py

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from tkinter import *
import copy

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
            self.pEval = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [50, 50, 50, 50, 50, 50, 50, 50],
                          [10, 10, 20, 30, 30, 20, 10, 10],
                          [5, 5, 10, 25, 25, 10, 5, 5],
                          [0, 0, 0, 20, 20, 0, 0, 0],
                          [5, -5, -10, 0, 0, -10, -5, 5],
                          [5, 10, 10, -20, -20, 10, 10, 5],
                          [0, 0, 0, 0, 0, 0, 0, 0]]

            self.PEval = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [5, 10, 10, -20, -20, 10, 10, 5],
                          [5, -5, -10, 0, 0, -10, -5, 5],
                          [0, 0, 0, 20, 20, 0, 0, 0],
                          [5, 5, 10, 25, 25, 10, 5, 5],
                          [10, 10, 20, 30, 30, 20, 10, 10],
                          [50, 50, 50, 50, 50, 50, 50, 50],
                          [0, 0, 0, 0, 0, 0, 0, 0]]

            self.nEval = [[-50, -40, -30, -30, -30, -30, -40, -50],
                          [-40, -20, 0, 0, 0, 0, -20, -40],
                          [-30, 0, 10, 15, 15, 10, 0, -30],
                          [-30, 5, 15, 20, 20, 15, 5, -30],
                          [-30, 0, 15, 20, 20, 15, 0, -30],
                          [-30, 5, 10, 15, 15, 10, 5, -30],
                          [-40, -20, 0, 5, 5, 0, -20, -40],
                          [-50, -40, -30, -30, -30, -30, -40, -50]]

            self.NEval = [[-50, -40, -30, -30, -30, -30, -40, -50],
                          [-40, -20, 0, 5, 5, 0, -20, -40],
                          [-30, 5, 10, 15, 15, 10, 5, -30],
                          [-30, 0, 15, 20, 20, 15, 0, -30],
                          [-30, 5, 15, 20, 20, 15, 5, -30],
                          [-30, 0, 10, 15, 15, 10, 0, -30],
                          [-40, -20, 0, 0, 0, 0, -20, -40],
                          [-50, -40, -30, -30, -30, -30, -40, -50]]

            self.bEval = [[-20, -10, -10, -10, -10, -10, -10, -20],
                          [-10, 0, 0, 0, 0, 0, 0, -10],
                          [-10, 0, 5, 10, 10, 5, 0, -10],
                          [-10, 5, 5, 10, 10, 5, 5, -10],
                          [-10, 0, 10, 10, 10, 10, 0, -10],
                          [-10, 10, 10, 10, 10, 10, 10, -10],
                          [-10, 5, 0, 0, 0, 0, 5, -10],
                          [-20, -10, -10, -10, -10, -10, -10, -20]]

            self.BEval = [[-20, -10, -10, -10, -10, -10, -10, -20],
                          [-10, 5, 0, 0, 0, 0, 5, -10],
                          [-10, 10, 10, 10, 10, 10, 10, -10],
                          [-10, 0, 10, 10, 10, 10, 0, -10],
                          [-10, 5, 5, 10, 10, 5, 5, -10],
                          [-10, 0, 5, 10, 10, 5, 0, -10],
                          [-10, 0, 0, 0, 0, 0, 0, -10],
                          [-20, -10, -10, -10, -10, -10, -10, -20]]

            self.rEval = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [5, 10, 10, 10, 10, 10, 10, 5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [0, 0, 0, 5, 5, 0, 0, 0]]

            self.REval = [[0, 0, 0, 5, 5, 0, 0, 0],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [-5, 0, 0, 0, 0, 0, 0, -5],
                          [5, 10, 10, 10, 10, 10, 10, 5],
                          [0, 0, 0, 0, 0, 0, 0, 0]]

            self.qEval = [[-20, -10, -10, -5, -5, -10, -10, -20],
                          [-10, 0, 0, 0, 0, 0, 0, -10],
                          [-10, 0, 5, 5, 5, 5, 0, -10],
                          [-5, 0, 5, 5, 5, 5, 0, -5],
                          [0, 0, 5, 5, 5, 5, 0, -5],
                          [-10, 5, 5, 5, 5, 5, 0, -10],
                          [-10, 0, 5, 0, 0, 0, 0, -10],
                          [-20, -10, -10, -5, -5, -10, -10, -20]]

            self.QEval = [[-20, -10, -10, -5, -5, -10, -10, -20],
                          [-10, 0, 5, 0, 0, 0, 0, -10],
                          [-10, 5, 5, 5, 5, 5, 0, -10],
                          [0, 0, 5, 5, 5, 5, 0, -5],
                          [-5, 0, 5, 5, 5, 5, 0, -5],
                          [-10, 0, 5, 5, 5, 5, 0, -10],
                          [-10, 0, 0, 0, 0, 0, 0, -10],
                          [-20, -10, -10, -5, -5, -10, -10, -20]]

            self.kEval = [[-30, -40, -40, -50, -50, -40, -40, -30],
                          [-30, -40, -40, -50, -50, -40, -40, -30],
                          [-30, -40, -40, -50, -50, -40, -40, -30],
                          [-30, -40, -40, -50, -50, -40, -40, -30],
                          [-20, -30, -30, -40, -40, -30, -30, -20],
                          [-10, -20, -20, -20, -20, -20, -20, -10],
                          [20, 20, 0, 0, 0, 0, 20, 20],
                          [20, 30, 10, 0, 0, 10, 30, 20]]

            self.KEval = [[20, 30, 10, 0, 0, 10, 30, 20],
                          [20, 20, 0, 0, 0, 0, 20, 20],
                          [-10, -20, -20, -20, -20, -20, -20, -10],
                          [-20, -30, -30, -40, -40, -30, -30, -20],
                          [-30, -40, -40, -50, -50, -40, -40, -30],
                          [-30, -40, -40, -50, -50, -40, -40, -30],
                          [-30, -40, -40, -50, -50, -40, -40, -30],
                          [-30, -40, -40, -50, -50, -40, -40, -30]]

            self.mobility = 0
            self.bMobility = 0
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
        #self.testMoveMethodWhiteKnight()
        #self.testMoveMethodWhiteBishop()
        #self.testMoveMethodWhiteKing()
        #self.testMoveMethodWhiteQueen()


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

    def testMoveMethodWhiteBishop(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'B'):
                        print(self.grid[i][j].move(self))

    def testMoveMethodWhiteKing(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'K'):
                        print(self.grid[i][j].move(self))

    def testMoveMethodWhiteQueen(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] != None):
                    if(self.grid[i][j].id == 'Q'):
                        print(self.grid[i][j].move(self))

    def evaluationFunction(self):
        whiteCount = 0
        blackCount = 0

        for i in range(8):
            for j in range(8):
                if self.grid[i][j] != None:
                    if self.grid[i][j].color == 'w':
                        if self.grid[i][j].id == 'P':
                            whiteCount = whiteCount + 100
                            self.mobility = self.mobility + self.pEval[i][j]
                        elif self.grid[i][j].id == 'N':
                            whiteCount = whiteCount + 320
                            self.mobility = self.mobility + self.nEval[i][j]
                        elif self.grid[i][j].id == 'B':
                            whiteCount = whiteCount + 330
                            self.mobility = self.mobility + self.bEval[i][j]
                        elif self.grid[i][j].id == 'Q':
                            whiteCount = whiteCount + 900
                            self.mobility = self.mobility + self.qEval[i][j]
                        elif self.grid[i][j].id == 'R':
                            whiteCount = whiteCount + 500
                            self.mobility = self.mobility + self.rEval[i][j]
                        elif self.grid[i][j].id == 'K':
                            whiteCount = whiteCount + 20000
                            self.mobility = self.mobility + self.kEval[i][j]
                    if self.grid[i][j].color == 'b':
                        if self.grid[i][j].id == 'p':
                            blackCount = blackCount + 100
                            self.bMobility = self.bMobility + self.PEval[i][j]
                        elif self.grid[i][j].id == 'n':
                            blackCount = blackCount + 320
                            self.bMobility = self.bMobility + self.NEval[i][j]
                        elif self.grid[i][j].id == 'b':
                            blackCount = blackCount + 330
                            self.bMobility = self.bMobility + self.BEval[i][j]
                        elif self.grid[i][j].id == 'q':
                            blackCount = blackCount + 900
                            self.bMobility = self.bMobility + self.QEval[i][j]
                        elif self.grid[i][j].id == 'r':
                            blackCount = blackCount + 500
                            self.bMobility = self.bMobility + self.REval[i][j]
                        elif self.grid[i][j].id == 'k':
                            blackCount = blackCount + 20000
                            self.bMobility = self.bMobility + self.KEval[i][j]

        return(whiteCount - blackCount + self.mobility - self.bMobility) # STUB





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


