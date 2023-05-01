from unittest import TestCase, main

from board import Board

class TestBoard(TestCase):
    def test_when_board_is_created_then_it_is_empty(self):
        board = Board()
        for row in board.board:
            for tile in row:
                self.assertEqual(tile, Board.EMPTY)

    def test_when_board_is_created_then_turn_is_cross(self):
        board = Board()
        self.assertEqual(board.turn, Board.CROSS)
    
    def test_when_board_is_created_with_nought_then_turn_is_naught(self):
        board = Board(Board.NOUGHT)
        self.assertEqual(board.turn, Board.NOUGHT)
    
    def test_when_board_is_empty_it_is_not_a_draw(self):
        board = Board()
        self.assertFalse(board.check_draw())

    def test_new_board_is_not_a_win(self):
        board = Board()
        self.assertEqual(board.check_win(), Board.EMPTY)

if __name__ == "__main__":
    main()
