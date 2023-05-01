"""Noughts and crosses board.
logic for the board and win conditions.
"""
import random

class Board:
    EMPTY = 0
    NOUGHT = 1
    CROSS = 2

    WIDTH = 3
    HEIGHT = 3

    def __init__(self, starting_player=CROSS) -> None:
        self.reset(starting_player)

    def reset(self, starting_player) -> None:
        self.board = [[Board.EMPTY] * self.WIDTH] * self.HEIGHT
        self.turn = starting_player

    def next_turn(self) -> int:
        """Advance the turn and return the new player."""
        self.turn = Board.NOUGHT if self.turn == Board.CROSS else Board.CROSS
        return self.turn
    
    def make_move(self, x: int, y: int, player: int) -> None:
        if self.board[y][x] != Board.EMPTY:
            raise ValueError("Tile is already occupied")
        if self.turn != player:
            raise ValueError("It is not your turn")
        self.board[y][x] = player
        self.next_turn()

    def get_tile(self, x: int, y: int) -> int:
        return self.board[y][x]

    def check_win(self) -> int:
        """Return winning player, or EMPTY if no winner."""
        # check horizontal
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != Board.EMPTY:
                return row[0]
        # check vertical
        for column in range(self.WIDTH):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] and self.board[0][column] != Board.EMPTY:
                return self.board[0][column]
        # check diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != Board.EMPTY:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != Board.EMPTY:
            return self.board[0][2]
        return Board.EMPTY

    def check_draw(self) -> bool:
        """Return True if the board is full"""
        for row in self.board:
            for tile in row:
                if tile == Board.EMPTY:
                    return False
        return True