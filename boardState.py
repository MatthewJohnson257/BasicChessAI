###############################################################################
#
#   boardState.py
#
############################################################################### 

import copy

class boardState():


    pEval = [[  0,  0,  0,  0,  0,  0,  0,  0],
             [ 50, 50, 50, 50, 50, 50, 50, 50],
             [ 10, 10, 20, 30, 30, 20, 10, 10],
             [  5,  5, 10, 25, 25, 10,  5,  5],
             [  0,  0,  0, 20, 20,  0,  0,  0],
             [  5, -5,-10,  0,  0,-10, -5,  5],
             [  5, 10, 10,-20,-20, 10, 10,  5],
             [  0,  0,  0,  0,  0,  0,  0,  0]]

    PEval = [[  0,  0,  0,  0,  0,  0,  0,  0],
             [  5, 10, 10,-20,-20, 10, 10,  5],
             [  5, -5,-10,  0,  0,-10, -5,  5],
             [  0,  0,  0, 20, 20,  0,  0,  0],
             [  5,  5, 10, 25, 25, 10,  5,  5],
             [ 10, 10, 20, 30, 30, 20, 10, 10],
             [ 50, 50, 50, 50, 50, 50, 50, 50],
             [  0,  0,  0,  0,  0,  0,  0,  0]]

    nEval = [[-50,-40,-30,-30,-30,-30,-40,-50],
             [-40,-20,  0,  0,  0,  0,-20,-40],
             [-30,  0, 10, 15, 15, 10,  0,-30],
             [-30,  5, 15, 20, 20, 15,  5,-30],
             [-30,  0, 15, 20, 20, 15,  0,-30],
             [-30,  5, 10, 15, 15, 10,  5,-30],
             [-40,-20,  0,  5,  5,  0,-20,-40],
             [-50,-40,-30,-30,-30,-30,-40,-50]]

    NEval = [[-50, -40, -30, -30, -30, -30, -40, -50],
             [-40, -20, 0, 5, 5, 0, -20, -40],
             [-30, 5, 10, 15, 15, 10, 5, -30],
             [-30, 0, 15, 20, 20, 15, 0, -30],
             [-30, 5, 15, 20, 20, 15, 5, -30],
             [-30, 0, 10, 15, 15, 10, 0, -30],
             [-40, -20, 0, 0, 0, 0, -20, -40],
             [-50, -40, -30, -30, -30, -30, -40, -50]]

    bEval = [[-20, -10, -10, -10, -10, -10, -10, -20],
             [-10, 0, 0, 0, 0, 0, 0, -10],
             [-10, 0, 5, 10, 10, 5, 0, -10],
             [-10, 5, 5, 10, 10, 5, 5, -10],
             [-10, 0, 10, 10, 10, 10, 0, -10],
             [-10, 10, 10, 10, 10, 10, 10, -10],
             [-10, 5, 0, 0, 0, 0, 5, -10],
             [-20, -10, -10, -10, -10, -10, -10, -20]]

    BEval = [[-20, -10, -10, -10, -10, -10, -10, -20],
             [-10, 5, 0, 0, 0, 0, 5, -10],
             [-10, 10, 10, 10, 10, 10, 10, -10],
             [-10, 0, 10, 10, 10, 10, 0, -10],
             [-10, 5, 5, 10, 10, 5, 5, -10],
             [-10, 0, 5, 10, 10, 5, 0, -10],
             [-10, 0, 0, 0, 0, 0, 0, -10],
             [-20, -10, -10, -10, -10, -10, -10, -20]]

    rEval = [[0, 0, 0, 0, 0, 0, 0, 0],
             [5, 10, 10, 10, 10, 10, 10, 5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [0, 0, 0, 5, 5, 0, 0, 0]]

    REval = [[0, 0, 0, 5, 5, 0, 0, 0],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [-5, 0, 0, 0, 0, 0, 0, -5],
             [5, 10, 10, 10, 10, 10, 10, 5],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    qEval = [[-20, -10, -10, -5, -5, -10, -10, -20],
             [-10, 0, 0, 0, 0, 0, 0, -10],
             [-10, 0, 5, 5, 5, 5, 0, -10],
             [-5, 0, 5, 5, 5, 5, 0, -5],
             [0, 0, 5, 5, 5, 5, 0, -5],
             [-10, 5, 5, 5, 5, 5, 0, -10],
             [-10, 0, 5, 0, 0, 0, 0, -10],
             [-20, -10, -10, -5, -5, -10, -10, -20]]

    QEval = [[-20, -10, -10, -5, -5, -10, -10, -20],
             [-10, 0, 5, 0, 0, 0, 0, -10],
             [-10, 5, 5, 5, 5, 5, 0, -10],
             [0, 0, 5, 5, 5, 5, 0, -5],
             [-5, 0, 5, 5, 5, 5, 0, -5],
             [-10, 0, 5, 5, 5, 5, 0, -10],
             [-10, 0, 0, 0, 0, 0, 0, -10],
             [-20, -10, -10, -5, -5, -10, -10, -20]]

    kEval = [[-30, -40, -40, -50, -50, -40, -40, -30],
             [-30, -40, -40, -50, -50, -40, -40, -30],
             [-30, -40, -40, -50, -50, -40, -40, -30],
             [-30, -40, -40, -50, -50, -40, -40, -30],
             [-20, -30, -30, -40, -40, -30, -30, -20],
             [-10, -20, -20, -20, -20, -20, -20, -10],
             [20, 20, 0, 0, 0, 0, 20, 20],
             [20, 30, 10, 0, 0, 10, 30, 20]]

    KEval = [[20, 30, 10, 0, 0, 10, 30, 20],
             [20, 20, 0, 0, 0, 0, 20, 20],
             [-10, -20, -20, -20, -20, -20, -20, -10],
             [-20, -30, -30, -40, -40, -30, -30, -20],
             [-30, -40, -40, -50, -50, -40, -40, -30],
             [-30, -40, -40, -50, -50, -40, -40, -30],
             [-30, -40, -40, -50, -50, -40, -40, -30],
             [-30, -40, -40, -50, -50, -40, -40, -30]]

    ###############################################################################
    #
    # constructor for a boardState object
    #
    ###############################################################################
    def __init__(self, grid, whiteInCheck = False, blackInCheck = False):
        self.grid = grid                        # board of pieces
        self.whiteInCheck = whiteInCheck
        self.blackInCheck = blackInCheck
        self.whiteMobility = 0                  # used for eval function            
        self.blackMobility = 0                  # used for eval function
        self.evalValue = self.evaluationFunction()




    ###############################################################################
    #
    # takes a board, returns its evaluation value, used in alpha beta pruning
    #
    ###############################################################################
    def evaluationFunction(self):
        whiteCount = 0
        blackCount = 0 
        totalEvaluation = 0

        for i in range(8):
            for j in range(8):
                if self.grid[i][j] != '_':
                    if self.grid[i][j] == 'P':
                        whiteCount = whiteCount + 100
                        self.whiteMobility = self.whiteMobility + boardState.pEval[i][j]
                    elif self.grid[i][j] == 'N':
                        whiteCount = whiteCount + 320
                        self.whiteMobility = self.whiteMobility + boardState.nEval[i][j]
                    elif self.grid[i][j] == 'B':
                        whiteCount = whiteCount + 330
                        self.whiteMobility = self.whiteMobility + boardState.bEval[i][j]
                    elif self.grid[i][j] == 'Q':
                        whiteCount = whiteCount + 900
                        self.whiteMobility = self.whiteMobility + boardState.qEval[i][j]
                    elif self.grid[i][j] == 'R':
                        whiteCount = whiteCount + 500
                        self.whiteMobility = self.whiteMobility + boardState.rEval[i][j]
                    elif self.grid[i][j] == 'K':
                        whiteCount = whiteCount + 20000
                        self.whiteMobility = self.whiteMobility + boardState.kEval[i][j]
                    elif self.grid[i][j] == 'p':
                        blackCount = blackCount + 100
                        self.blackMobility = self.blackMobility + boardState.rEval[i][j]
                    elif self.grid[i][j] == 'n':
                        blackCount = blackCount + 320
                        self.blackMobility = self.blackMobility + boardState.rEval[i][j]
                    elif self.grid[i][j] == 'b':
                        blackCount = blackCount + 330
                        self.blackMobility = self.blackMobility + boardState.rEval[i][j]
                    elif self.grid[i][j] == 'q':
                        blackCount = blackCount + 900
                        self.blackMobility = self.blackMobility + boardState.rEval[i][j]
                    elif self.grid[i][j] == 'r':
                        blackCount = blackCount + 500
                        self.blackMobility = self.blackMobility + boardState.rEval[i][j]
                    elif self.grid[i][j] == 'k':
                        blackCount = blackCount + 20000
                        self.blackMobility = self.blackMobility + boardState.rEval[i][j]

        if(self.isWhiteInCheckmate()): 
            return(-100000)
        if(self.isBlackInCheckmate()):
            return(100000)

        self.mobility = 0.5*self.mobility
        self.bMobility = 0.5*self.bMobility
        totalEvaluation = whiteCount - blackCount + self.whiteMobility + self.blackMobility
        
        #print("Eval: ", totalEvaluation)
        return(totalEvaluation)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def isWhiteInCheckmate(self):
        tempList = self.generateAllWhiteMoves()
        if(len(tempList) == 0):
            return(True)
        else:
            return(False)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def isBlackInCheckmate(self):
        tempList = self.generateAllBlackMoves()
        if(len(tempList) == 0):
            return(True)
        else:
            return(False)
        

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def generateAllWhiteMoves(self):
        boardList = []
        # for i in range(8):
        #     for j in range(8):
        #         if(self.grid[i][j] == 'P'):

        return(boardList)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def generateAllBlackMoves(self):
        boardList = []
        return(boardList)





    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def fPawnWhiteMoves(self, i , j):
        pawnMoveList = []
        tempGrid = []

        # test if pawn can move two paces forward
        if(self.grid[i-1][j] == '_' and self.grid[i-2][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-2][j] = 'S'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j-1] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j+1] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # for x in pawnMoveList:
        #     x.printBoard()

        return(pawnMoveList)




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def fPawnBlackMoves(self, i , j):
        pawnMoveList = []
        tempGrid = []

        # test if pawn can move two paces forward
        if(self.grid[i+1][j] == '_' and self.grid[i+2][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+2][j] = 's'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can move one space forward
        if(self.grid[i+1][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+1][j] = 'p'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i+1][j-1]).isupper()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+1][j-1] = 'p'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i+1][j+1]).isupper()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+1][j+1] = 'p'
            pawnMoveList.append(boardState(tempGrid))

        # for x in pawnMoveList:
        #     x.printBoard()

        return(pawnMoveList)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def sPawnWhiteMoves(self, i , j):
        pawnMoveList = []
        tempGrid = []

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j-1] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j+1] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # for x in pawnMoveList:
        #     x.printBoard()

        return(pawnMoveList)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def sPawnBlackMoves(self, i , j):
        pawnMoveList = []
        tempGrid = []

        # if the pawn can move one space forward
        if(self.grid[i+1][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+1][j] = 'p'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i+1][j-1]).isupper()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+1][j-1] = 'p'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i+1][j+1]).isupper()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i+1][j+1] = 'p'
            pawnMoveList.append(boardState(tempGrid))

        # for x in pawnMoveList:
        #     x.printBoard()

        return(pawnMoveList)


    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def pPawnWhiteMoves(self, i , j):
        pawnMoveList = []
        tempGrid = []

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j-1] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[i][j] = '_'
            tempGrid[i-1][j+1] = 'P'
            pawnMoveList.append(boardState(tempGrid))

        # if the pawn will be promoted to a queen
        if()

        # for x in pawnMoveList:
        #     x.printBoard()

        return(pawnMoveList)





    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def pPawnBlackMoves(self, i , j):
        stub = 1



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def qQueenWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def qQueenBlackMoves(self, i , j):
        stub = 1




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def uKingWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def uKingBlackMoves(self, i , j):
        stub = 1






    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def kKingWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def kKingBlackMoves(self, i , j):
        stub = 1




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def bBishopWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def bBishopBlackMoves(self, i , j):
        stub = 1





    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def oRookWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def oRookBlackMoves(self, i , j):
        stub = 1




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def lRookWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def lRookBlackMoves(self, i , j):
        stub = 1





    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def rRookWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def rRookBlackMoves(self, i , j):
        stub = 1







    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def hKnightWhiteMoves(self, i , j):
        stub = 1

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def hKnightBlackMoves(self, i , j):
        stub = 1














    ###############################################################################
    #
    # takes in a board, and prints to output a character representation of that 
    # board to standard output
    #
    ###############################################################################
    def printBoard(self):
        print("    ◘----------------◘")
        for i in range(0,8):
            print('    |', end = '')
            for j in range(0,8):
                if(self.grid[i][j] == '_'):
                    print(" ", end = ' ')
                else:
                    print(self.grid[i][j], end = ' ')
            print('|', end = '')
            print()
        print("    ◘----------------◘")

    