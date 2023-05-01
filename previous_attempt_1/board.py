"""Noughts and crosses board.
logic for the board and win conditions.
"""

class Board:
    EMPTY = 0
    NOUGHT = 1
    CROSS = 2

    def __init__(self) -> None:
        self.width = 3
        self.height = 3

        self.reset()

    def next_turn(self) -> int:
        self.turn = Board.NOUGHT if self.turn == Board.CROSS else Board.CROSS
        return self.turn
    
    def reset(self) -> None:
        self.board = [[Board.EMPTY] * self.width] * self.height
        self.turn = Board.NOUGHT

    def make_move(self, x: int, y: int, player: int) -> None:
        if self.board[y][x] != Board.EMPTY:
            raise ValueError("Tile is already occupied")
        self.board[y][x] = player

    def get_tile(self, x: int, y: int) -> int:
        return self.board[y][x]

    def check_win(self) -> int:
        # check horizontal
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != Board.EMPTY:
                return row[0]
        # check vertical
        for column in range(self.width):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] and self.board[0][column] != Board.EMPTY:
                return self.board[0][column]
        # check diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != Board.EMPTY:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != Board.EMPTY:
            return self.board[0][2]
        return Board.EMPTY

    def check_draw(self) -> bool:
        for row in self.board:
            for tile in row:
                if tile == Board.EMPTY:
                    return False
        return True
