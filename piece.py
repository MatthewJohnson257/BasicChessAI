# piece.py
from abc import ABC, abstractmethod     # for abstract classes
import copy

class Piece(ABC):
    def __init__(self, i, j, color, id): # STUB!! get rid of default values later

        # instance variables:
        self.i = i
        self.j = j
        self.color = color
        self.id = id
        if self.id == 'k' or self.id == 'K':
            self.kink = True
        else:
            self.kink = False
        self.canMove = False


    # this method returns a list of coordinates that a piece would be able to move to
    # from its position if the rest of the board was completely empty
    def move(self):
        pass





    def isWhiteInCheck(self, grid, coordsList):
        tempGrid = [[None for x in range(0,8)] for y in range(0,8)]
        for x in range(8):
            for y in range(8):
                if(grid[x][y] != None):
                    tempGrid[x][y] = grid[x][y].id   #copying real board to temp board
                else:
                    tempGrid[x][y] = '_'

        boolList = [True for x in range(len(coordsList))]

        # find white king
        kingI = -1
        kingJ = -1
        if(self.id != 'K'):
            for g in range(8):
                for h in range(8):
                    if tempGrid[g][h] == 'K':
                        kingI = g
                        kingJ = h
                        break


        # test each coordinate pair in the parameter
        for x in range(len(coordsList)):
            newI = coordsList[x][0]
            newJ = coordsList[x][1]
            formerPiece = tempGrid[newI][newJ]
            tempGrid[newI][newJ] = tempGrid[self.i][self.j]
            tempGrid[self.i][self.j] = '_'

            if(self.id == 'K'):
                kingI = newI
                kingJ = newJ

            # checks by pawn to the left
            if(kingI > 0 and kingJ > 0 and (tempGrid[kingI - 1][kingJ - 1] == 'p' or tempGrid[kingI - 1][kingJ - 1] == 'k')):
                boolList[x] = False
                continue

            # checks by pawn to the right
            if(kingI > 0 and kingJ < 7 and (tempGrid[kingI - 1][kingJ + 1] == 'p' or tempGrid[kingI - 1][kingJ + 1] == 'k')):
                boolList[x] = False
                continue


            # all the surroundings for kings
            # above
            if(kingI > 0 and tempGrid[kingI - 1][kingJ] == 'k'):
                boolList[x] = False
                continue
            # left
            if(kingJ > 0 and tempGrid[kingI][kingJ - 1] == 'k'):
                boolList[x] = False
                continue
            # left below
            if(kingJ > 0 and kingI < 7 and tempGrid[kingI + 1][kingJ - 1] == 'k'):
                boolList[x] = False
                continue
            # below
            if(kingI < 7 and tempGrid[kingI + 1][kingJ] == 'k'):
                boolList[x] = False
                continue
            # below right
            if(kingI < 7 and kingJ < 7 and tempGrid[kingI + 1][kingJ + 1] == 'k'):
                boolList[x] = False
                continue
            # right
            if(kingJ < 7 and tempGrid[kingI][kingJ + 1] == 'k'):
                boolList[x] = False
                continue

            # check from horizontal left
            tempI = kingI
            tempJ = kingJ - 1
            while(tempJ >= 0):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'r'):
                        boolList[x] = False
                    else:
                        break
                tempJ = tempJ - 1

            # check from horizontal right
            tempI = kingI
            tempJ = kingJ + 1
            while(tempJ <= 7):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'r'):
                        boolList[x] = False
                    else:
                        break
                tempJ = tempJ + 1

            # check from vertical above
            tempI = kingI - 1
            tempJ = kingJ
            while(tempI >= 0):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'r'):
                        boolList[x] = False
                    else:
                        break
                tempI = tempI - 1

            # check from vertical below
            tempI = kingI + 1
            tempJ = kingJ
            while(tempI <= 7):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'r'):
                        boolList[x] = False
                    else:
                        break
                tempI = tempI + 1

            # check from diagonal upper left
            tempI = kingI - 1
            tempJ = kingJ - 1
            while(tempI >= 0 and tempJ >= 0):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'b'):
                        boolList[x] = False
                    else:
                        break
                tempI = tempI - 1
                tempJ = tempJ - 1

            # check from diagonal upper right
            tempI = kingI - 1
            tempJ = kingJ + 1
            while(tempI >= 0 and tempJ <= 7):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'b'):
                        boolList[x] = False
                    else:
                        break
                tempI = tempI - 1
                tempJ = tempJ + 1

            # check from diagonal bottom left
            tempI = kingI + 1
            tempJ = kingJ - 1
            while(tempI <= 7 and tempJ >= 0):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'b'):
                        boolList[x] = False
                    else:
                        break
                tempI = tempI + 1
                tempJ = tempJ - 1

            # check from diagonal bottom right
            tempI = kingI + 1
            tempJ = kingJ + 1
            while(tempI <= 7 and tempJ <= 7):
                if(tempGrid[tempI][tempJ] != '_'):
                    if(tempGrid[tempI][tempJ] == 'q' or tempGrid[tempI][tempJ] == 'b'):
                        boolList[x] = False
                    else:
                        break
                tempI = tempI + 1
                tempJ = tempJ + 1

            # check from knight

            if(kingI < 6 and kingJ < 7 and tempGrid[kingI + 2][kingJ + 1] == 'n'):
                boolList[x] = False
                continue
            if(kingI < 6 and kingJ > 0 and tempGrid[kingI + 2][kingJ - 1] == 'n'):
                boolList[x] = False
                continue
            if(kingI < 7 and kingJ < 6 and tempGrid[kingI + 1][kingJ + 2] == 'n'):
                boolList[x] = False
                continue
            if(kingI < 7 and kingJ > 1 and tempGrid[kingI + 1][kingJ - 2] == 'n'):
                boolList[x] = False
                continue
            if(kingI > 1 and kingJ < 7 and tempGrid[kingI - 2][kingJ + 1] == 'n'):
                boolList[x] = False
                continue
            if(kingI > 1 and kingJ > 0 and tempGrid[kingI - 2][kingJ - 1] == 'n'):
                boolList[x] = False
                continue
            if(kingI > 0 and kingJ > 1 and tempGrid[kingI - 1][kingJ - 2] == 'n'):
                boolList[x] = False
                continue
            if(kingI > 0 and kingJ < 1 and tempGrid[kingI - 1][kingJ + 2] == 'n'):
                boolList[x] = False
                continue

            # reset what was moved
            tempGrid[self.i][self.j] = self.id
            tempGrid[newI][newJ] = formerPiece

        return(boolList)


    def isBlackInCheck(self, grid, coordsList):
            tempGrid = [[None for x in range(0,8)] for y in range(0,8)]
            for x in range(8):
                for y in range(8):
                    if(grid[x][y] != None):
                        tempGrid[x][y] = grid[x][y].id   #copying real board to temp board
                    else:
                        tempGrid[x][y] = '_'

            boolList = [True for x in range(len(coordsList))]



            # find black king
            kingI = -1
            kingJ = -1
            if(self.id != 'k'):
                for g in range(8):
                    for h in range(8):
                        if tempGrid[g][h] == 'k':
                            kingI = g
                            kingJ = h
                            break


            # test each coordinate pair in the parameter
            for x in range(len(coordsList)):
                newI = coordsList[x][0]
                newJ = coordsList[x][1]
                formerPiece = tempGrid[newI][newJ]
                tempGrid[newI][newJ] = tempGrid[self.i][self.j]
                tempGrid[self.i][self.j] = '_'

                if(self.id == 'k'):
                    kingI = newI
                    kingJ = newJ

                # checks by pawn to the left
                if(kingI < 7 and kingJ > 0 and (tempGrid[kingI + 1][kingJ - 1] == 'P' or tempGrid[kingI + 1][kingJ - 1] == 'K')):
                    boolList[x] = False

                # checks by pawn to the right
                if(kingI < 7 and kingJ < 7 and (tempGrid[kingI + 1][kingJ + 1] == 'P' or tempGrid[kingI + 1][kingJ + 1] == 'K')):
                    boolList[x] = False


                # all the surroundings for kings
                # above
                if(kingI > 0 and tempGrid[kingI - 1][kingJ] == 'K'):
                    boolList[x] = False
                # left
                if(kingJ > 0 and tempGrid[kingI][kingJ - 1] == 'K'):
                    boolList[x] = False
                # left above
                if(kingJ > 0 and kingI > 0 and tempGrid[kingI - 1][kingJ - 1] == 'K'):
                    boolList[x] = False
                # below
                if(kingI < 7 and tempGrid[kingI + 1][kingJ] == 'K'):
                    boolList[x] = False
                # above right
                if(kingI > 0 and kingJ < 7 and tempGrid[kingI - 1][kingJ + 1] == 'K'):
                    boolList[x] = False
                # right
                if(kingJ < 7 and tempGrid[kingI][kingJ + 1] == 'K'):
                    boolList[x] = False

                # check from horizontal left
                tempI = kingI
                tempJ = kingJ - 1
                while(tempJ >= 0):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'R'):
                            boolList[x] = False
                        else:
                            break
                    tempJ = tempJ - 1

                # check from horizontal right
                tempI = kingI
                tempJ = kingJ + 1
                while(tempJ <= 7):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'R'):
                            boolList[x] = False
                        else:
                            break
                    tempJ = tempJ + 1

                # check from vertical above
                tempI = kingI - 1
                tempJ = kingJ
                while(tempI >= 0):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'R'):
                            boolList[x] = False
                        else:
                            break
                    tempI = tempI - 1

                # check from vertical below
                tempI = kingI + 1
                tempJ = kingJ
                while(tempI <= 7):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'R'):
                            boolList[x] = False
                        else:
                            break
                    tempI = tempI + 1

                # check from diagonal upper left
                tempI = kingI - 1
                tempJ = kingJ - 1
                while(tempI >= 0 and tempJ >= 0):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'B'):
                            boolList[x] = False
                        else:
                            break
                    tempI = tempI - 1
                    tempJ = tempJ - 1

                # check from diagonal upper right
                tempI = kingI - 1
                tempJ = kingJ + 1
                while(tempI >= 0 and tempJ <= 7):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'B'):
                            boolList[x] = False
                        else:
                            break
                    tempI = tempI - 1
                    tempJ = tempJ + 1

                # check from diagonal bottom left
                tempI = kingI + 1
                tempJ = kingJ - 1
                while(tempI <= 7 and tempJ >= 0):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'B'):
                            boolList[x] = False
                        else:
                            break
                    tempI = tempI + 1
                    tempJ = tempJ - 1

                # check from diagonal bottom right
                tempI = kingI + 1
                tempJ = kingJ + 1
                while(tempI <= 7 and tempJ <= 7):
                    if(tempGrid[tempI][tempJ] != '_'):
                        if(tempGrid[tempI][tempJ] == 'Q' or tempGrid[tempI][tempJ] == 'B'):
                            boolList[x] = False
                        else:
                            break
                    tempI = tempI + 1
                    tempJ = tempJ + 1

                # check from knight

                if(kingI < 6 and kingJ < 7 and tempGrid[kingI + 2][kingJ + 1] == 'N'):
                    boolList[x] = False
                if(kingI < 6 and kingJ > 0 and tempGrid[kingI + 2][kingJ - 1] == 'N'):
                    boolList[x] = False
                if(kingI < 7 and kingJ < 6 and tempGrid[kingI + 1][kingJ + 2] == 'N'):
                    boolList[x] = False
                if(kingI < 7 and kingJ > 1 and tempGrid[kingI + 1][kingJ - 2] == 'N'):
                    boolList[x] = False
                if(kingI > 1 and kingJ < 7 and tempGrid[kingI - 2][kingJ + 1] == 'N'):
                    boolList[x] = False
                if(kingI > 1 and kingJ > 0 and tempGrid[kingI - 2][kingJ - 1] == 'N'):
                    boolList[x] = False
                if(kingI > 0 and kingJ > 1 and tempGrid[kingI - 1][kingJ - 2] == 'N'):
                    boolList[x] = False
                if(kingI > 0 and kingJ < 1 and tempGrid[kingI - 1][kingJ + 2] == 'N'):
                    boolList[x] = False

                # reset what was moved
                tempGrid[self.i][self.j] = self.id
                tempGrid[newI][newJ] = formerPiece

            return(boolList)


