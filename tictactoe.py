"""
Tic Tac Toe Player
"""
import math
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    good
    Returns starting state of the board.
    used in runner
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    probably good
    Returns player who has the next turn on a board. First player is X, second is O
    used in runner
    """
    xval = 0
    oval = 0
    for i in range(3):
        for t in board[i]:
            if t == "X":
                xval+=1
            elif t == "O":
                oval+=1
            else:
                pass
    if xval==oval:
        return "X"
    else:
        return "O"

def actions(board):
    """
    Good
    Returns set of all possible actions (i, j) available on the board.
    Not used in runner
    """
    
    actions = []
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == None:
                actions.append((row,cell))
    
    return actions  

def result(board, action):
    """
    no
    Returns the board that results from making move (i, j) on the board.
    used in runner
    """
    theboard = copy.deepcopy(board)
    
    if terminal(theboard):
        return theboard
    
    
    theboard[action[0]][action[1]] = player(board)
    
    
    return theboard

def winner(board):
    """
    probably good
    Returns the winner of the game, if there is one.
    used in runner
    """
    for i in range(3):
        #Horizontal
        if EMPTY not in board[i]:
            temp = ''
            temp = temp.join(board[i])
            if temp.count('X') == 3:
                return 'X'
            elif temp.count('O') == 3:
                return 'O'
    for i in range(3): # Vertical
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i]!= None:
                return board[0][i]
    #diagonal
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1]!= None:
            return board[1][1]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[1][1]!= None:
            return board[1][1]
    
    
    return None

def terminal(board):
    """
    Good
    Returns True if game is over, False otherwise.
    used in runner
    """
    for i in range(3):
        #Horizontal
        if EMPTY not in board[i]:
            temp = ''
            temp = temp.join(board[i])
            if temp.count('X') == 3 or temp.count('O') == 3:
                return True
    #vertical
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i]!= None:
                return True
    for random in range(2): #diagonal
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[1][1]!= None:
                return True
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[1][1]!= None:
                return True
    for i in range(3): #istherepossiblemoves
        if EMPTY in board[i]:
            return False
    #draw,failed other tests
    return True

def utility(board):
    """
    good
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    not used in runner
    """
    whowon = winner(board)
    
    if whowon == "X" :
        return 1
    elif whowon == "O":
        return -1
    if whowon == None:
        return 0


bestmovex = (3,3)
bestmoveo = (3,3)



def evalute(board):
    global bestmovex,bestmoveo
    state = copy.deepcopy(board)
    if terminal(state):
        return utility(state)
    lactions = actions(state)


    if player(state) =='X':
        maxEval = -100
        for x in lactions:
            move = evalute(result(state,x))
            if move>=maxEval:
                maxEval = move
                if lactions == actions(inputboard):
                    bestmovex = x
                    



        #print(temp3)
        
        
        return maxEval
            
    elif player(state) =='O':
        minEval = 100
        for o in lactions:
            move = evalute(result(state,o))
            if move<=minEval:
                minEval = move
                if lactions == actions(inputboard):
                    bestmoveo = o

        return minEval

inputboard = initial_state()
def minimax(board):
    """
    returns coordnite move that is best for the player who turns it is on initial input board. 
    """
    global bestmovex,bestmoveo,inputboard
    
    inputboard = copy.deepcopy(board)
    
    a = evalute(board)
    player1 = (player(board))
    
    if player1 =='X':
        return bestmovex
    else:
        return bestmoveo
         
    
        
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] fills horizontal row, left to right, then moves to next row down
    

# ape = [['X', 'X', 'O'],
#        [EMPTY, 'O', 'X'],  #(2,0)
#        [EMPTY, 'O', EMPTY]]


# trest = [['O', EMPTY, 'X'],
#          [EMPTY, 'X', EMPTY], #(2,0)
#          [EMPTY, EMPTY, EMPTY]]


# temp = [['X', EMPTY, 'X'], 
#         ['O', 'X', EMPTY], #(0,1)
#         ['O', 'X', 'O']]

# test1 = [['O', 'O', 'X'],
#          [EMPTY, 'X', 'O'], #(2,0)
#          [EMPTY, EMPTY, 'X']]

# test2 = [['O', EMPTY, EMPTY],
#          [EMPTY, 'X', EMPTY],  #(0,2);(1,2) is best
#          [EMPTY, 'O', 'X']]

# empty = initial_state()

    

# print(minimax(ape))





        
    
            