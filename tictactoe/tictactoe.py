"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    #if  the list is empty return x 
    if not board:
        return X

    #count how many times X appears in list
    value = 0
    for list in board:
        # check the number of times X appears in list
        #store the number in variable value
        value+= list.count(X)

    #check if value is divisible by 2
    if value%2 ==0:
        return X
    else:
        return O
            
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #iterate through the board list
    for sub_list in board:
        #iterate through sublist
        for x in sub_list:
            #look for cells on the board that do not already have an X or an O in them
            if x!="X" and  x!="O":
                 #return index of a tuple of (sub_list, index of None in sub_list)
                return (board.index(sub_list),sub_list.index(None))

   
        
    


    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError





