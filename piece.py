# piece.py
from abc import ABC, abstractmethod     # for abstract classes
  
class Piece(ABC):
    def __init__(self, i, j, color, id): # STUB!! get rid of default values later

        # these things are instance variables:
        self.i = i
        self.j = j
        self.color = color
        self.id = id
        # print("oh yeah we a piece man")  # debut print statement I guess lol


    # this method returns a list of coordinates that a piece would be able to move to
    # from its position if the rest of the board was completely empty
    def move(self):
        pass

class Pawn(Piece):

    # this method returns a list of coordinates that a Pawn would be able to move to
    # from its position if the rest of the board was completely empty
    def move(self):

        coordsList = []   # this is a list of (i,j) coordinates where a pawn can move.
                          # each move() method will need a list like this.  For a pawn, the list
                          # is only going to have one pair of coordinates, but different
                          # pieces will have a lot more coordinates

        # black pawn
        if(self.color == 'b'):
            if(self.i != 7): # this line checks to make sure a black pawn isn't at the very bottom of the board
                coordsList.append([self.i, self.j + 1]) # this is the syntax for adding one particular coordinate to the list
                                                        # 'self.i' and 'self.j' are instance variables for this pawn
                                                        # the [INT, INT] is just a pair of coordinates.  For some reason,
                                                        # you can just shove this into a list in python and it magically works

        # white pawn
        else:
            if(self.i != 0): # this line checks to make sure a white pawn isn't at the very top of the board
                coordsList.append([self.i, self.j - 1])

        return(coordsList)  # return the list of coordinates - a method in board.py will then check to see if the coords
                            # conflict with existing pieces or make the King in check and all that complicated stuff



        print("Stub: Move Pawn")

class Rook(Piece):
    def move(self):
        coordsList = []
        print("Stub: Move Rook")

class Knight(Piece):
    def move(self):
        coordsList = []
        print("Stub: Move Knight")

class Bishop(Piece):
    def move(self):
        coordsList = []
        print("Stub: Move Bishop")

class Queen(Piece):
    def move(self):
        coordsList = []
        print("Stub: Move Queen")

class King(Piece):
    def move(self):
        coordsList = []
        print("Stub: Move King")


