# piece.py
from abc import ABC, abstractmethod     # for abstract classes
  
class Piece(ABC):
    def __init__(self, x = 0 , y = 0, color = 'b'): # STUB!! get rid of default values later
        self.x = x
        self.y = y
        self.color = color
        print("oh yeah we a piece man")

    def move(self):
        pass

class Pawn(Piece):
    def move(self):
        coordsList = []

        # black pawn
        if(self.color == 'b'):
            if(self.y != 7):
                coordsList.append([self.x, self.y + 1])

        # white pawn
        else:
            if(self.y != 0):
                coordsList.append([self.x, self.y - 1])

        return(coordsList)
        print("Stub: Move Pawn")

class Rook(Piece):
    def move(self):
        print("Stub: Move Rook")

class Knight(Piece):
    def move(self):
        print("Stub: Move Knight")

class Bishop(Piece):
    def move(self):
        print("Stub: Move Bishop")

class Queen(Piece):
    def move(self):
        print("Stub: Move Queen")

class King(Piece):
    # def __init__(self):

    def move(self):
        print("Stub: Move King")



# thing = Piece()
# thing.move()
# thing2 = King()
# thing2.move()