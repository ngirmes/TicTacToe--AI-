"""
Tic Tac Toe Player
"""

from dbm import dumb
import math
from queue import Empty
from ssl import VerifyFlags

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

    The player function should take a “board” state as input, 
    and return which player’s turn it is (either X or O)
    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

    """
    if board is initial_state():
        return "X"
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
    return 'O' if count_x > count_o else "X"
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    The actions function should return a set of all of the possible actions 
    that can be taken on a given board.
    Each action should be represented as a tuple (i, j) where ‘i’ corresponds 
    to the row of the move (0,1 or 2) and ‘j’ corresponds to which cell in 
    the row corresponds to the move (also 0, 1 or 2).
    Possible moves are any cells on the board that do not already have an ‘X’ or an ‘O’  in them.
    Any return value is acceptable if a terminal board is provided as input.

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

    The result function takes a “board” and an “action” as input, and should return a new board state, without modifying the original board.

    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, 
    and letting the player whose turn it is make their move at the cell indicated by the input action.
    Importantly, the original board should be left unmodified: since Minimax will ultimately require considering
    many different board states during its computation. This means that simply updating a cell in “board” 
    itself is not a correct implementation of the “result” function. You’ll likely want to make a deep copy
    of the board first before making any changes.
    """
    result = board.copy()
    avalibleactions = actions(board)   
    print(action)
   
    for tuple in avalibleactions:
        if action[0] is tuple[0] and action[1] is tuple[1]:
            result[action[0]][action[1]] = "X"
            return result
        
        
    raise Exception("Sorry, can't go here")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def checkHorizontalWinner(board):
        for player in board:
            if len(set(player)) == 1:
                return player[0]
        return -1

    def checkVerticalWinner(board):
        for col in zip(*board):
            setcol = set()
            for i in range(len(board)):
                setcol.add(board[i][col])
            if len(setcol) == 1:
                return player[0]
        return -1
    
    def checkDiagWinner(board):
        setdia = set([board[0][0], board[1][1], board[2][2]])
        setdia2 = set([board[0][2], board[1][1], board[2][0]])
        if len(setdia) == 1:
            return setdia[0]
        elif len(setdia2) == 1:
            return setdia2[0]
        else:
            return -1

    horizontal = checkHorizontalWinner(board)
    if horizontal is not -1:
        return horizontal
    
    vertical = checkVerticalWinner(board)
    if vertical is not -1:
        return vertical

    dia = checkDiagWinner(board)
    if dia is not -1:
        return dia
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    The terminal function should accept a “board” as input, and return a boolean value 
    indicating whether the game is over.
    If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return “True”.
    Otherwise, the function should return “False” if the game is still in progress.

    """
    if winner(board) is "O":
        return True
    elif winner(board) is "1":
        return True
    else:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] is EMPTY:
                    return False
        return True    


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is 'X':
        return 1
    elif winner(board) is 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
