import unittest

from model.Board import Board, SIZE_OF_BOARD


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertIsNone(self.board.get_value(), "Initial value should be None")
        self.assertIsNone(self.board.get_childs(), "Initial childs should be None")

    def test_set_and_get_value(self):
        self.board.set_value("X")
        self.assertEqual(self.board.get_value(), "X", "Value should be 'X' after setting")
        self.board.set_value("O")
        self.assertEqual(self.board.get_value(), "O", "Value should be 'O' after setting")

    def test_reset(self):
        self.board.set_value("X")
        self.board.reset()
        self.assertIsNone(self.board.get_value(), "Value should be None after reset")

    def test_completely_filled(self):
        self.board.set_childs([[Board() for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)])
        
        for i in range(SIZE_OF_BOARD):
            for j in range(SIZE_OF_BOARD):
                self.board.get_childs()[i][j].set_value("X")
        
        self.assertTrue(self.board.is_completely_filled(), "Board should be completely filled")

    def test_check_result(self):
        self.board.set_childs([[Board() for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)])
        
        for i in range(SIZE_OF_BOARD):
            self.board.get_childs()[i][0].set_value("X")
        
        self.board.check_result()
        self.assertEqual(self.board.get_value(), "X", "X should win with a vertical line")

if __name__ == '__main__':
    unittest.main()
