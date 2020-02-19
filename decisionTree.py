# decisionTree.py

class decisionTree():

    def __init__(self, initialBoard, initialColor = 'w'):
        
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
                tempChild = None
                print("LENGTH OF CHILDREN:", len(children))
                for x in children:
                    tempChild = x
                    v = max(v, self.minNode(x, alpha, beta, 'b', depth + 1))
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        if(depth == 0):
                            print("have my child 1")
                            return(tempChild)
                        else:
                            return(v)
                    alpha = max(v, alpha)
                if(depth == 0):
                    print("have my child 2")
                    return(tempChild)
                else:
                    return(v)
            else:
                children = parentBoard.generateAllBlackMoves()
                tempChild = None
                for x in children:
                    tempChild = x
                    v = max(v, self.minNode(x, alpha, beta, 'w', depth + 1))
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        if(depth == 0):
                            print("have my child 3")
                            return(tempChild)
                        else:
                            return(v)
                    alpha = max(v, alpha)
                if(depth == 0):
                    print("have my child 4")
                    return(tempChild)
                else:
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