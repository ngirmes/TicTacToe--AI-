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
    In initial state, X gets first move
    """
    if board == initial_state():
        return X
    count_x = count_o = 0
    # Count how many X's and O's are on the board
    # If there are more X's, it is O's turn
    # If they are equal, it is X's turn
    # To be potentially optimized:
    for row in board:
        for element in row:
            if element == 'X':
                count_x += 1
            elif element == 'O':
                count_o += 1
            else:
                continue
    return O if count_x > count_o else X
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize an empty set to add the possible actions to
    moves = []
    # Loop through the board to find the possible actions
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    # Return moves unless it is empty, then return 0
    return moves if moves else 0
    #raise NotImplementedError


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


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
