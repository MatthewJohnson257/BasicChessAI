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

    NEval = [[-50,-40,-30,-30,-30,-30,-40,-50],
             [-40,-20,  0,  5,  5,  0,-20,-40],
             [-30,  5, 10, 15, 15, 10,  5,-30],
             [-30,  0, 15, 20, 20, 15,  0,-30],
             [-30,  5, 15, 20, 20, 15,  5,-30],
             [-30,  0, 10, 15, 15, 10,  0,-30],
             [-40,-20,  0,  0,  0,  0,-20,-40],
             [-50,-40,-30,-30,-30,-30,-40,-50]]

    bEval = [[-20,-10,-10,-10,-10,-10,-10,-20],
             [-10,  0,  0,  0,  0,  0,  0,-10],
             [-10,  0,  5, 10, 10,  5,  0,-10],
             [-10,  5,  5, 10, 10,  5,  5,-10],
             [-10,  0, 10, 10, 10, 10,  0,-10],
             [-10, 10, 10, 10, 10, 10, 10,-10],
             [-10,  5,  0,  0,  0,  0,  5,-10],
             [-20,-10,-10,-10,-10,-10,-10,-20]]

    BEval = [[-20,-10,-10,-10,-10,-10,-10,-20],
             [-10,  5,  0,  0,  0,  0,  5,-10],
             [-10, 10, 10, 10, 10, 10, 10,-10],
             [-10,  0, 10, 10, 10, 10,  0,-10],
             [-10,  5,  5, 10, 10,  5,  5,-10],
             [-10,  0,  5, 10, 10,  5,  0,-10],
             [-10,  0,  0,  0,  0,  0,  0,-10],
             [-20,-10,-10,-10,-10,-10,-10,-20]]

    rEval = [[  0,  0,  0,  0,  0,  0,  0,  0],
             [  5, 10, 10, 10, 10, 10, 10,  5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [  0,  0,  0,  5,  5,  0,  0,  0]]

    REval = [[  0,  0,  0,  5,  5,  0,  0,  0],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [ -5,  0,  0,  0,  0,  0,  0, -5],
             [  5, 10, 10, 10, 10, 10, 10,  5],
             [  0,  0,  0,  0,  0,  0,  0,  0]]

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
        pawnCoordList = []

        # test if pawn can move two paces forward
        if(self.grid[i-1][j] == '_' and self.grid[i-2][j] == '_'):
            pawnCoordList.append([i-2, j, 0])

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            pawnCoordList.append([i-1, j, 0])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            pawnCoordList.append([i-1, j-1, 0])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            pawnCoordList.append([i-1, j+1, 0])

        return(pawnCoordList)




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def fPawnBlackMoves(self, i , j):
        pawnCoordList = []

        # test if pawn can move two paces forward
        if(self.grid[i+1][j] == '_' and self.grid[i+2][j] == '_'):
            pawnCoordList.append([i+2, j, 0])

        # if the pawn can move one space forward
        if(self.grid[i+1][j] == '_'):
            pawnCoordList.append([i+1, j, 0])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i+1][j-1]).isupper()):
            pawnCoordList.append([i+1, j-1, 0])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i+1][j+1]).isupper()):
            pawnCoordList.append([i+1, j+1, 0])

        return(pawnCoordList)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def sPawnWhiteMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            pawnCoordList.append([i-1, j, 0])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            pawnCoordList.append([i-1, j-1, 0])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            pawnCoordList.append([i-1, j+1, 0])

        return(pawnCoordList)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def sPawnBlackMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(self.grid[i+1][j] == '_'):
            pawnCoordList.append([i+1, j, 0])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i+1][j-1]).isupper()):
            pawnCoordList.append([i+1, j-1, 0])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i+1][j+1]).isupper()):
            pawnCoordList.append([i+1, j+1, 0])


        return(pawnCoordList)


    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def pPawnWhiteMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            pawnCoordList.append([i-1, j, 0])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and i != 1 and (self.grid[i-1][j-1]).islower()):
            pawnCoordList.append([i-1, j-1, 0])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and i != 1 and (self.grid[i-1][j+1]).islower()):
            pawnCoordList.append([i-1, j+1, 0])

        # if the pawn will be promoted to a queen
        if(i == 1):
            if(j != 0 and (self.grid[i-1][j-1]).islower()):
                pawnCoordList.append([i-1, j-1, 1])
            if(j != 7 and (self.grid[i-1][j+1]).islower()):
                pawnCoordList.append([i-1, j+1, 1])
            if(self.grid[i-1][j] == '_'):
                pawnCoordList.append([i-1, j, 1])

        # en passant up left
        if(i == 3 and j != 0 and self.grid[i][j-1] == 's'):
            pawnCoordList.append([i-1, j-1, 4])

        # en passant up right
        if(i == 3 and j != 7 and self.grid[i][j+1] == 's'):
            pawnCoordList.append([i-1, j+1, 5])

        return(pawnCoordList)





    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def pPawnBlackMoves(self, i , j):
        coords = []
        return(coords)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def qQueenWhiteMoves(self, i , j):
        coords = []
        return(coords)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def qQueenBlackMoves(self, i , j):
        coords = []
        return(coords)




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
        coords = []
        return(coords)





    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def kKingWhiteMoves(self, i , j):
        coords = []
        return(coords)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def kKingBlackMoves(self, i , j):
        coords = []
        return(coords)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def bBishopWhiteMoves(self, i , j):
        coords = []
        return(coords)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def bBishopBlackMoves(self, i , j):
        coords = []
        return(coords)




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def oRookWhiteMoves(self, i , j):
        coords = []
        return(coords)
    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def oRookBlackMoves(self, i , j):
        coords = []
        return(coords)



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def lRookWhiteMoves(self, i , j):
        coords = []
        return(coords)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def lRookBlackMoves(self, i , j):
        coords = []
        return(coords)




    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def rRookWhiteMoves(self, i , j):
        coords = []
        return(coords)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def rRookBlackMoves(self, i , j):
        coords = []
        return(coords)






    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def hKnightWhiteMoves(self, i , j):
        coords = []
        return(coords)

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def hKnightBlackMoves(self, i , j):
        coords = []
        return(coords)













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

    




    

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def convertCoordsToBoards(self, i, j, coords):
        boardList = []
        tempGrid = []

        for x in coords:
            tempGrid = copy.deepcopy(self.grid)

            # regular move
            if(coords[2] == 0):
                stub = 1
            
            # pawn promotion
            elif(coords[2] == 1):
                stub = 1

            # en passant down left
            elif(coords[2] == 2):
                stub = 1

            # en passant down right
            elif(coords[2] == 3):
                stub = 1

            # en passant up left
            elif(coords[2] == 4):
                stub = 1
            
            # en passant up right
            elif(coords[2] == 5):
                stub = 1

            # castle left
            elif(coords[2] == 6):
                stub = 1

            # castle right
            elif(coords[2] == 7):
                stub = 1

        #return(boardList)