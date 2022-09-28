"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


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
            if element == "X":
                count_x += 1
            elif element == "O":
                count_o += 1
            else:
                continue
    return "O" if count_x > count_o else "X"


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


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    The result function takes a “board” and an “action” as input, and should return a new board state, without modifying the original board.
    """
    
    # the original board should be left unmodified
    result = copy.deepcopy(board)
    # The returned board state should be the board that would result from taking the original input board,
    # and letting the player whose turn it is make their move at the cell indicated by the input action.   
    for x,y in actions(board):
        if int(action[0]) is x and int(action[1]) is y:
            result[action[0]][action[1]] = player(board)
            return result
        
    # If action is not a valid action for the board, your program should raise an exception.    
    raise Exception("Sorry, can't go here")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #inner funciton to check if we have a horizontal winner
    def checkHorizontalWinner(board):
        for player in board:
            if len(set(player)) == 1:
                return player[0]
        return -1
    
    #inner function to check if we have a vertical winner
    def checkVerticalWinner(board):
        for col in zip(*board):
            setcol = set()
            for i in range(len(board)):
                setcol.add(col[i])
            if len(setcol) == 1:
                return list(setcol)[0]
        return -1

    #inner function to check if we have a diagonal winner
    def checkDiagWinner(board):
        setdia = set([board[0][0], board[1][1], board[2][2]])
        setdia2 = set([board[0][2], board[1][1], board[2][0]])
        if len(setdia) == 1:
            return list(setdia)[0]
        elif len(setdia2) == 1:
            return list(setdia2)[0]
        else:
            return -1
        
    # variable will return -1 if we don't have a winner or X or 0 to represent the winner
    horizontal = checkHorizontalWinner(board)
    if horizontal != -1:
        # return the winner
        return horizontal

    # variable will return -1 if we don't have a winner or X or 0 to represent the winner
    vertical = checkVerticalWinner(board)
    if vertical != -1:
        # return the winner
        return vertical

    # variable will return -1 if we don't have a winner or X or 0 to represent the winner
    dia = checkDiagWinner(board)
    if dia != -1:
        # return the winner
        return dia
    
    # return None if we have no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    The terminal function should accept a “board” as input, and return a boolean value
    indicating whether the game is over.
    If the game is over, either because someone has won the game or because all cells have 
    been filled without anyone winning, the function should return “True”.
    Otherwise, the function should return “False” if the game is still in progress.

    """
    # we end the game if we have a winner
    if winner(board) == "O":
        return True
    elif winner(board) == "X":
        return True
    else:
        # if we don't have a winner we check the board if all the spots are not empty we return false
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == EMPTY:
                    return False
        # if we have no empty slots then the game is over        
        return True


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # check if game is over then we have no moves left
    if terminal(board):
        return score(board)

    # If player is 'X', we will maximize
    if player(board) == "X":
        # start with lowest so we can get the minumum score
        max_score = -INFINITY
        # initialize move so we can return the move with the move the ai will take
        moves = None

        # Find action with maximum score
        for action in actions(board):
            try:
                # get board with possible move
                playboard = result(board,action)
                # if score is higher than current score we swap results and the move
                if score(playboard) > max_score:
                    max_score = score(playboard)
                    moves = action
            except:
                continue
        return moves

    # If player is 'O', minimize
    elif player(board) == "O":
        # start with lowest so we can get the maximum score
        min_score = INFINITY
        # initialize move so we can return the move with the move the ai will take
        moves = None
        # Find action with minimum score
        for action in actions(board):
            try:
                # get board with possible move
                playboard = result(board,action)
                # if score is lower than current score we swap results and the move
                if score(playboard) < min_score:
                    min_score = score(playboard)
                    moves = action
            except:
                continue
        return moves

    # Else there is no valid player
    else:
        raise Exception("Invalid player")
