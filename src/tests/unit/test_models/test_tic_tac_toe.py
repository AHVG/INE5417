import unittest

from model.Board import Board
from model.TicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def test_initialization(self):
        self.assertIsInstance(self.tic_tac_toe, TicTacToe, "Should be an instance of UltimateTicTacToe")
        self.assertTrue(all(isinstance(x, Board) for row in self.tic_tac_toe.get_childs() for x in row), "All childs should be instances of Board")


if __name__ == '__main__':
    unittest.main()