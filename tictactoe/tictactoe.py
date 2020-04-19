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
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns 'X' if it is the turn of X
    and return 'O' if turn of O
    """
    count_X = 0  # Counts X on board
    count_O = 0  # Counts O on board

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_X += 1
            elif board[i][j] == O:
                count_O += 1

    if count_X > count_O:
        return O
    elif not terminal(board) and count_O == count_X:
        return X
    else:
        return None


def actions(board):
    # Set of actions available
    action_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.add((i, j))

    if len(action_set) == 0:  # If the board is full
        raise Exception("Board is Full")
    else:
        return action_set


def result(board, action):
    """
        Returns the resulting board after performing actions
        on the input board.
    """

    if terminal(board):
        raise ValueError("Game over.")
    elif action not in actions(board):  # Check for Invalid Action
        raise ValueError("Invalid action.")
    else:
        p = player(board)
        result_board = copy.deepcopy(board)
        (i, j) = action
        result_board[i][j] = p

    return result_board


def winner(board):
    """
        Returns 'X' or 'O' if there is a winner in the current state
        of the board and return 'NONE' if tie or no winner yet
    """
    if board[0][0] == board[0][1] == board[0][2] is not None:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    elif board[1][0] == board[1][1] == board[1][2] is not None:
        if board[1][0] == X:
            return X
        elif board[1][0] == O:
            return O
    elif board[2][0] == board[2][1] == board[2][2] is not None:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
    elif board[0][0] == board[1][0] == board[2][0] is not None:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    elif board[0][1] == board[1][1] == board[2][1] is not None:
        if board[0][1] == X:
            return X
        elif board[0][1] == O:
            return O
    elif board[0][2] == board[1][2] == board[2][2] is not None:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O
    elif board[0][0] == board[1][1] == board[2][2] is not None:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    elif board[0][2] == board[1][1] == board[2][0] is not None:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
        Returns TRUE if there is a winner and
        Game is over.
        Returns FALSE if game is not over yet
    """

    if winner(board) is not None:
        return True
    count_EMPTY = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count_EMPTY += 1
    if count_EMPTY == 0 and winner(board) is None:
        return True
    else:
        return False


def utility(board):
    """
        Returns '+1' if X wins.
        Returns '0' if there is a tie.
        Returns '-1' if O wins.
    """

    if terminal(board) is True:
        if winner(board) is X:
            return 1
        elif winner(board) is O:
            return -1
        else:
            return 0


def minimax(board):
    """
        Returns selected_action after applying the minimax
        algorithm.
    """
    p = player(board)
    if board == [[EMPTY] * 3] * 3:
        return 0, 0
    elif p == X:  # Player X tries to maximize the score
        selected_action = None
        MaxValueResult = MaxValue(board)
        """
        Applying a loop to find the action to which the maximum value
        corresponds.
        """
        for action in actions(board):
            if MinValue(result(board, action)) == MaxValueResult:
                selected_action = action

    elif p == O:  # Player O tries to minimize the score
        selected_action = None
        MinValueResult = MinValue(board)
        """
        Applying a loop to find the action to which the minimum value
        corresponds.
        """
        for action in actions(board):
            if MaxValue(result(board, action)) == MinValueResult:
                selected_action = action

    return selected_action


def MaxValue(board):
    """
    Returns the maximum value possible from available actions.
    """
    if terminal(board) is True:
        return utility(board)
    v = float("-inf")  # Lowest number possible i.e -infinity

    for action in actions(board):
        v = max(v, MinValue(result(board, action)))

    return v


def MinValue(board):
    """
    Returns the minimum value possible from available actions.
    """
    if terminal(board) is True:
        return utility(board)
    v = float("inf")  # Largest number possible i.e infinity

    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))

    return v