class Pawn(Piece):

    def __init___(self, i, j, color, id):
        super(self, i, j, color, id)
        self.hasMoved = False

    # this method returns a list of coordinates that a Pawn would be able to move to
    # from its position if the rest of the board was completely empty
    def move(self, board):

        coordsList = []   # this is a list of (i,j) coordinates where a pawn can move.
                          # each move() method will need a list like this.  For a pawn, the list
                          # is only going to have one pair of coordinates, but different
                          # pieces will have a lot more coordinates

        # black pawn
        if(self.color == 'b'):
            if(self.i != 7): # this line checks to make sure a black pawn isn't at the very bottom of the board
                if(board.grid[self.i+1][self.j] == None): #pawn can move forward normally
                    coordsList.append([self.i + 1, self.j])
                if(self.j > 0 and board.grid[self.i+1][self.j-1] != None and board.grid[self.i+1][self.j-1].color != self.color and board.grid[self.i+1][self.j-1].kink != True): #pawn captures
                    coordsList.append([self.i + 1, self.j - 1])
                if(self.j < 7 and board.grid[self.i+1][self.j+1] != None and board.grid[self.i+1][self.j+1].color != self.color and board.grid[self.i+1][self.j+1].kink != True): #pawn captures
                    coordsList.append([self.i + 1, self.j + 1])
                if(self.i == 1 and board.grid[self.i+2][self.j] == None):
                    coordsList.append([self.i + 2, self.j])
                    if( (self.j > 0 and board.grid[self.i+2][self.j-1] == 'P') or (self.j < 7 and board.grid[self.i+2][self.j+1] == 'P' )):
                        self.hasMoved = True
                # if(self.i == 4 and self.j > 0 and board.grid[self.i+1][self.j-1] == None and board.grid[self.i][self.j-1].id == 'P' and board.grid[self.i][self.j-1].hasMoved == True ):
                #     coordsList.append([self.i+1, self.j-1])
                #     if(self.j < 6 and board.grid[self.i][self.j-2] == 'p'):
                #         board.grid[self.i][self.j-1].hasMoved == True
                #     else:
                #         board.grid[self.i][self.j-1].hasMoved == False
                # if(self.i == 4 and self.j < 7 and board.grid[self.i+1][self.j+1] == None and board.grid[self.i][self.j+1].id == 'P' and board.grid[self.i][self.j+1].hasMoved == True ):
                #     coordsList.append([self.i+1, self.j+1])
                #     board.grid[self.i][self.j-1].hasMoved == False



        # white pawn
        else:
            if(self.i != 0): # this line checks to make sure a white pawn isn't at the very top of the board
                if(board.grid[self.i-1][self.j] == None): #pawn can move forward normally
                    coordsList.append([self.i - 1, self.j])
                if(self.j > 0 and board.grid[self.i-1][self.j-1] != None and board.grid[self.i-1][self.j-1].color != self.color and board.grid[self.i-1][self.j-1].kink != True): #pawn captures
                    coordsList.append([self.i - 1, self.j - 1])
                if(self.j < 7 and board.grid[self.i-1][self.j+1] != None and board.grid[self.i-1][self.j+1].color != self.color and board.grid[self.i-1][self.j+1].kink != True): #pawn captures
                    coordsList.append([self.i - 1, self.j + 1])
                if(self.i == 1 and board.grid[self.i+2][self.j] == None):
                    coordsList.append([self.i + 2, self.j])
                    if( (self.j > 0 and board.grid[self.i+2][self.j-1] == 'P') or (self.j < 7 and board.grid[self.i+2][self.j+1] == 'P' )):
                        self.hasMoved = True
                # if(self.i == 4 and self.j > 0 and board.grid[self.i+1][self.j-1] == None and board.grid[self.i][self.j-1].id == 'P' and board.grid[self.i][self.j-1].hasMoved == True ):
                #     coordsList.append([self.i+1, self.j-1])
                #     if(self.j < 6 and board.grid[self.i][self.j-2] == 'p'):
                #         board.grid[self.i][self.j-1].hasMoved == True
                #     else:
                #         board.grid[self.i][self.j-1].hasMoved == False
                # if(self.i == 4 and self.j < 7 and board.grid[self.i+1][self.j+1] == None and board.grid[self.i][self.j+1].id == 'P' and board.grid[self.i][self.j+1].hasMoved == True ):
                #     coordsList.append([self.i+1, self.j+1])
                #     board.grid[self.i][self.j-1].hasMoved == False

        if(self.color == 'w'):
            inCheckList = self.isWhiteInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
            count = 0


        elif(self.color == 'b'):
            inCheckList = self.isBlackInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
            count = 0
        if(self.canMove == False):
            for x in range(len(coordsList)):
                if coordsList[x] is None:
                    count = count + 1
                    if(count == len(coordsList)):
                        self.canMove = False
                    else:
                        self.canMove = True




        return(coordsList)  # return the list of coordinates - a method in board.py will then check to see if the coords
                            # conflict with existing pieces or make the King in check and all that complicated stuff



        # print("Stub: Move Pawn")


