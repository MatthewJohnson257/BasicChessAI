###############################################################################
#
#   boardState.py
#
############################################################################### 


class boardState():


    pEval = [[  0,  0,  0,  0,  0,  0,  0,  0],
             [50, 50, 50, 50, 50, 50, 50, 50],
             [10, 10, 20, 30, 30, 20, 10, 10],
             [5, 5, 10, 25, 25, 10, 5, 5],
             [0, 0, 0, 20, 20, 0, 0, 0],
             [5, -5, -10, 0, 0, -10, -5, 5],
             [5, 10, 10, -20, -20, 10, 10, 5],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    PEval = [[0, 0, 0, 0, 0, 0, 0, 0],
             [5, 10, 10, -20, -20, 10, 10, 5],
             [5, -5, -10, 0, 0, -10, -5, 5],
             [0, 0, 0, 20, 20, 0, 0, 0],
             [5, 5, 10, 25, 25, 10, 5, 5],
             [10, 10, 20, 30, 30, 20, 10, 10],
             [50, 50, 50, 50, 50, 50, 50, 50],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    nEval = [[-50, -40, -30, -30, -30, -30, -40, -50],
             [-40, -20, 0, 0, 0, 0, -20, -40],
             [-30, 0, 10, 15, 15, 10, 0, -30],
             [-30, 5, 15, 20, 20, 15, 5, -30],
             [-30, 0, 15, 20, 20, 15, 0, -30],
             [-30, 5, 10, 15, 15, 10, 5, -30],
             [-40, -20, 0, 5, 5, 0, -20, -40],
             [-50, -40, -30, -30, -30, -30, -40, -50]]

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
                        self.whiteMobility = self.whiteMobility + Board.pEval[i][j]
                    elif self.grid[i][j] == 'N':
                        whiteCount = whiteCount + 320
                        self.whiteMobility = self.whiteMobility + Board.nEval[i][j]
                    elif self.grid[i][j] == 'B':
                        whiteCount = whiteCount + 330
                        self.whiteMobility = self.whiteMobility + Board.bEval[i][j]
                    elif self.grid[i][j] == 'Q':
                        whiteCount = whiteCount + 900
                        self.whiteMobility = self.whiteMobility + Board.qEval[i][j]
                    elif self.grid[i][j] == 'R':
                        whiteCount = whiteCount + 500
                        self.whiteMobility = self.whiteMobility + Board.rEval[i][j]
                    elif self.grid[i][j] == 'K':
                        whiteCount = whiteCount + 20000
                        self.whiteMobility = self.whiteMobility + Board.kEval[i][j]
                    elif self.grid[i][j] == 'p':
                        blackCount = blackCount + 100
                        self.blackMobility = self.blackMobility + Board.rEval[i][j]
                    elif self.grid[i][j] == 'n':
                        blackCount = blackCount + 320
                        self.blackMobility = self.blackMobility + Board.rEval[i][j]
                    elif self.grid[i][j] == 'b':
                        blackCount = blackCount + 330
                        self.blackMobility = self.blackMobility + Board.rEval[i][j]
                    elif self.grid[i][j] == 'q':
                        blackCount = blackCount + 900
                        self.blackMobility = self.blackMobility + Board.rEval[i][j]
                    elif self.grid[i][j] == 'r':
                        blackCount = blackCount + 500
                        self.blackMobility = self.blackMobility + Board.rEval[i][j]
                    elif self.grid[i][j] == 'k':
                        blackCount = blackCount + 20000
                        self.blackMobility = self.blackMobility + Board.rEval[i][j]

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

    