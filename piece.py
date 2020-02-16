# piece.py
from abc import ABC, abstractmethod     # for abstract classes

class Piece(ABC):
    def __init__(self, i, j, color, id): # STUB!! get rid of default values later

        # these things are instance variables:
        self.i = i
        self.j = j
        self.color = color
        self.id = id
        if self.id == 'k' or self.id == 'K':
            self.kink = True
        else:
            self.kink = False
        # print("oh yeah we a piece man")  # debug print statement I guess lol


    # this method returns a list of coordinates that a piece would be able to move to
    # from its position if the rest of the board was completely empty
    def move(self):
        pass

class Pawn(Piece):

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
                if(board.grid[i+1][j] == None): #pawn can move forward normally
                    coordsList.append([self.i + 1, self.j])
                if(board.grid[i+1][j-1] != None and board.grid[i+1][j-1].color != self.color and j > 0 and board.grid[i+1][j-1].kink != True): #pawn captures
                    coordsList.append([self.i + 1, self.j - 1])
                if(board.grid[i+1][j+1] != None and board.grid[i+1][j+1].color != self.color and j < 8 and board.grid[i+1][j+1].kink != True): #pawn captures
                    coordsList.append([self.i + 1, self.j + 1])





        # white pawn
        else:
            if(self.i != 0): # this line checks to make sure a white pawn isn't at the very top of the board
                if(board.grid[i-1][j] == None): #pawn can move forward normally
                    coordsList.append([self.i - 1, self.j])
                if(board.grid[i-1][j-1] != None and board.grid[i-1][j-1].color != self.color and j > 0 and board.grid[i-1][j-1].kink != True): #pawn captures
                    coordsList.append([self.i + 1, self.j - 1])
                if(board.grid[i-1][j+1] != None and board.grid[i-1][j+1].color != self.color and j < 8 and board.grid[i-1][j+1].kink != True): #pawn captures
                    coordsList.append([self.i + 1, self.j + 1])


        return(coordsList)  # return the list of coordinates - a method in board.py will then check to see if the coords
                            # conflict with existing pieces or make the King in check and all that complicated stuff



        print("Stub: Move Pawn")


class Rook(Piece):
    def move(self, board):
        coordsList = []

        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        flag = False
        while(x < 7): #move rook to all legal  upward rows
            x = x + 1
            if( (board.grid[x][n] == None or board.grid[x][n].color != self.color) and board.grid[x][n].kink != True):
                coordsList.append([x,n])
            flag = True
            if not flag: # if(!flag)
                break


        x = m + 0
        flag = False
        while(x > 0): # move rook to all legal downward rows
            x = x - 1
            if( (board.grid[x][n] == None or board.grid[x][n].color != self.color) and board.grid[x][n].kink != True):
                coordsList.append([x,n])
            flag = True
            if not flag: # if(!flag)
                break

        x = n + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        flag = False
        while(x < 7): #move rook to all legal  rightward columns
            x = x + 1
            if( (board.grid[m][x] == None or board.grid[m][x].color != self.color) and board.grid[m][x].kink != True):
                coordsList.append([m,x])
            flag = True
            if not flag: # if(!flag)
                break

        x = m + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        while(x > 0): # move rook to all legal leftward columns
            x = x - 1
            if( (board.grid[m][x] == None or board.grid[m][x].color != self.color) and board.grid[m][x].kink != True):
                coordsList.append([m,x])
            flag = True
            if not flag: # if(!flag)
                break
        print("Stub: Move Rook")


class Knight(Piece):
    def move(self, board):
        coordsList = []
        x = self.i
        y = self.j
        if( x < 6 and y < 7  and (board.grid[x+2][y+1] == None or board.grid[x+2][y+1].color != self.color) and board.grid[x+2][y+1].kink != True):
            coordsList.append([x+2,y+1])
        if( x < 6 and y > 0 and (board.grid[x+2][y-1] == None or board.grid[x+2][y-1].color != self.color) and board.grid[x+2][y-1].kink != True):
            coordsList.append([x+2,y-1])
        if( x < 7 and y < 6 and (board.grid[x+1][y+2] == None or board.grid[x+1][y+2].color != self.color) and board.grid[x+1][y+2].kink != True):
            coordsList.append([x+1,y+2])
        if( x < 7 and y > 1 and (board.grid[x+1][y-2] == None or board.grid[x+1][y-2].color != self.color) and board.grid[x+1][y-2].kink != True):
            coordsList.append([x+1,y-2])
        if( x > 1 and y < 7  and (board.grid[x-2][y+1] == None or board.grid[x-2][y+1].color != self.color) and board.grid[x-2][y+1].kink != True):
            coordsList.append([x-2,y+1])
        if( x > 1 and y > 0  and (board.grid[x-2][y-1] == None or board.grid[x-2][y-1].color != self.color) and board.grid[x-2][y-1].kink != True):
            coordsList.append([x-2,y-1])
        if( x > 0 and y > 1 and (board.grid[x-1][y-2] == None or board.grid[x-1][y-2].color != self.color) and board.grid[x-1][y-2].kink != True):
            coordsList.append([x-1,y-2])
        if( x > 0 and y < 6 and (board.grid[x-1][y+2] == None or board.grid[x-1][y+2].color != self.color) and board.grid[x-1][y+2].kink != True):
            coordsList.append([x-1,y+2])





        print("Stub: Move Knight")

