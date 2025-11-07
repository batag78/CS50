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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board is None:
        return X
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count <= o_count:
        return X
    else:
        return O
 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))               
    return actions
    raise NotImplementedError


def result(board, action):
    if actions(board) is None:
        raise Exception("Invalid action")
    if action not in actions(board):
        raise Exception("Invalid action")
    board_copy = [row[:] for row in board]
    board_copy[action[0]][action[1]] = player(board)
    return board_copy
    
    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]        
    return None
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True 
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:    
        return -1             
    else:
        return 0
    raise NotImplementedError


def minimax(board, level = 0):
    if board == initial_state():
        return (1, 1)
 
    if terminal(board):
        return utility(board)
    level += 1
    current_player = player(board)
    if current_player == X:
        max_eval = -math.inf
        best_action = None
        for action in actions(board):
            eval = minimax(result(board, action),level)
            if eval > max_eval:
                max_eval = eval
                best_action = action
        if level == 1:
            return best_action
        return max_eval
    else:
        min_eval = math.inf
        best_action = None
        for action in actions(board):
            eval = minimax(result(board, action),level)
            if eval < min_eval:
                min_eval = eval
                best_action = action
        if level == 1:
            return best_action
        return min_eval
    return best_action
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
