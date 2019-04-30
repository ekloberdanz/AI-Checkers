import copy

intructions = "\nInstructions: You are playing white\n(1) Enter xy coordinates of the checker that you want to move. \n(2) Then space separated by commas. \n(3) Then xy coordinates where you want to move the checker to. \nE.g.: 1,2 2,3\nNote that x and y coordinates start at 0."
print(intructions)

height = 8 # height of the board
width = 8 # width of the board
depth = 5 # depth of alpha beta algorithm that computer uses to choose a move
user = "user"
computer = "computer"

class Board:
    def __init__(self, height, width):
        # set the height and width of the play board
        self.height = height
        self.width = width

        # two lists containing the pieces of players
        self.blackList = []
        self.blackKings = []
        self.whiteList = []
        self.whiteKings = []
        
        # set up the initial positions of white and black pieces, black side will be shown on top of the board
        for i in range(width):
            self.blackList.append((i, (i+1)%2))
            self.whiteList.append((i, height - (i%2) -1 ))
            
        thirdRowBlackCheckers = [(1,2), (3,2), (5,2), (7,2)]
        for i in thirdRowBlackCheckers:
            self.blackList.append(i)
            
        thridRowWhiteCheckers = [(0,5), (2, 5), (4,5), (6,5)]
        for i in thridRowWhiteCheckers:
            self.whiteList.append(i)
        
    def populateBoard(self):
        l = []
        
        for i in range(width):
            l.append([' '] * height)
            
        for blackChecker in self.blackList:
            x, y = blackChecker # unpack tuple
            l[y][x] = "b"
            
        for whiteChecker in self.whiteList:
            x, y = whiteChecker # unpack tuple
            l[y][x] = "w"
            
        return l
        
        
        
    def printBoard(self, board):
        for line in board:
            print(line)


    def getUserMove(self, board):

        while True:
            move = input().split()
                            
            if not(len(move) == 2):
                print("Invalid move")
                continue
                
            Movefr = tuple(map(int, move[0].split(',')))
            Moveto = tuple(map(int, move[1].split(',')))
            '''
            if Movefr not in self.whiteList:
                print ("You don't have a checker in that place. Review the instructions below\n", intructions)
                continue

            elif tuple((Movefr,Moveto)) not in self.generateLegalMoves(board, self.whiteList, self.blackList):
                print("Invalid move")
                #print(self.generateLegalMoves(board, self.whiteList, self.blackList))
                continue
            '''
            break
        move = (Movefr, Moveto)
        return move

    def implementMove(self, board, move, player):
         Movefrom = move[0]
         xf, yf = Movefrom
         board[yf][xf] = ' '

         Moveto = move[1]
         x, y = Moveto

         if player == "user":
             # check if the checker made it to the end of the board and became a king
             if y == 0:
                 board[y][x] = "W"# king
                 self.whiteList.remove(Movefrom)
                 self.whiteKings.append((x,y))
            
             # check if the piece being moved is a king     
             elif (xf, yf) in self.whiteKings:
                 board[y][x] = "W"# king 
                 self.whiteKings.remove(Movefrom)
                 self.whiteKings.append(Moveto)
                 
             # in this situation, ordinary checker is being moved    
             else:
                 board[y][x] = "w"#checker
                 # update whiteList
                 self.whiteList.remove(Movefrom)
                 self.whiteList.append(Moveto)

             if self.isJump(move):
                jumpedChecker = None
                if x - xf == 2:
                    jumpedChecker = x-1, y+1
                if x - xf == -2:
                    jumpedChecker = xf-1, yf-1
                    
                #check if jumped checker was a king or checker and update the opponents pieces accordinly
                if jumpedChecker in self.blackKings:
                    self.blackKings.remove(jumpedChecker)
                else:
                    self.blackList.remove(jumpedChecker)
                x, y = jumpedChecker
                board[y][x] = ' '
             print("Board after user move")
  
             
         if player == "computer":
             # check if the checker made it to the end of the board and became a king
             if y == 7:
                 board[y][x] = "B"
                 self.blackList.remove(Movefrom)
                 self.blackKings.append((x,y)) # update lsit of kings
     
             # check if the piece being moved is a king     
             elif (xf, yf) in self.blackKings:
                 board[y][x] = "B"# king 
                 self.blackKings.remove(Movefrom)
                 self.blackKings.append(Moveto)
             # in this situation, ordinary checker is being moved  
             else:
                 board[y][x] = "b"
                 # update blackList
                 self.blackList.remove(Movefrom)
                 self.blackList.append(Moveto)
                 
             if self.isJump(move):
                jumpedChecker = None
                if x - xf == 2:
                    jumpedChecker = x-1, y-1
                if x - xf == -2:
                    jumpedChecker = x+1, y-1
                    
                if jumpedChecker in self.whiteKings:
                    self.whiteKings.remove(jumpedChecker)
                else:
                    self.whiteList.remove(jumpedChecker)
                x, y = jumpedChecker
                board[y][x] = ' '
               

             print("Board after computer move")

             
         self.printBoard(board)
         
    def implementSimulatedMoveBlack(self, board, move):
         Movefrom = move[0]
         xf, yf = Movefrom
         board[yf][xf] = ' '

         Moveto = move[1]
         x, y = Moveto
         if (xf, yf) in self.blackKings:
             board[y][x] = "B"
         else:
             board[y][x] = "b"
         
         if self.isJump(move):
             jumpedChecker = None
             if x - xf == 2:
                 jumpedChecker = x-1, y-1
             else:
                 jumpedChecker = x+1, y-1

             x, y = jumpedChecker
             board[y][x] = ' '


             
    def implementSimulatedMoveWhite(self, board, move):
         Movefrom = move[0]
         xf, yf = Movefrom
         board[yf][xf] = ' '

         Moveto = move[1]
         x, y = Moveto
         if (xf, yf) in self.whiteKings:
             board[y][x] = "W"
         else:
             board[y][x] = "w"
         
         if self.isJump(move):
                jumpedChecker = None
                if x - xf == 2:
                    jumpedChecker = x-1, y+1
                else:
                    jumpedChecker = xf-1, yf-1
           
                x, y = jumpedChecker
                board[y][x] = " "
                
  


    def generateLegalMoves(self, board, my_checkers, my_kings, oponents_checkers, opponents_kings):
        # if a Jump is possible, that is the only legal move
        
        jumpList = self.Jump(board, my_checkers, my_kings, oponents_checkers, opponents_kings)
        if len(jumpList) > 0:
            return jumpList
 
        else:
            return self.simpleMove(board, my_checkers, my_kings)
        
        
    def blackTiles(self, board):
        blackTiles = []
        for x, l in enumerate(board):
            for y, i in enumerate(l):
                if (x % 2) != (y % 2):
                    blackTiles.append((x, y))
        return blackTiles

    def emptyBlackTiles(self, board):
        blackTiles = self.blackTiles(board)
        emptyBlackTiles = []
        for tpl in blackTiles:
            if tpl not in self.whiteList and tpl not in self.blackList: # filter our tiles occupied by black and white checkers
                emptyBlackTiles.append(tpl)
                
        return emptyBlackTiles

    # returns a list of tuples, where each tuple has two tuples: (movefrom),(moveto)
    def simpleMove(self, board, my_checkers, my_kings): # for white player
        emptyBlackTiles = self.emptyBlackTiles(board)

        simpleMove = []
        # simple moves for checkers
        for moveFrom in my_checkers:
            x = moveFrom[0]
            y = moveFrom[1]

            if my_checkers == self.whiteList:
                MoveTo_option1 = x-1, y-1 # move distance = 1, always travelling forward, move on left diagonal
                MoveTo_option2 = x+1, y-1 # move on right diagonal
                
            elif my_checkers == self.blackList:
                MoveTo_option1 = x+1, y+1 # move distance = 1, always travelling forward, move on left diagonal
                MoveTo_option2 = x-1, y+1 # move on right diagonal
                
            if MoveTo_option1 in emptyBlackTiles: simpleMove.append((moveFrom,MoveTo_option1)) 
            if MoveTo_option2 in emptyBlackTiles: simpleMove.append((moveFrom,MoveTo_option2))
        
        # simple moves for kings
        if len(my_kings) > 0:
            for moveFrom in my_kings:
                x = moveFrom[0]
                y = moveFrom[1]
                if my_kings == self.whiteKings:
                    MoveTo_king_option1 = x-1, y-1 # move distance = 1, travelling forward, move on left diagonal
                    MoveTo_king_option2 = x+1, y-1 # move on right diagonal travelling forward
                    MoveTo_king_option3 = x+1, y+1 # move on right diagonal travelling backward
                    MoveTo_king_option4 = x-1, y+1 # move on left diagonal travelling backward
        
                elif my_kings == self.blackKings:
                    MoveTo_king_option1 = x+1, y+1 # move distance = 1, travelling forward, move on left diagonal
                    MoveTo_king_option2 = x-1, y+1 # move on right diagonal travellig forward
                    MoveTo_king_option3 = x+1, y-1 # move on right diagonal travelling backward
                    MoveTo_king_option4 = x-1, y-1 # move on left diagonal travelling backward    
            
                if MoveTo_king_option1 in emptyBlackTiles: simpleMove.append((moveFrom,MoveTo_king_option1)) 
                if MoveTo_king_option2 in emptyBlackTiles: simpleMove.append((moveFrom,MoveTo_king_option2))  
                if MoveTo_king_option3 in emptyBlackTiles: simpleMove.append((moveFrom,MoveTo_king_option3))  
                if MoveTo_king_option4 in emptyBlackTiles: simpleMove.append((moveFrom,MoveTo_king_option4))  
            
        return simpleMove

    def isJump(self, move):
        Movefrom = move[0]
        xf, yf = Movefrom
        Moveto = move[1]
        xt, yt = Moveto
  
        if ((xt - xf == 2) or (xf - xt == 2)):
            return True
        else:
            return False 
              
    
    def Jump(self, board, my_checkers, my_kings, oponents_checkers, opponents_kings):
        emptyBlackTiles = self.emptyBlackTiles(board)

        Jumps = []
        for moveFrom in my_checkers:
            x = moveFrom[0]
            y = moveFrom[1]

            if my_checkers == self.whiteList:
                OpponentChecker_option1 = x-1, y-1 # immediate tile possibly with opponent's checker
                TileAfter_option1 = x-2, y-2 # landing tile
                OpponentChecker_option2 = x+1, y-1 # immediate tile possibly with opponent's checker
                TileAfter_option2 = x+2, y-2 # landing tile
                
                if (OpponentChecker_option1 in oponents_checkers or OpponentChecker_option1 in opponents_kings) and TileAfter_option1 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option1))  
                if (OpponentChecker_option2 in oponents_checkers or OpponentChecker_option2 in opponents_kings) and TileAfter_option2 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option2))
             
               
            elif my_checkers == self.blackList:
                OpponentChecker_option1 = x+1, y+1 # immediate tile possibly with opponent's checker
                TileAfter_option1 = x+2, y+2 # landing tile
                OpponentChecker_option2 = x-1, y+1 # immediate tile possibly with opponent's checker
                TileAfter_option2 = x-2, y+2 # landing tile
		        
                if (OpponentChecker_option1 in oponents_checkers or OpponentChecker_option1 in opponents_kings) and TileAfter_option1 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option1))
                if (OpponentChecker_option2 in oponents_checkers or OpponentChecker_option2 in opponents_kings) and TileAfter_option2 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option2))
        
        if len(my_kings) > 0:
            for moveFrom in my_kings:
                x = moveFrom[0]
                y = moveFrom[1]
                if my_kings == self.whiteKings:
                    OpponentChecker_option1 = x-1, y-1 # move distance = 1, travelling forward, move on left diagonal
                    TileAfter_option1 = x-2, y-2 # landing tile
                    OpponentChecker_option2 = x+1, y-1 # move on right diagonal travelling forward
                    TileAfter_option2 = x+2, y-2 # landing tile
                    OpponentChecker_option3 = x+1, y+1 # move on right diagonal travelling backward
                    TileAfter_option3 = x+2, y+2 # landing tile
                    OpponentChecker_option4 = x-1, y+1 # move on left diagonal travelling backward
                    TileAfter_option4 = x-2, y+2 # landing tile
                    
                elif my_kings == self.blackKings:
                    OpponentChecker_option1 = x+1, y+1 # move distance = 1, travelling forward, move on left diagonal
                    TileAfter_option1 = x+2, y+2
                    OpponentChecker_option2 = x-1, y+1 # move on right diagonal travellig forwardTileAfter_option1
                    TileAfter_option2 = x-2, y+2
                    OpponentChecker_option3 = x+1, y-1 # move on right diagonal travelling backward
                    TileAfter_option3 = x+2, y-2 
                    OpponentChecker_option4 = x-1, y-1 # move on left diagonal travelling backward    
                    TileAfter_option4 = x-2, y-2
                
                if (OpponentChecker_option1 in oponents_checkers or OpponentChecker_option1 in opponents_kings) and TileAfter_option1 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option1))  
                if (OpponentChecker_option2 in oponents_checkers or OpponentChecker_option2 in opponents_kings) and TileAfter_option2 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option2))
                if (OpponentChecker_option3 in oponents_checkers or OpponentChecker_option3 in opponents_kings) and TileAfter_option3 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option1))  
                if (OpponentChecker_option4 in oponents_checkers or OpponentChecker_option4 in opponents_kings) and TileAfter_option4 in emptyBlackTiles:
                    Jumps.append((moveFrom,TileAfter_option2))

        return Jumps   


    def evaluationFunctionImproved(self, board, my_checkers, my_kings, oponents_checkers, opponents_kings):
        if (my_checkers == self.whiteList and my_kings == self.whiteKings):
            score = 0
            
            for whiteChecker in self.whiteList:
                x, y = whiteChecker # unpack tuple
                # check if whiteChecker is on opponent's side of the board
                if y <= 3:
                # if yes, then it's worth 2 points else just 1 point
                    score = score + 2
                else:
                    score = score +  1
            for whiteKing in self.whiteKings:
                score = score + 3 # kings is worth 3 points
  
            return score
            
        elif (my_checkers == self.blackList and my_kings == self.blackKings):
            score = 0
            for blackChecker in self.blackList:
                x, y = blackChecker # unpack tuple
                # check if blackChecker is on opponent's side of the board
                if y >=4 :
                # if yes, then it's worth 2 points else just 1 point
                    score = score + 2
                else:
                    score = score + 1
                for blackKing in self.blackKings:
                    score = score + 3
                    
            return score
            
    
    def winnerIsUser(self, board, my_checkers, oponents_checkers):
        blackList = self.blackList
        whiteList = self.whiteList
        
        blackKings = self.blackKings
        whiteKings = self.whiteKings

        if len(whiteList) == 0 and len(whiteKings) == 0 or self.generateLegalMoves(board, my_checkers, my_kings, oponents_checkers, opponents_kings) == 0:
            return False
        elif len(blackList) == 0 and len(blackKings) == 0 or self.generateLegalMoves(board, oponents_checkers, opponents_kings, my_checkers, my_kings) == 0:
            return True
        
    def terminalState(self, board):
        blackList = self.blackList
        whiteList = self.whiteList
        
        blackKings = self.blackKings
        whiteKings = self.whiteKings

        if len(whiteList) == 0 and len(whiteKings) or self.generateLegalMoves(board, whiteList, whiteKings, blackList, blackKings) == 0:
            return True
        elif len(blackList) == 0 and len(blackKings) or self.generateLegalMoves(board, blackList, blackKings, whiteList, whiteKings) == 0:
            return True
        else:
            return False

    def minMax(self, board):
        bestBoard = None
        currentDepth = depth + 1
        while not bestBoard and currentDepth > 0:
            currentDepth -= 1
            (bestBoard, bestVal, move) = self.maxMove(board, currentDepth)
            
        return (bestBoard, bestVal, move)
        
      


    def maxMove(self, maxboard, currentDepth):
        return self.alphaBeta(maxboard, currentDepth-1, float('-inf'))

    
    def minMove(self, minboard, currentDepth):
        return self.alphaBeta(minboard, currentDepth-1, (float('inf')))

    def alphaBeta(self, board, currentDepth, bestMove):
    
        if self.terminalState(board) or currentDepth <= 0:
            return (board, self.evaluationFunctionImproved(board, self.whiteList, self.whiteKings, self.blackList, self.blackKings))

        best_move = bestMove
        best_board = None
        use_this_move = ((3,7), (2,6))
        
    
         # max 
        if bestMove == float('-inf'):
            moves = self.generateLegalMoves(board, self.blackList, self.blackKings, self.whiteList, self.whiteKings)
 
            for move in moves:
                maxboard = copy.deepcopy(board)              
                self.implementSimulatedMoveBlack(maxboard, move)
                alpha = self.minMove(maxboard, currentDepth-1)[1]
                if alpha > bestMove:
                    best_move = alpha
                    best_board = maxboard
                    use_this_move = move
 
        # min
        elif bestMove == float('inf'):
            moves = self.generateLegalMoves(board, self.whiteList, self.whiteKings, self.blackList, self.blackKings)
            for move in moves:
  
                minboard = copy.deepcopy(board)
                self.implementSimulatedMoveWhite(minboard, move)
                beta = self.maxMove(minboard, currentDepth-1)[1]

                if beta < bestMove:
                    best_move = beta
                    best_board = minboard
       
        return(best_board, best_move, use_this_move)