class Rook(Piece):
    def move(self, board):
        coordsList = []

        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        while(x < 7): #move rook to all legal downward rows
            x = x + 1
            if(board.grid[x][n] == None):
                coordsList.append([x,n])
            elif(board.grid[x][n].color != self.color and board.grid[x][n].kink != True):
                coordsList.append([x,n])
                break
            else:
                break

        x = m + 0
        while(x > 0): # move rook to all legal upward rows
            x = x - 1
            if(board.grid[x][n] == None):
                coordsList.append([x,n])
            elif(board.grid[x][n].color != self.color and board.grid[x][n].kink != True):
                coordsList.append([x,n])
                break
            else:
                break

        x = n + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        while(x < 7): #move rook to all legal rightward columns
            x = x + 1
            if(board.grid[m][x] == None):
                coordsList.append([m,x])
            elif(board.grid[m][x].color != self.color and board.grid[m][x].kink != True):
                coordsList.append([m,x])
                break
            else:
                break

        x = n + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        while(x > 0): # move rook to all legal leftward columns
            x = x - 1
            if(board.grid[m][x] == None):
                coordsList.append([m,x])
            elif(board.grid[m][x].color != self.color and board.grid[m][x].kink != True):
                coordsList.append([m,x])
                break
            else:
                break
        # print("Stub: Move Rook")

        if(self.color == 'w'):
            inCheckList = self.isWhiteInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
            if len(coordsList) != 0:
                self.canMove = True


        elif(self.color == 'b'):
            inCheckList = self.isBlackInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
            if len(coordsList) != 0:
                self.canMove = True
        if(self.canMove == False):
            for x in range(len(coordsList)):
                if coordsList[x] is None:
                    count = count + 1
                    if(count == len(coordsList)):
                        self.canMove = False
                    else:
                        self.canMove = True

        return(coordsList)


