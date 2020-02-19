# decisionTree.py

class decisionTree():

    def __init__(self, tree, initialBoard, initialColor = 'w'):
        self.tree = tree
        self.initialBoard = initialBoard
        self.initialColor = initialColor
        self.numberPrunes = 0
        self.numberTerminalNodesExamined = 0

    def maxNode(self, parentBoard, alpha, beta, color, depth):
        if(depth == 4):
            return(parentBoard.evalValue)
        else:
            v = -999999999      # used to represent negative infinity 
                                # python doesn't have a MIN INT
            if(color == 'w'):
                children = parentBoard.generateAllWhiteMoves()
                for x in children:
                    v = max(v, self.minNode(x, alpha, beta, 'b', depth + 1))
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    alpha = max(v, alpha)
                return(v)
            else:
                children = parentBoard.generateAllBlackMoves()
                for x in children:
                    v = max(v, self.minNode(x, alpha, beta, 'w', depth + 1))
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    alpha = max(v, alpha)
                return(v)
            

    def minNode(self, parentBoard, alpha, beta, color, depth):
        if(depth == 4):
            return(parentBoard.evalValue)
        else:
            v = 999999999       # used to represent positive infinity
                                # ptyhon doesn't have a MAX INT

            if(color == 'w'):
                children = parentBoard.generateAllWhiteMoves()
                for x in children:
                    v = min(v, self.maxNode(x, alpha, beta, 'b', depth + 1))
                    if v <= alpha:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    beta = min(v, beta)
                return(v)
            else:
                children = parentBoard.generateAllBlackMoves()
                for x in children:
                    v = min(v, self.maxNode(x, alpha, beta, 'w', depth + 1))
                    if v <= alpha:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    beta = min(v, beta)
                return(v)

    # starts the entire Alpha Beta Pruning process
    def alphaBetaPruning(self):
        return(self.maxNode(self.initialBoard, -9999999999, 999999999, self.initialColor, 0))