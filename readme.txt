Usage:

Navigate inside the SimpleChessAI directory.  To run, type the command

    python3 chess.py [initialBoard] [ExplorationStrategy]

Where the initialBoard argument is an int between 1 and 6 that determines which
inital boards (A, B, or C) that will be solved by the program.  The numbers 1-3
represent the given boards from the lab2 assignment.  Board 4 is a regular 
chess board.  Board 5 is a complicated chess board where white has the 
advantage. Board 6 simply has one of each of the kings.

The ExplorationStrategy argument is an int between 1 and 2 that determines 
which of our two exploration strategies will be employed by the AI.
For example, the command

    python3 chess.py 3 1

will solve puzzle C using exploration strategy one.  The command

    python3 chess.py 1 2

will solved puzzle A using exploration strategy two.

----------------------------------IMPORTANT------------------------------------

Use of the GUI is fairly intuitive - you will be prompted visually by the
colors of the squares you click on.  HOWEVER, one element is not obvious.  In
order to get the AI to select a move, you will need to first click on the 
board. The AI will then go through the somewhat lengthy process of selecting a 
move.  Do not click the board during this period.  Afterwards, the player can
make their move, then afterwards will need to click the board once more to 
prompt the AI to select its next move.

