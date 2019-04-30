The program checkers_final.py must be run with python3 (preferably python3.6+)

The library copy must be installed, run the following command:
python3 -m pip install copy --user

evaluation function:
This program uses a simple evaluation function that assigns one point per checker and three points for a king. 

usage:
You, the user is playing white. The program displays your valid moves (note that if a jump is possible, that is the only valid move). You enter your move as x,y coordinates of the checker you want to move followed by a space followed by the x,y coordinates of where you want to move the checker. E.g: 0,5 1,4.
Pieces:
w = white checker
W = white king

b = black checker
B = back king

Rules:
1) If a jump is available - that is the only legal move
2) Kings and checkers move one tile on a right or left diagonal. Checkers can move only forwards, but kings can move forward and backward. If the move is a jump, the piece that is jumping lands on the tile that comes right after the one that had the opponent's piece.

__________________________________________________________________________________________________
The program checkers_final_improved.py must be run with python3 (preferably python3.6+)

The library copy must be installed, run the following command:
python3 -m pip install copy --user

improved evaluation function:
This program uses an improved evaluation function, which accounts for the fact that checkers closer to opponent's side are more valuable. It assignes one point per checker located on the player's side of the board, two points per checker located on the opponent's side of the board, and three points per king.

usage:
You, the user is playing white. The program displays your valid moves (note that if a jump is possible, that is the only valid move). You enter your move as x,y coordinates of the checker you want to move followed by a space followed by the x,y coordinates of where you want to move the checker. E.g: 0,5 1,4.