class Bishop(Piece):
    def move(self, board):
        coordsList = []
        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        z = n + 0
        flag = False
        while(x < 7 and z < 7): #move bishop to all right diagonals upwards
            x = x + 1
            z = z + 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
                flag = True
                if not flag: # if(!flag)
                    break
        x = m + 0
        z = n + 0
        flag = False
        while(x > 0 and n > 0): # move bishop  left diagonal downwards
            x = x - 1
            z = z - 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        x = m + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0   #switching pointers for rows and columns
        flag = False
        while(x < 7 and z > 0): #move bishop
            x = x + 1
            z = z - 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        x = m + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0
        flag = False
        while(x > 0 and z < 8): # move bishop
            x = x - 1
            z = z + 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        print("Stub: Move Bishop")


class Queen(Piece): #for queen you can reuse rook and bishop moves
    def move(self, board):
        coordsList = []
        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        flag = False
        while(x < 7): #move rook to all legal  upward rows
            x = x + 1
            if( (board.grid[x][n] == None or board.grid[x][n].color != self.color) and board.grid[x][n].kink != True):
                coordsList.append([x,n])
            flag = True
            if not flag: # if(!flag)
                break

        x = m + 0
        flag = False
        while(x > 0): # move rook to all legal downward rows
            x = x - 1
            if( (board.grid[x][n] == None or board.grid[x][n].color != self.color) and board.grid[x][n].kink != True):
                coordsList.append([x,n])
            flag = True
            if not flag: # if(!flag)
                break

        x = n + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        flag = False
        while(x < 7): #move rook to all legal  rightward columns
            x = x + 1
            if( (board.grid[m][x] == None or board.grid[m][x].color != self.color) and board.grid[m][x].kink != True):
                coordsList.append([m,x])
            flag = True
            if not flag: # if(!flag)
                break

        x = m + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        flag = False
        while(x > 0): # move rook to all legal leftward columns
            x = x - 1
            if( (board.grid[m][x] == None or board.grid[m][x].color != self.color) and board.grid[m][x].kink != True):
                coordsList.append([m,x])
            flag = True
            if not flag: # if(!flag)
                break
        m = self.i
        x = m + 0  #cause i was lazy to deep copy and dont wanna copy by reference
        n = self.j
        z = n + 0
        flag = False
        while(x < 7 and z < 7): #move bishop to all right diagonals upwards
            x = x + 1
            z = z + 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        x = m + 0
        z = n + 0
        flag = False
        while(x > 0 and n > 0): # move bishop  left diagonal downwards
            x = x - 1
            z = z - 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        x = m + 0   #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0   #switching pointers for rows and columns
        flag = False
        while(x < 7 and z > 0): #move bishop
            x = x + 1
            z = z - 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        x = m + 0 #cause i was lazy to deep copy and dont wanna copy by reference
        z = n + 0
        flag = False
        while(x > 0 and z < 8): # move bishop
            x = x - 1
            z = z + 1
            if( (board.grid[x][z] == None or board.grid[x][z].color != self.color) and board.grid[x][z].kink != True):
                coordsList.append([x,z])
            flag = True
            if not flag: # if(!flag)
                break
        print("Stub: Move Queen")


class King(Piece):
    def move(self, board):
        coordsList = []
        x = self.i
        y = self.j
        if( (x < 7) and (board.grid[x+1][y] ==  None or board.grid[x+1][y].color != self.color or board.grid[x+1][y].kink != True)  ):
            coordsList.append([x,y])
        if( (x > 0) and (board.grid[x-1][y] ==  None or board.grid[x-1][y].color != self.color or board.grid[x-1][y].kink != True)  ):
            coordsList.append([x,y])
        if( (y > 0) and (board.grid[x][y-1] ==  None or board.grid[x][y-1].color != self.color or board.grid[x][y-1].kink != True)  ):
            coordsList.append([x,y])
        if( (y > 0) and (board.grid[x][y+1] ==  None or board.grid[x][y+1].color != self.color or board.grid[x][y+1].kink != True)  ):
            coordsList.append([x,y])
        if( (x < 7) and (y < 7) and (board.grid[x+1][y+1] ==  None or board.grid[x+1][y+1].color != self.color or board.grid[x+1][y+1].kink != True)  ):
            coordsList.append([x,y])
        if( (x < 7) and (y > 0) and (board.grid[x+1][y-1] ==  None or board.grid[x+1][y-1].color != self.color or board.grid[x+1][y-1].kink != True)  ):
            coordsList.append([x,y])
        if( (x > 0) and (y > 0) and (board.grid[x-1][y-1] ==  None or board.grid[x-1][y-1].color != self.color or board.grid[x-1][y-1].kink != True)  ):
            coordsList.append([x,y])
        if( (x > 0) and (y < 7) and (board.grid[x-1][y+1] ==  None or board.grid[x-1][y+1].color != self.color or board.grid[x-1][y+1].kink != True)  ):
            coordsList.append([x,y])
        print("Stub: Move King")