def main():
    b = Board(height, width)
    boardstate = b.populateBoard()
    print("\nCheckers Game\n")
    b.printBoard(boardstate)
    
    print("User legal moves:")
    print(b.generateLegalMoves(boardstate, b.whiteList, b.whiteKings, b.blackList, b.blackKings))

                    
    while b.terminalState(boardstate) == False:
        # User's turn
        user = "user" # the player is user
        userMove = b.getUserMove(boardstate) # read user input
        b.implementMove(boardstate, userMove, user) # update board with user's move
        # tell user their score
        print("Your score is:")
        print(b.evaluationFunctionImproved(boardstate, b.whiteList, b.whiteKings, b.blackList, b.blackKings))
        
        # Computer's turn
        print("Computer legal moves:")
        computerLegalMoves = b.generateLegalMoves(boardstate, b.blackList, b.blackKings, b.whiteList, b.whiteKings)
        print(computerLegalMoves) # print the computer's legal moves
        computer = "computer" # the player is computer
        computerMove = b.minMax(boardstate) # call minimax algorithm to get computer's move
        computerScore = computerMove[1] # computer's score      
        computerPlayed = computerMove[2] # this is the move that computer chose to play
        print("The move that computer will play is:", computerPlayed)
        print('The computer score after this move is:', computerScore)
        b.implementMove(boardstate, computerPlayed, computer) # upadate checkers lists and board
        
        # print legal moves for user
        print("User legal moves:")
        print(b.generateLegalMoves(boardstate, b.whiteList, b.whiteKings, b.blackList, b.blackKings))

        # Check for termination
        if b.winnerIsUser == False:
            print("Game over. Black won")
            break
        elif b.winnerIsUser == True:
            print("Congratualations! White won")



if __name__ == '__main__':
    main()
    print('done')
