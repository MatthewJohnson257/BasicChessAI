# decisionTree.py

class decisionTree():

    def __init__(self, initialBoard, initialColor = 'w'):
        
        self.initialBoard = initialBoard
        self.initialColor = initialColor
        self.numberPrunes = 0
        self.numberTerminalNodesExamined = 0

    def maxNode(self, parentBoard, alpha, beta, color, depth):
        #print("Enter max node")
        #print(self.numberTerminalNodesExamined)
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
                    if(depth == 0):
                        if(x.isBlackInCheckmate()):
                            print("WE HAVE RETURNED AN EARLY CHECKMATE")
                            x.printBoard()
                            return(x)
                    tempChild = x
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1
                    v = max(v, self.minNode(x, alpha, beta, 'b', depth + 1), parentBoard.evalValue)
                    if v >= beta:
                        self.numberPrunes = self.numberPrunes + 1
                        if(depth == 0):
                            print("have my child 1")
                            return(tempChild)
                        else:
                            return(v)
                    alpha = max(v, alpha)
                if(depth == 0):
                    print("Number of prunes:", self.numberPrunes)
                    print("Number of nodes examined:", self.numberTerminalNodesExamined)
                    print("have my child 2")
                    return(tempChild)
                else:
                    return(v)
            else:
                children = parentBoard.generateAllBlackMoves()
                tempChild = None
                for x in children:
                    tempChild = x
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1
                    v = max(v, self.minNode(x, alpha, beta, 'w', depth + 1), parentBoard.evalValue)
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
        #print("Enter min node")
        if(depth == 4):
            return(parentBoard.evalValue)
        else:
            v = 999999999       # used to represent positive infinity
                                # python doesn't have a MAX INT

            if(color == 'w'):
                children = parentBoard.generateAllWhiteMoves()
                for x in children:
                    if(x.isWhiteInCheckmate()):
                            #print("WE HAVE RETURNED AN EARLY CHECKMATE")
                            #x.printBoard()
                            return(x)
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1
                    v = min(v, self.maxNode(x, alpha, beta, 'b', depth + 1))
                    if v <= alpha:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    beta = min(v, beta)
                return(v)
            else:
                children = parentBoard.generateAllBlackMoves()
                for x in children:
                    self.numberTerminalNodesExamined = self.numberTerminalNodesExamined + 1
                    v = min(v, self.maxNode(x, alpha, beta, 'w', depth + 1))
                    if v <= alpha:
                        self.numberPrunes = self.numberPrunes + 1
                        return(v)
                    beta = min(v, beta)
                return(v)

    # starts the entire Alpha Beta Pruning process
    def alphaBetaPruning(self):
        return(self.maxNode(self.initialBoard, -9999999, 9999999, self.initialColor, 0))