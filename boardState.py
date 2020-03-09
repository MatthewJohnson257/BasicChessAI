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

    qEval = [[-20,-10,-10, -5, -5,-10,-10,-20],
             [-10,  0,  0,  0,  0,  0,  0,-10],
             [-10,  0,  5,  5,  5,  5,  0,-10],
             [ -5,  0,  5,  5,  5,  5,  0, -5],
             [  0,  0,  5,  5,  5,  5,  0, -5],
             [-10,  5,  5,  5,  5,  5,  0,-10],
             [-10,  0,  5,  0,  0,  0,  0,-10],
             [-20,-10,-10, -5, -5,-10,-10,-20]]

    QEval = [[-20,-10,-10, -5, -5,-10,-10,-20],
             [-10,  0,  5,  0,  0,  0,  0,-10],
             [-10,  5,  5,  5,  5,  5,  0,-10],
             [  0,  0,  5,  5,  5,  5,  0, -5],
             [ -5,  0,  5,  5,  5,  5,  0, -5],
             [-10,  0,  5,  5,  5,  5,  0,-10],
             [-10,  0,  0,  0,  0,  0,  0,-10],
             [-20,-10,-10, -5, -5,-10,-10,-20]]

    kEval = [[-30,-40,-40,-50,-50,-40,-40,-30],
             [-30,-40,-40,-50,-50,-40,-40,-30],
             [-30,-40,-40,-50,-50,-40,-40,-30],
             [-30,-40,-40,-50,-50,-40,-40,-30],
             [-20,-30,-30,-40,-40,-30,-30,-20],
             [-10,-20,-20,-20,-20,-20,-20,-10],
             [ 20, 20,  0,  0,  0,  0, 20, 20],
             [ 20, 30, 10,  0,  0, 10, 30, 20]]

    KEval = [[ 20, 30, 10,  0,  0, 10, 30, 20],
             [ 20, 20,  0,  0,  0,  0, 20, 20],
             [-10,-20,-20,-20,-20,-20,-20,-10],
             [-20,-30,-30,-40,-40,-30,-30,-20],
             [-30,-40,-40,-50,-50,-40,-40,-30],
             [-30,-40,-40,-50,-50,-40,-40,-30],
             [-30,-40,-40,-50,-50,-40,-40,-30],
             [-30,-40,-40,-50,-50,-40,-40,-30]]

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
        self.evalValue = 0    #self.evaluationFunction()




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
                    elif self.grid[i][j] == 'H':
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
                    elif self.grid[i][j] == 'h':
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

        #self.mobility = 0.5*self.mobility
        #self.bMobility = 0.5*self.bMobility
        totalEvaluation = whiteCount - blackCount + self.whiteMobility + self.blackMobility
        
        #print("Eval: ", totalEvaluation)
        return(totalEvaluation)



    ###############################################################################
    #
    # Given a character and its coordinates, make call upon appropriate
    # corresponding move method for that particular piece
    #
    ###############################################################################
    def move(self, i, j, letter):
        if(letter == '_'):
            return([])
        elif(letter == 'P'):
            return(self.pPawnWhiteMoves(i, j))
        elif(letter == 'p'):
            return(self.pPawnBlackMoves(i, j))
        elif(letter == 'F'):
            return(self.fPawnWhiteMoves(i, j))
        elif(letter == 'f'):
            return(self.fPawnBlackMoves(i, j))
        elif(letter == 'S'):
            return(self.sPawnWhiteMoves(i, j))
        elif(letter == 's'):
            return(self.sPawnBlackMoves(i, j))
        elif(letter == 'Q'):
            return(self.qQueenWhiteMoves(i, j))
        elif(letter == 'q'):
            return(self.qQueenBlackMoves(i, j))
        elif(letter == 'K'):
            return(self.kKingWhiteMoves(i, j))
        elif(letter == 'k'):
            return(self.kKingBlackMoves(i, j))
        elif(letter == 'U'):
            return(self.uKingWhiteMoves(i, j))
        elif(letter == 'u'):
            return(self.uKingBlackMoves(i, j))
        elif(letter == 'B'):
            return(self.bBishopWhiteMoves(i, j))
        elif(letter == 'b'):
            return(self.bBishopBlackMoves(i, j))
        elif(letter == 'O'):
            return(self.oRookWhiteMoves(i, j))
        elif(letter == 'o'):
            return(self.oRookBlackMoves(i, j))
        elif(letter == 'L'):
            return(self.lRookWhiteMoves(i, j))
        elif(letter == 'l'):
            return(self.lRookBlackMoves(i, j))
        elif(letter == 'R'):
            return(self.rRookWhiteMoves(i, j))
        elif(letter == 'r'):
            return(self.rRookBlackMoves(i, j))
        elif(letter == 'H'):
            return(self.hKnightWhiteMoves(i, j))
        elif(letter == 'h'):
            return(self.hKnightBlackMoves(i, j))


    ###############################################################################
    #
    # Given a board, determine if the white king is in checkmate
    #
    ###############################################################################
    def isWhiteInCheckmate(self):
        for i in range(8):
            for j in range(8):
                coordList = self.move(i, j, self.grid[i][j])
                boardList = self.convertCoordsToBoards(i, j, coordList)
                for x in boardList:
                    if(x.isWhiteInCheck() == False):
                        return(False)
        return(True)
        

    ###############################################################################
    #
    # Given a board, determine if the black king is in checkmate
    #
    ###############################################################################
    def isBlackInCheckmate(self):
        for i in range(8):
            for j in range(8):
                coordList = self.move(i, j, self.grid[i][j])
                boardList = self.convertCoordsToBoards(i, j, coordList)
                for x in boardList:
                    if(x.isBlackInCheck() == False):
                        return(False)
        return(True)


    ###############################################################################
    #
    # Given a boardState, verify whether or not the black king is in check
    #
    ###############################################################################
    def isWhiteInCheck(self, testBoard):
        kingI = -1
        kingJ = -1

        # find the coordinates of the white king
        for i in range(8):
            for j in range(8):
                if(testBoard.grid[i][j] == 'K' or testBoard.grid[i][j] == 'U'):
                    kingI = i
                    kingJ = j
                    break
        
        # checks pawn to the upper left
        if(kingI > 0 and kingJ > 0 and (testBoard.grid[kingI - 1][kingJ - 1] in ['p', 'f', 's'])):
            return(True)

        # check pawn to the upper right
        if(kingI > 0 and kingJ < 0 and (testBoard.grid[kingI - 1][kingJ + 1] in ['p', 'f', 's'])):
            return(True)

        # check all surroundings for kings
        if(kingJ > 0 and (testBoard.grid[kingI][kingJ-1] == 'k' or testBoard.grid[kingI][kingJ-1] == 'u')):
            return(True)
        if(kingI > 0 and kingJ > 0 and (testBoard.grid[kingI-1][kingJ-1] == 'k' or testBoard.grid[kingI-1][kingJ-1] == 'u')):
            return(True)
        if(kingI > 0 and (testBoard.grid[kingI-1][kingJ] == 'k' or testBoard.grid[kingI-1][kingJ] == 'u')):
            return(True)
        if(kingI > 0 and kingJ < 7 and (testBoard.grid[kingI-1][kingJ+1] == 'k' or testBoard.grid[kingI-1][kingJ+1] == 'u')):
            return(True)
        if(kingJ < 7 and (testBoard.grid[kingI][kingJ+1] == 'k' or testBoard.grid[kingI][kingJ+1] == 'u')):
            return(True)
        if(kingI < 7 and kingJ < 7 and (testBoard.grid[kingI+1][kingJ+1] == 'k' or testBoard.grid[kingI+1][kingJ+1] == 'u')):
            return(True)
        if(kingI < 7 and (testBoard.grid[kingI+1][kingJ] == 'k' or testBoard.grid[kingI+1][kingJ] == 'u')):
            return(True)
        if(kingI < 7 and kingJ > 0 and (testBoard.grid[kingI+1][kingJ-1] == 'k' or testBoard.grid[kingI+1][kingJ-1] == 'u')):
            return(True)


        # check from horizontal left
        tempI = kingI
        tempJ = kingJ
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'l', 'o', 'r']):
                return(True)
            else:
                break
        
        # check from horizontal right
        tempI = kingI
        tempJ = kingJ
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'l', 'o', 'r']):
                return(True)
            else:
                break

        # check from vertical above
        tempI = kingI
        tempJ = kingJ
        while(tempI > 0):
            tempI = tempI - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'l', 'o', 'r']):
                return(True)
            else:
                break
        
        # check from vertical above
        tempI = kingI
        tempJ = kingJ
        while(tempI < 7):
            tempI = tempI + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'l', 'o', 'r']):
                return(True)
            else:
                break


        # check from diagonal upper left
        tempI = kingI
        tempJ = kingJ
        while(tempI > 0 and tempJ > 0):
            tempI = tempI - 1
            tempJ = tempJ - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'b']):
                return(True)
            else:
                break

        # check from diagonal upper right
        tempI = kingI
        tempJ = kingJ
        while(tempI > 0 and tempJ < 7):
            tempI = tempI - 1
            tempJ = tempJ + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'b']):
                return(True)
            else:
                break

        # check from diagonal lower left
        tempI = kingI
        tempJ = kingJ
        while(tempI < 7 and tempJ > 0):
            tempI = tempI + 1
            tempJ = tempJ - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'b']):
                return(True)
            else:
                break

        # check from diagonal lower right
        tempI = kingI
        tempJ = kingJ
        while(tempI < 7 and tempJ < 7):
            tempI = tempI + 1
            tempJ = tempJ + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['q', 'b']):
                return(True)
            else:
                break
        
        # check from knight
        if(kingI < 6 and kingJ < 7 and testBoard.grid[kingI + 2][kingJ + 1] == 'h'):
                return(True)
        if(kingI < 6 and kingJ > 0 and testBoard.grid[kingI + 2][kingJ - 1] == 'h'):
            return(True)
        if(kingI < 7 and kingJ < 6 and testBoard.grid[kingI + 1][kingJ + 2] == 'h'):
            return(True)
        if(kingI < 7 and kingJ > 1 and testBoard.grid[kingI + 1][kingJ - 2] == 'h'):
            return(True)
        if(kingI > 1 and kingJ < 7 and testBoard.grid[kingI - 2][kingJ + 1] == 'h'):
            return(True)
        if(kingI > 1 and kingJ > 0 and testBoard.grid[kingI - 2][kingJ - 1] == 'h'):
            return(True)
        if(kingI > 0 and kingJ > 1 and testBoard.grid[kingI - 1][kingJ - 2] == 'h'):
            return(True)
        if(kingI > 0 and kingJ < 1 and testBoard.grid[kingI - 1][kingJ + 2] == 'h'):
            return(True)


        # the white king is not in check
        return(False)

    ###############################################################################
    #
    # Given a boardState, verify whether or not the black king is in check
    #
    ###############################################################################
    def isBlackInCheck(self, testBoard):
        kingI = -1
        kingJ = -1

        # find the coordinates of the white king
        for i in range(8):
            for j in range(8):
                if(testBoard.grid[i][j] == 'k' or testBoard.grid[i][j] == 'u'):
                    kingI = i
                    kingJ = j
                    break
        
        # checks pawn to the lower left
        if(kingI < 7 and kingJ > 0 and (testBoard.grid[kingI + 1][kingJ - 1] in ['P', 'F', 'S'])):
            return(True)

        # check pawn to the lower right
        if(kingI < 7 and kingJ < 7 and (testBoard.grid[kingI + 1][kingJ + 1] in ['P', 'F', 'S'])):
            return(True)

        # check all surroundings for kings
        if(kingJ > 0 and (testBoard.grid[kingI][kingJ-1] in ['K', 'U'])):
            return(True)
        if(kingI > 0 and kingJ > 0 and (testBoard.grid[kingI-1][kingJ-1] in ['K', 'U'])):
            return(True)
        if(kingI > 0 and (testBoard.grid[kingI-1][kingJ] in ['K', 'U'])):
            return(True)
        if(kingI > 0 and kingJ < 7 and (testBoard.grid[kingI-1][kingJ+1] in ['K', 'U'])):
            return(True)
        if(kingJ < 7 and (testBoard.grid[kingI][kingJ+1] in ['K', 'U'])):
            return(True)
        if(kingI < 7 and kingJ < 7 and (testBoard.grid[kingI+1][kingJ+1] in ['K', 'U'])):
            return(True)
        if(kingI < 7 and (testBoard.grid[kingI+1][kingJ] in ['K', 'U'])):
            return(True)
        if(kingI < 7 and kingJ > 0 and (testBoard.grid[kingI+1][kingJ-1] in ['K', 'U'])):
            return(True)


        # check from horizontal left
        tempI = kingI
        tempJ = kingJ
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'L', 'O', 'R']):
                return(True)
            else:
                break
        
        # check from horizontal right
        tempI = kingI
        tempJ = kingJ
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'L', 'O', 'R']):
                return(True)
            else:
                break

        # check from vertical above
        tempI = kingI
        tempJ = kingJ
        while(tempI > 0):
            tempI = tempI - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'L', 'O', 'R']):
                return(True)
            else:
                break
        
        # check from vertical above
        tempI = kingI
        tempJ = kingJ
        while(tempI < 7):
            tempI = tempI + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'L', 'O', 'R']):
                return(True)
            else:
                break


        # check from diagonal upper left
        tempI = kingI
        tempJ = kingJ
        while(tempI > 0 and tempJ > 0):
            tempI = tempI - 1
            tempJ = tempJ - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'B']):
                return(True)
            else:
                break

        # check from diagonal upper right
        tempI = kingI
        tempJ = kingJ
        while(tempI > 0 and tempJ < 7):
            tempI = tempI - 1
            tempJ = tempJ + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'B']):
                return(True)
            else:
                break

        # check from diagonal lower left
        tempI = kingI
        tempJ = kingJ
        while(tempI < 7 and tempJ > 0):
            tempI = tempI + 1
            tempJ = tempJ - 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'B']):
                return(True)
            else:
                break

        # check from diagonal lower right
        tempI = kingI
        tempJ = kingJ
        while(tempI < 7 and tempJ < 7):
            tempI = tempI + 1
            tempJ = tempJ + 1
            if(testBoard.grid[tempI][tempJ] == '_'):
                continue
            elif((testBoard.grid[tempI][tempJ]).isupper()):
                break
            elif(testBoard.grid[tempI][tempJ] in ['Q', 'B']):
                return(True)
            else:
                break
        
        # check from knight
        if(kingI < 6 and kingJ < 7 and testBoard.grid[kingI + 2][kingJ + 1] == 'H'):
                return(True)
        if(kingI < 6 and kingJ > 0 and testBoard.grid[kingI + 2][kingJ - 1] == 'H'):
            return(True)
        if(kingI < 7 and kingJ < 6 and testBoard.grid[kingI + 1][kingJ + 2] == 'H'):
            return(True)
        if(kingI < 7 and kingJ > 1 and testBoard.grid[kingI + 1][kingJ - 2] == 'H'):
            return(True)
        if(kingI > 1 and kingJ < 7 and testBoard.grid[kingI - 2][kingJ + 1] == 'H'):
            return(True)
        if(kingI > 1 and kingJ > 0 and testBoard.grid[kingI - 2][kingJ - 1] == 'H'):
            return(True)
        if(kingI > 0 and kingJ > 1 and testBoard.grid[kingI - 1][kingJ - 2] == 'H'):
            return(True)
        if(kingI > 0 and kingJ < 1 and testBoard.grid[kingI - 1][kingJ + 2] == 'H'):
            return(True)


        # the black king is not in check
        return(False)

    
        

    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def generateAllWhiteMoves(self):

        ########################### NEED TO UPDATE THE S PAWNS ####################

        boardList = []
        for i in range(8):
            for j in range(8):
                if((self.grid[i][j]).isupper()):
                    tempCoords = self.move(i, j, self.grid[i][j])
                    tempBoards = self.convertCoordsToBoards(i, j, tempCoords)
                    for x in tempBoards:
                        if(x.isWhiteInCheck() == False):
                            boardList.append(x)
        return(boardList)       



    ###############################################################################
    #
    # 
    #
    ###############################################################################
    def generateAllBlackMoves(self):

        ########################### NEED TO UPDATE THE S PAWNS ####################

        boardList = []
        for i in range(8):
            for j in range(8):
                if((self.grid[i][j]).islower()):
                    tempCoords = self.move(i, j, self.grid[i][j])
                    tempBoards = self.convertCoordsToBoards(i, j, tempCoords)
                    for x in tempBoards:
                        if(x.isBlackInCheck() == False):
                            boardList.append(x)
        return(boardList)





    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an F pawn, not considering
    # leaving king in check
    #
    ###############################################################################
    def fPawnWhiteMoves(self, i , j):
        pawnCoordList = []

        # test if pawn can move two paces forward
        if(self.grid[i-1][j] == '_' and self.grid[i-2][j] == '_'):
            pawnCoordList.append([i-2, j, 8])

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            pawnCoordList.append([i-1, j, 8])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            pawnCoordList.append([i-1, j-1, 8])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            pawnCoordList.append([i-1, j+1, 8])

        return(pawnCoordList)




    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an f pawn, not considering
    # leaving king in check 
    #
    ###############################################################################
    def fPawnBlackMoves(self, i , j):
        pawnCoordList = []

        # test if pawn can move two paces forward
        if(self.grid[i+1][j] == '_' and self.grid[i+2][j] == '_'):
            pawnCoordList.append([i+2, j, 9])

        # if the pawn can move one space forward
        if(self.grid[i+1][j] == '_'):
            pawnCoordList.append([i+1, j, 9])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i+1][j-1]).isupper()):
            pawnCoordList.append([i+1, j-1, 9])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i+1][j+1]).isupper()):
            pawnCoordList.append([i+1, j+1, 9])

        return(pawnCoordList)



    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an S pawn, not considering
    # leaving king in check 
    #
    ###############################################################################
    def sPawnWhiteMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(self.grid[i-1][j] == '_'):
            pawnCoordList.append([i-1, j, 10])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i-1][j-1]).islower()):
            pawnCoordList.append([i-1, j-1, 10])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i-1][j+1]).islower()):
            pawnCoordList.append([i-1, j+1, 10])

        return(pawnCoordList)



    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an s pawn, not considering
    # leaving king in check 
    #
    ###############################################################################
    def sPawnBlackMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(self.grid[i+1][j] == '_'):
            pawnCoordList.append([i+1, j, 11])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and (self.grid[i+1][j-1]).isupper()):
            pawnCoordList.append([i+1, j-1, 11])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and (self.grid[i+1][j+1]).isupper()):
            pawnCoordList.append([i+1, j+1, 11])

        return(pawnCoordList)


    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a P pawn, not considering
    # leaving king in check 
    #
    ###############################################################################
    def pPawnWhiteMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(i != 1 and self.grid[i-1][j] == '_'):
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
    # Generate all viable coordinates for the moves of a p pawn, not considering
    # leaving king in check 
    #
    ###############################################################################
    def pPawnBlackMoves(self, i , j):
        pawnCoordList = []

        # if the pawn can move one space forward
        if(i != 6 and self.grid[i+1][j] == '_'):
            pawnCoordList.append([i+1, j, 0])

        # if the pawn can capture piece to the diagonal left
        if(j != 0 and i != 6 and (self.grid[i+1][j-1]).isupper()):
            pawnCoordList.append([i+1, j-1, 0])

        # if the pawn can capture piece to the diagonal right
        if(j != 7 and i != 6 and (self.grid[i+1][j+1]).isupper()):
            pawnCoordList.append([i+1, j+1, 0])

        # if the pawn will be promoted to a queen
        if(i == 6):
            if(j != 0 and (self.grid[i+1][j-1]).isupper()):
                pawnCoordList.append([i+1, j-1, 1])
            if(j != 7 and (self.grid[i+1][j+1]).isupper()):
                pawnCoordList.append([i+1, j+1, 1])
            if(self.grid[i+1][j] == '_'):
                pawnCoordList.append([i+1, j, 1])

        # en passant down left
        if(i == 4 and j != 0 and self.grid[i][j-1] == 'S'):
            pawnCoordList.append([i+1, j-1, 2])

        # en passant down right
        if(i == 4 and j != 7 and self.grid[i][j+1] == 'S'):
            pawnCoordList.append([i+1, j+1, 3])

        return(pawnCoordList)





    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a Q queen, not considering
    # leaving king in check  
    #
    ###############################################################################
    def qQueenWhiteMoves(self, i , j):
        coords = []

        # upwards moves
        tempI = i
        tempJ = j
        while(tempI > 0):
            tempI = tempI - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break
    
        # leftwards moves
        tempI = i
        tempJ = j
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downwards moves
        tempI = i
        tempJ = j 
        while(tempI < 7):
            tempI = tempI + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # rightwards moves
        tempI = i
        tempJ = j
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # upward right diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ < 7):
            tempI = tempI - 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # upward left diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ > 0):
            tempI = tempI - 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward right diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ < 7):
            tempI = tempI + 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward left diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ > 0):
            tempI = tempI + 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        
        return(coords)

    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a q queen, not considering
    # leaving king in check  
    #
    ###############################################################################
    def qQueenBlackMoves(self, i , j):
        coords = []

        # upwards moves
        tempI = i
        tempJ = j
        while(tempI > 0):
            tempI = tempI - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break
    
        # leftwards moves
        tempI = i
        tempJ = j
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downwards moves
        tempI = i
        tempJ = j 
        while(tempI < 7):
            tempI = tempI + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # rightwards moves
        tempI = i
        tempJ = j
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # upward right diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ < 7):
            tempI = tempI - 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # upward left diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ > 0):
            tempI = tempI - 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward right diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ < 7):
            tempI = tempI + 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward left diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ > 0):
            tempI = tempI + 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        return(coords)




    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a U king, not considering
    # leaving king in check   
    #
    ###############################################################################
    def uKingWhiteMoves(self, i , j):
        coords = []

        # regular moves 
        if(self.grid[i][j-1] == '_' or (self.grid[i][j-1]).islower()):
            coords.append([i, j-1, 12])
        if(self.grid[i-1][j-1] == '_' or (self.grid[i-1][j-1]).islower()):
            coords.append([i-1, j-1, 12])
        if(self.grid[i-1][j] == '_' or (self.grid[i-1][j]).islower()):
            coords.append([i-1, j, 12])
        if(self.grid[i-1][j+1] == '_' or (self.grid[i-1][j+1]).islower()):
            coords.append([i-1, j+1, 12])
        if(self.grid[i][j+1] == '_' or (self.grid[i][j+1]).islower()):
            coords.append([i, j+1, 12])

        # castle left
        if(self.grid[7][0] == 'L' and self.grid[7][1] == '_' and self.grid[7][2] == '_' and self.grid[7][3] == '_'):
            coords.append([7, 2, 6])

        # castle right
        if(self.grid[7][7] == 'O' and self.grid[7][6] == '_' and self.grid[7][5] == '_'):
            coords.append([7, 6, 7])


        return(coords)

    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a u king, not considering
    # leaving king in check   
    #
    ###############################################################################
    def uKingBlackMoves(self, i , j):
        coords = []

        # regular moves
        if(self.grid[i][j-1] == '_' or (self.grid[i][j-1]).isupper()):
            coords.append([i, j-1, 13])
        if(self.grid[i+1][j-1] == '_' or (self.grid[i+1][j-1]).isupper()):
            coords.append([i+1, j-1, 13])
        if(self.grid[i+1][j] == '_' or (self.grid[i+1][j]).isupper()):
            coords.append([i+1, j, 13])
        if(self.grid[i+1][j+1] == '_' or (self.grid[i+1][j+1]).isupper()):
            coords.append([i+1, j+1, 13])
        if(self.grid[i][j+1] == '_' or (self.grid[i][j+1]).isupper()):
            coords.append([i, j+1, 13])

        # castle left
        if(self.grid[0][0] == 'l' and self.grid[0][1] == '_' and self.grid[0][2] == '_' and self.grid[0][2] == '_'):
            coords.append([0, 2, 6])
        
        # castle right
        if(self.grid[0][7] == 'o' and self.grid[0][6] == '_' and self.grid[0][5] == '_'):
            coords.append([0, 6, 7])


        return(coords)





    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a K king, not considering
    # leaving king in check   
    #
    ###############################################################################
    def kKingWhiteMoves(self, i , j):
        coords = []

        if(j > 0 and (self.grid[i][j-1] == '_' or (self.grid[i][j-1]).islower())):
            coords.append([i, j-1, 0])
        if(i > 0 and j > 0 and (self.grid[i-1][j-1] == '_' or (self.grid[i-1][j-1]).islower())):
            coords.append([i-1, j-1, 0])
        if(i > 0 and (self.grid[i-1][j] == '_' or (self.grid[i-1][j]).islower())):
            coords.append([i-1, j, 0])
        if(i > 0 and j < 7 and (self.grid[i-1][j+1] == '_' or (self.grid[i-1][j+1]).islower())):
            coords.append([i-1, j+1, 0])
        if(j < 7 and (self.grid[i][j+1] == '_' or (self.grid[i][j+1]).islower())):
            coords.append([i, j+1, 0])
        if(i < 7 and j < 7 and (self.grid[i+1][j+1] == '_' or (self.grid[i+1][j+1]).islower())):
            coords.append([i+1, j+1, 0])
        if(i < 7 and (self.grid[i+1][j] == '_' or (self.grid[i+1][j]).islower())):
            coords.append([i+1, j, 0])
        if(i < 7 and j > 0 and (self.grid[i+1][j-1] == '_' or (self.grid[i+1][j-1]).islower())):
            coords.append([i+1, j-1, 0])
        
        return(coords)

    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a k king, not considering
    # leaving king in check  
    #
    ###############################################################################
    def kKingBlackMoves(self, i , j):
        coords = []

        if(j > 0 and (self.grid[i][j-1] == '_' or (self.grid[i][j-1]).isupper())):
            coords.append([i, j-1, 0])
        if(i > 0 and j > 0 and (self.grid[i-1][j-1] == '_' or (self.grid[i-1][j-1]).isupper())):
            coords.append([i-1, j-1, 0])
        if(i > 0 and (self.grid[i-1][j] == '_' or (self.grid[i-1][j]).isupper())):
            coords.append([i-1, j, 0])
        if(i > 0 and j < 7 and (self.grid[i-1][j+1] == '_' or (self.grid[i-1][j+1]).isupper())):
            coords.append([i-1, j+1, 0])
        if(j < 7 and (self.grid[i][j+1] == '_' or (self.grid[i][j+1]).isupper())):
            coords.append([i, j+1, 0])
        if(i < 7 and j < 7 and (self.grid[i+1][j+1] == '_' or (self.grid[i+1][j+1]).isupper())):
            coords.append([i+1, j+1, 0])
        if(i < 7 and (self.grid[i+1][j] == '_' or (self.grid[i+1][j]).isupper())):
            coords.append([i+1, j, 0])
        if(i < 7 and j > 0 and (self.grid[i+1][j-1] == '_' or (self.grid[i+1][j-1]).isupper())):
            coords.append([i+1, j-1, 0])

        return(coords)



    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a B bishop, not considering
    # leaving king in check  
    #
    ###############################################################################
    def bBishopWhiteMoves(self, i , j):
        coords = []

        # upward right diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ < 7):
            tempI = tempI - 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # upward left diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ > 0):
            tempI = tempI - 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward right diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ < 7):
            tempI = tempI + 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward left diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ > 0):
            tempI = tempI + 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

    
        return(coords)



    ###############################################################################
    #
    # Generate all viable coordinates for the moves of a b bishop, not considering
    # leaving king in check  
    #
    ###############################################################################
    def bBishopBlackMoves(self, i , j):
        coords = []

        # upward right diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ < 7):
            tempI = tempI - 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # upward left diagonal
        tempI = i
        tempJ = j 
        while(tempI > 0 and tempJ > 0):
            tempI = tempI - 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward right diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ < 7):
            tempI = tempI + 1
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downward left diagonal
        tempI = i
        tempJ = j 
        while(tempI < 7 and tempJ > 0):
            tempI = tempI + 1
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break


        return(coords)




    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an O rook, not considering
    # leaving king in check  
    #
    ###############################################################################
    def oRookWhiteMoves(self, i , j):
        coords = []
        
        # upwards moves
        tempI = i
        tempJ = j
        while(tempI > 0):
            tempI = tempI - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 14])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 14])
                break
            else:
                break
    
        # leftwards moves
        tempI = i
        tempJ = j
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 14])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 14])
                break
            else:
                break


        return(coords)


    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an o rook, not considering
    # leaving king in check 
    #
    ###############################################################################
    def oRookBlackMoves(self, i , j):
        coords = []
        
        # leftwards moves
        tempI = i
        tempJ = j
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 15])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 15])
                break
            else:
                break

        # downwards moves
        tempI = i
        tempJ = j 
        while(tempI < 7):
            tempI = tempI + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 15])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 15])
                break
            else:
                break

        return(coords)



    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an L rook, not considering
    # leaving king in check 
    #
    ###############################################################################
    def lRookWhiteMoves(self, i , j):
        coords = []

        # upwards moves
        tempI = i
        tempJ = j
        while(tempI > 0):
            tempI = tempI - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 16])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 16])
                break
            else:
                break

        # rightwards moves
        tempI = i
        tempJ = j
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 16])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 16])
                break
            else:
                break

        return(coords)

    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an l rook, not considering
    # leaving king in check 
    #
    ###############################################################################
    def lRookBlackMoves(self, i , j):
        coords = []

        # rightwards moves
        tempI = i
        tempJ = j
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 17])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 17])
                break
            else:
                break

        # downwards moves
        tempI = i
        tempJ = j 
        while(tempI < 7):
            tempI = tempI + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 17])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 17])
                break
            else:
                break

        return(coords)




    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an R rook, not considering
    # leaving king in check 
    #
    ###############################################################################
    def rRookWhiteMoves(self, i , j):
        coords = []

        # upwards moves
        tempI = i
        tempJ = j
        while(tempI > 0):
            tempI = tempI - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break
    
        # leftwards moves
        tempI = i
        tempJ = j
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downwards moves
        tempI = i
        tempJ = j 
        while(tempI < 7):
            tempI = tempI + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # rightwards moves
        tempI = i
        tempJ = j
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).islower()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        return(coords)

    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an r rook, not considering
    # leaving king in check 
    #
    ###############################################################################
    def rRookBlackMoves(self, i , j):
        coords = []

        # upwards moves
        tempI = i
        tempJ = j
        while(tempI > 0):
            tempI = tempI - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break
    
        # leftwards moves
        tempI = i
        tempJ = j
        while(tempJ > 0):
            tempJ = tempJ - 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # downwards moves
        tempI = i
        tempJ = j 
        while(tempI < 7):
            tempI = tempI + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        # rightwards moves
        tempI = i
        tempJ = j
        while(tempJ < 7):
            tempJ = tempJ + 1
            if(self.grid[tempI][tempJ] == '_'):
                coords.append([tempI, tempJ, 0])
            elif((self.grid[tempI][tempJ]).isupper()):
                coords.append([tempI, tempJ, 0])
                break
            else:
                break

        return(coords)




    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an H knight, not considering
    # leaving king in check 
    #
    ###############################################################################
    def hKnightWhiteMoves(self, i , j):
        coords = []

        if( i < 6 and j < 7 and ((self.grid[i+2][j+1] == '_' or (self.grid[i+2][j+1]).islower()))):
            coords.append([i+2,j+1, 0])
        if( i < 6 and j > 0 and ((self.grid[i+2][j-1] == '_' or (self.grid[i+2][j-1]).islower()))):
            coords.append([i+2,j-1, 0])
        if( i < 7 and j < 6 and ((self.grid[i+1][j+2] == '_' or (self.grid[i+1][j+2]).islower()))):
            coords.append([i+1,j+2, 0])
        if( i < 7 and j > 1 and ((self.grid[i+1][j-2] == '_' or (self.grid[i+1][j-2]).islower()))):
            coords.append([i+1,j-2, 0])
        if( i > 1 and j < 7 and ((self.grid[i-2][j+1] == '_' or (self.grid[i-2][j+1]).islower()))):
            coords.append([i-2,j+1, 0])
        if( i > 1 and j > 0 and ((self.grid[i-2][j-1] == '_' or (self.grid[i-2][j-1]).islower()))):
            coords.append([i-2,j-1, 0])
        if( i > 0 and j > 1 and ((self.grid[i-1][j-2] == '_' or (self.grid[i-1][j-2]).islower()))):
            coords.append([i-1,j-2, 0])
        if( i > 0 and j < 6 and ((self.grid[i-1][j+2] == '_' or (self.grid[i-1][j+2]).islower()))):
            coords.append([i-1,j+2, 0])


        return(coords)

    ###############################################################################
    #
    # Generate all viable coordinates for the moves of an h knight, not considering
    # leaving king in check 
    #
    ###############################################################################
    def hKnightBlackMoves(self, i , j):
        coords = []

        if( i < 6 and j < 7 and ((self.grid[i+2][j+1] == '_' or (self.grid[i+2][j+1]).isupper()))):
            coords.append([i+2,j+1, 0])
        if( i < 6 and j > 0 and ((self.grid[i+2][j-1] == '_' or (self.grid[i+2][j-1]).isupper()))):
            coords.append([i+2,j-1, 0])
        if( i < 7 and j < 6 and ((self.grid[i+1][j+2] == '_' or (self.grid[i+1][j+2]).isupper()))):
            coords.append([i+1,j+2, 0])
        if( i < 7 and j > 1 and ((self.grid[i+1][j-2] == '_' or (self.grid[i+1][j-2]).isupper()))):
            coords.append([i+1,j-2, 0])
        if( i > 1 and j < 7 and ((self.grid[i-2][j+1] == '_' or (self.grid[i-2][j+1]).isupper()))):
            coords.append([i-2,j+1, 0])
        if( i > 1 and j > 0 and ((self.grid[i-2][j-1] == '_' or (self.grid[i-2][j-1]).isupper()))):
            coords.append([i-2,j-1, 0])
        if( i > 0 and j > 1 and ((self.grid[i-1][j-2] == '_' or (self.grid[i-1][j-2]).isupper()))):
            coords.append([i-1,j-2, 0])
        if( i > 0 and j < 6 and ((self.grid[i-1][j+2] == '_' or (self.grid[i-1][j+2]).isupper()))):
            coords.append([i-1,j+2, 0])

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
    # Takes viable coordinates for any piece moving, can converts a list of those
    # coordinates into a list of corresponding new boardStates that reflect 
    # those moves after they take place
    #
    ###############################################################################
    def convertCoordsToBoards(self, i, j, coords):
        boardList = []
        tempGrid = []

        for x in coords:
            tempGrid = copy.deepcopy(self.grid)

            # regular move
            if(x[2] == 0):
                tempGrid[x[0]][x[1]] = tempGrid[i][j]
                tempGrid[i][j] = '_'
                boardList.append(boardState(tempGrid))
            
            else:
                # pawn promotion
                if(x[2] == 1):

                    # white pawn
                    if(i == 1):
                        tempGrid[x[0]][x[1]] = 'Q'

                    # black pawn
                    else:
                        tempGrid[x[0]][x[1]] = 'q'
                    
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # en passant down left
                elif(x[2] == 2):
                    tempGrid[x[0]][x[1]] = 'p'
                    tempGrid[i][j-1] = '_'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # en passant down right
                elif(x[2] == 3):
                    tempGrid[x[0]][x[1]] = 'p'
                    tempGrid[i][j+1] = '_'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # en passant up left
                elif(x[2] == 4):
                    tempGrid[x[0]][x[1]] = 'P'
                    tempGrid[i][j-1] = '_'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))
                
                # en passant up right
                elif(x[2] == 5):
                    tempGrid[x[0]][x[1]] = 'P'
                    tempGrid[i][j+1] = '_'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # castle left
                elif(x[2] == 6):

                    # white king
                    if(i == 7):
                        tempGrid[x[0]][x[1]] = 'K'
                        tempGrid[i][j-1] = 'R'

                    # black king
                    else:
                        tempGrid[x[0]][x[1]] = 'k'
                        tempGrid[i][j-1] = 'r'

                    tempGrid[i][0] = '_'
                    tempGrid[i][j] = '_' 
                    boardList.append(boardState(tempGrid))

                # castle right
                elif(x[2] == 7):
                    
                    # white king
                    if(i == 7):
                        tempGrid[x[0]][x[1]] = 'K'
                        tempGrid[i][j+1] = 'R'

                    # black king
                    else:
                        tempGrid[x[0]][x[1]] = 'k'
                        tempGrid[i][j+1] = 'r'
                    
                    tempGrid[i][7] = '_'
                    tempGrid[i][j] = '_' 
                    boardList.append(boardState(tempGrid))

                # F pawn move
                elif(x[2] == 8):
                    tempGrid[x[0]][x[1]] = 'S'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # f pawn move
                elif(x[2] == 9):
                    tempGrid[x[0]][x[1]] = 's'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # S pawn move
                elif(x[2] == 10):
                    tempGrid[x[0]][x[1]] = 'P'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # s pawn move
                elif(x[2] == 11):
                    tempGrid[x[0]][x[1]] = 'p'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # U king move
                elif(x[2] == 12):
                    tempGrid[x[0]][x[1]] = 'K'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # u king move
                elif(x[2] == 13):
                    tempGrid[x[0]][x[1]] = 'k'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # O rook move
                elif(x[2] == 14):
                    tempGrid[x[0]][x[1]] = 'R'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # o rook move
                elif(x[2] == 15):
                    tempGrid[x[0]][x[1]] = 'r'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # L rook move
                elif(x[2] == 16):
                    tempGrid[x[0]][x[1]] = 'R'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))

                # l rook move
                elif(x[2] == 17):
                    tempGrid[x[0]][x[1]] = 'r'
                    tempGrid[i][j] = '_'
                    boardList.append(boardState(tempGrid))


        return(boardList)