from unittest import TestCase, main

from board import Board

class TestBoard(TestCase):
    def test_when_board_is_created_then_it_is_empty(self):
        board = Board()
        for row in board.board:
            for tile in row:
                self.assertEqual(tile, Board.EMPTY)

if __name__ == "__main__":
    main()
