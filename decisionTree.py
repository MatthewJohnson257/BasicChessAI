###############################################################################
#
# This file handles the logic of the H-minimax alpha beta pruning tree
#
###############################################################################
class decisionTree():

    ###############################################################################
    #
    # Constructor takes the initial board, which strategy to use, and the depth 
    # to which to search
    #
    ###############################################################################
    def __init__(self, initialBoard, depth, initialColor = 'w'):
        
        self.initialBoard = initialBoard        # current board
        self.initialColor = initialColor        # AI color
        self.numberPrunes = 0                   
        self.numberTerminalNodesExamined = 0
        self.depth = depth

    ###############################################################################
    #
    # Represents the function of an alpha beta maximizer node
    #
    ###############################################################################
    def maxNode(self, parentBoard, alpha, beta, color, depth):
        #print(self.numberTerminalNodesExamined)
        if(depth == self.depth):
            return(parentBoard)
        else:
            v = -999999999      # used to represent negative infinity 
                                
            # if the color of the player at the maximizer is white
            if(color == 'w'):
                children = parentBoard.generateAllWhiteMoves()
                tempChild = None
                for x in children:

                    # checks for an early checkmate and prioritizes that move
                    if(depth == 0):
                        if(x.isBlackInCheckmate()):
                            print("This is checkmate.")
                            return(x)
                    tempChild = x
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1

                    # calls minimizer node if maximum depth has not yet been reached
                    v = max(v, self.minNode(x, alpha, beta, 'b', depth + 1).evalValue, parentBoard.evalValue)
                    if(v == x.evalValue):
                        return(tempChild)
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        if(depth == 0):
                            return(tempChild)
                        else:
                            return(v)
                    alpha = max(v, alpha)
                if(depth == 0):
                    return(tempChild)
                else:
                    return(v)

            # if the color of the player at the maximizer is black
            else:
                children = parentBoard.generateAllBlackMoves()
                tempChild = None
                for x in children:
                    tempChild = x
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1

                    # calls minimizer node if maximum depth has not yet been reached
                    v = max(v, self.minNode(x, alpha, beta, 'w', depth + 1), parentBoard.evalValue)
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        if(depth == 0):
                            return(tempChild)
                        else:
                            return(v)
                    alpha = max(v, alpha)
                if(depth == 0):
                    return(tempChild)
                else:
                    return(v)
            

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
                for x in children:
                    if(x.isWhiteInCheckmate()):
                            return(x)
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1

                    # calls maximizer node if maximum depth has not yet been reached
                    v = min(v, self.maxNode(x, alpha, beta, 'b', depth + 1).evalValue)
                    if v <= alpha:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    beta = min(v, beta)
                return(v)
            else:
                children = parentBoard.generateAllBlackMoves()
                for x in children:
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1

                    # calls maximizer node if maximum depth has not yet been reached
                    v = min(v, self.maxNode(x, alpha, beta, 'w', depth + 1).evalValue)
                    if v <= alpha:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    beta = min(v, beta)
                return(v)



    ###############################################################################
    #
    # kicks off the entire Alpha Beta Pruning process, which a maximizer at top
    #
    ###############################################################################
    def alphaBetaPruning(self):
        nextBoard = self.maxNode(self.initialBoard, -9999999, 9999999, self.initialColor, 0)
        print("Number of prunes:", self.numberPrunes)
        print("Number of terminal nodes examined:", self.numberTerminalNodesExamined)
        print("Evaluation score of the selected move:", nextBoard.evalValue)
        return(nextBoard)