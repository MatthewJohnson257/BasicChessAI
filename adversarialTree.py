###############################################################################
#
# 
#
###############################################################################
class adversarialTree():

    ###############################################################################
    #  
    # 
    #
    ###############################################################################
    def __init__(self, initialBoard, depth, initialColor = 'w'):
        self.initialBoard = initialBoard        # current board
        self.initialColor = initialColor        # AI color
        self.depth = depth

    
    ###############################################################################
    #  
    # 
    #
    ###############################################################################
    def maxNode(self, parentBoard, alpha, beta, color, depth):
        if(depth == self.depth):
            return(parentBoard)
        else:
            v = -999999999

            # if the color of the player at the maximizer is white
            if(color == 'w'):
                children = parentBoard.generateAllWhiteMoves()
                tempChild = None
                if(len(children) == 0):
                    print("this happens 1")
                    return(parentBoard)
                for x in children:

                     # checks for an early checkmate and prioritizes that move
                    if(depth == 0):
                        if(x.isBlackInCheckmate()):
                            print("This is checkmate.")
                            return(x)
                                       
                    # calls minimizer node if maximum depth has not yet been reached
                    nextLevel = self.minNode(x, alpha, beta, 'b', depth + 1)
                    v = max(v, nextLevel.evaluationFunction())#, parentBoard.evaluationFunction())
                    #tempChild = x
                    if(depth == 0):
                        print("child processed, eval:", nextLevel.evalValue, "   v:", v)
                    if(v == nextLevel.evalValue and depth == 0):
                        print("THis should BE ALRIGHT")
                        tempChild = x
                    if v >= beta:
                        return(x)
                    alpha = max(v, alpha)
                if(tempChild != None):
                    #print("DODODODDODO")
                    return(tempChild)
                else:
                    if(depth == 0):
                        print("this happens 2")
                    return(parentBoard)

            # if the color of the player at the maximizer is black
            else:
                children = parentBoard.generateAllBlackMoves()
                tempChild = None
                if(len(children) == 0):
                    print("this happens 3")
                    return(parentBoard)
                for x in children:

                    # checks for an early checkmate and prioritizes that move
                    if(depth == 0):
                        if(x.isWhiteInCheckmate()):
                            print("This is checkmate.")
                            return(x)
                    
                    
                    # calls minimizer node if maximum depth has not yet been reached
                    v = max(v, self.minNode(x, alpha, beta, 'w', depth + 1).evaluationFunction(), parentBoard.evaluationFunction())
                    if(v == x.evaluationFunction()):
                        tempChild = x
                    if v >= beta:
                        return(x)
                    alpha = max(v, alpha)
                if(tempChild != None):
                    return(tempChild)
                else:
                    print("this happens 4")
                    return(parentBoard)
            

    ###############################################################################
    #
    # Represents the function of an alpha beta minimizer node
    #
    ###############################################################################
    def minNode(self, parentBoard, alpha, beta, color, depth):
        if(depth == self.depth):
            return(parentBoard)
        else:
            v = 999999999       # used to represent positive infinity

            if(color == 'w'):
                children = parentBoard.generateAllWhiteMoves()
                tempChild = None
                if(len(children) == 0):
                    print("this happens 5")
                    return(parentBoard)
                for x in children:
                    if(depth == 0):
                        if(x.isBlackInCheckmate()):
                            print("This is checkmate")
                            return(x)


                    # calls maximizer node if maximum depth has not yet been reached
                    v = min(v, self.maxNode(x, alpha, beta, 'b', depth + 1).evaluationFunction())#, parentBoard.evaluationFunction())
                    if(v == x.evaluationFunction()):
                        tempChild = x
                    if v <= alpha:
                        return(x)
                    beta = min(v, beta)
                if(tempChild != None):
                    return(tempChild)
                else:
                    print("this happens 6")
                    return(parentBoard)
            else:
                children = parentBoard.generateAllBlackMoves()
                tempChild = None
                if(len(children) == 0):
                    print("this happens 7")
                    return(parentBoard)
                for x in children:

                    if(depth == 0):
                        if(x.isWhiteInCheckmate()):
                            print("This is checkmate")
                            return(x)

                    # calls maximizer node if maximum depth has not yet been reached
                    v = min(v, self.maxNode(x, alpha, beta, 'w', depth + 1).evaluationFunction())#, parentBoard.evaluationFunction())
                    if(v == x.evaluationFunction()):
                        tempChild = x
                    if v <= alpha:
                        return(x)
                    beta = min(v, beta)
                if(tempChild != None):
                    return(tempChild)
                else:
                    #print("this happens 8")
                    return(parentBoard)


    ###############################################################################
    #
    # kicks off the entire Alpha Beta Pruning process, which a maximizer at top
    #
    ###############################################################################
    def alphaBetaPruning(self):
        nextBoard = self.maxNode(self.initialBoard, -9999999, 9999999, self.initialColor, 0)
        print("Evaluation score of the selected move:", nextBoard.evalValue)
        return(nextBoard)

    