class Knight(Piece):
    def move(self, board):
        coordsList = []
        x = self.i
        y = self.j
        if( x < 6 and y < 7 and ((board.grid[x+2][y+1] == None) or (board.grid[x+2][y+1].color != self.color and board.grid[x+2][y+1].kink != True))):
            coordsList.append([x+2,y+1])
        if( x < 6 and y > 0 and ((board.grid[x+2][y-1] == None) or (board.grid[x+2][y-1].color != self.color and board.grid[x+2][y-1].kink != True))):
            coordsList.append([x+2,y-1])
        if( x < 7 and y < 6 and ((board.grid[x+1][y+2] == None) or (board.grid[x+1][y+2].color != self.color and board.grid[x+1][y+2].kink != True))):
            coordsList.append([x+1,y+2])
        if( x < 7 and y > 1 and ((board.grid[x+1][y-2] == None) or (board.grid[x+1][y-2].color != self.color and board.grid[x+1][y-2].kink != True))):
            coordsList.append([x+1,y-2])
        if( x > 1 and y < 7 and ((board.grid[x-2][y+1] == None) or (board.grid[x-2][y+1].color != self.color and board.grid[x-2][y+1].kink != True))):
            coordsList.append([x-2,y+1])
        if( x > 1 and y > 0 and ((board.grid[x-2][y-1] == None) or (board.grid[x-2][y-1].color != self.color and board.grid[x-2][y-1].kink != True))):
            coordsList.append([x-2,y-1])
        if( x > 0 and y > 1 and ((board.grid[x-1][y-2] == None) or (board.grid[x-1][y-2].color != self.color and board.grid[x-1][y-2].kink != True))):
            coordsList.append([x-1,y-2])
        if( x > 0 and y < 6 and ((board.grid[x-1][y+2] == None) or (board.grid[x-1][y+2].color != self.color and board.grid[x-1][y+2].kink != True))):
            coordsList.append([x-1,y+2])


        if(self.color == 'w'):
            inCheckList = self.isWhiteInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
                if len(coordsList) != 0:
                    self.canMove = True
            coordsList = list(filter(lambda a: a != None, coordsList))
        elif(self.color == 'b'):
            inCheckList = self.isBlackInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        if(self.canMove == False):
            for x in range(len(coordsList)):
                if coordsList[x] is None:
                    count = count + 1
                    if(count == len(coordsList)):
                        self.canMove = False
                    else:
                        self.canMove = True

        # print("Stub: Move Knight")

        return (coordsList)

