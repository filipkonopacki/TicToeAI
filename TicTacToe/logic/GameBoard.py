"""
# Class representing game board, performing actions like move, check current state, refresh
"""

# Game states #
DRAW = 0
CORSS_WIN = 1
NAUGHT_WIN = 2
NOT_FINISHED = 3

# Board cell state #
NAUGHT = 0
CROSS = 1
EMPTY = 2


class GameBoard:
    def __init__(self):
        self.current_state = NOT_FINISHED
        self.board = [EMPTY]*9

    def move(self, position, sign):
        if self.board[position] != EMPTY:
            raise ValueError('Invalid move')

        self.board[position] = sign