class Bishop(Piece):
    def move(self, board):
        coordsList = []
        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        z = n + 0
        while(x < 7 and z < 7): #move bishop to all right diagonals upwards
            x = x + 1
            z = z + 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        x = m + 0
        z = n + 0
        while(x > 0 and z > 0): # move bishop left diagonal downwards
            x = x - 1
            z = z - 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        x = m + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0   #switching pointers for rows and columns
        while(x < 7 and z > 0): #move bishop
            x = x + 1
            z = z - 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        x = m + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0
        while(x > 0 and z < 7): # move bishop
            x = x - 1
            z = z + 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        # print("Stub: Move Bishop")

        if(self.color == 'w'):
            inCheckList = self.isWhiteInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        elif(self.color == 'b'):
            inCheckList = self.isBlackInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        if(self.canMove == False):
            for x in range(len(coordsList)):
                if coordsList[x] is None:
                    count = count + 1
                    if(count == len(coordsList)):
                        self.canMove = False
                    else:
                        self.canMove = True

        return(coordsList)


class Queen(Piece): #for queen you can reuse rook and bishop moves
    def move(self, board):
        coordsList = []

        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        while(x < 7): #move rook to all legal downward rows
            x = x + 1
            if(board.grid[x][n] == None):
                coordsList.append([x,n])
            elif(board.grid[x][n].color != self.color and board.grid[x][n].kink != True):
                coordsList.append([x,n])
                break
            else:
                break

        x = m + 0
        while(x > 0): # move rook to all legal upward rows
            x = x - 1
            if(board.grid[x][n] == None):
                coordsList.append([x,n])
            elif(board.grid[x][n].color != self.color and board.grid[x][n].kink != True):
                coordsList.append([x,n])
                break
            else:
                break

        x = n + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        while(x < 7): #move rook to all legal rightward columns
            x = x + 1
            if(board.grid[m][x] == None):
                coordsList.append([m,x])
            elif(board.grid[m][x].color != self.color and board.grid[m][x].kink != True):
                coordsList.append([m,x])
                break
            else:
                break

        x = n + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        while(x > 0): # move rook to all legal leftward columns
            x = x - 1
            if(board.grid[m][x] == None):
                coordsList.append([m,x])
            elif(board.grid[m][x].color != self.color and board.grid[m][x].kink != True):
                coordsList.append([m,x])
                break
            else:
                break

        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        z = n + 0
        while(x < 7 and z < 7): #move bishop to all right diagonals upwards
            x = x + 1
            z = z + 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        x = m + 0
        z = n + 0
        while(x > 0 and z > 0): # move bishop left diagonal downwards
            x = x - 1
            z = z - 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        x = m + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0   #switching pointers for rows and columns
        while(x < 7 and z > 0): #move bishop
            x = x + 1
            z = z - 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break
        x = m + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0
        while(x > 0 and z < 7): # move bishop
            x = x - 1
            z = z + 1
            if(board.grid[x][z] == None):
                coordsList.append([x,z])
            elif(board.grid[x][z].color != self.color and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                break
            else:
                break

        if(self.color == 'w'):
            inCheckList = self.isWhiteInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        elif(self.color == 'b'):
            inCheckList = self.isBlackInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        if(self.canMove == False):
            for x in range(len(coordsList)):
                if coordsList[x] is None:
                    count = count + 1
                    if(count == len(coordsList)):
                        self.canMove = False
                    else:
                        self.canMove = True

        # print("Stub: Move Queen")

        return(coordsList)

class King(Piece):
    def move(self, board):
        coordsList = []
        x = self.i
        y = self.j
        if( (x < 7) and ((board.grid[x+1][y] ==  None) or (board.grid[x+1][y].color != self.color and board.grid[x+1][y].kink != True))):
            coordsList.append([x+1,y])
        if( (x > 0) and ((board.grid[x-1][y] ==  None) or (board.grid[x-1][y].color != self.color and board.grid[x-1][y].kink != True))):
            coordsList.append([x-1,y])
        if( (y > 0) and ((board.grid[x][y-1] ==  None) or (board.grid[x][y-1].color != self.color and board.grid[x][y-1].kink != True))):
            coordsList.append([x,y-1])
        if( (y < 7) and ((board.grid[x][y+1] ==  None) or (board.grid[x][y+1].color != self.color and board.grid[x][y+1].kink != True))):
            coordsList.append([x,y+1])
        if( (x < 7) and (y < 7) and ((board.grid[x+1][y+1] ==  None) or (board.grid[x+1][y+1].color != self.color and board.grid[x+1][y+1].kink != True))):
            coordsList.append([x+1,y+1])
        if( (x < 7) and (y > 0) and ((board.grid[x+1][y-1] ==  None) or (board.grid[x+1][y-1].color != self.color and board.grid[x+1][y-1].kink != True))):
            coordsList.append([x+1,y-1])
        if( (x > 0) and (y > 0) and ((board.grid[x-1][y-1] ==  None) or (board.grid[x-1][y-1].color != self.color and board.grid[x-1][y-1].kink != True))):
            coordsList.append([x-1,y-1])
        if( (x > 0) and (y < 7) and ((board.grid[x-1][y+1] ==  None) or (board.grid[x-1][y+1].color != self.color and board.grid[x-1][y+1].kink != True))):
            coordsList.append([x-1,y+1])
        # print("Stub: Move King")

        if(self.color == 'w'):
            inCheckList = self.isWhiteInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        if(self.color == 'b'):
            inCheckList = self.isBlackInCheck(board.grid, coordsList)
            for x in range(len(inCheckList)):
                if(inCheckList[x] == False):
                    coordsList[x] = None
            coordsList = list(filter(lambda a: a != None, coordsList))
        if(self.canMove == False):
            for x in range(len(coordsList)):
                if coordsList[x] is None:
                    count = count + 1
                    if(count == len(coordsList)):
                        self.canMove = False
                    else:
                        self.canMove = True

        return(coordsList)
