import unittest

from model.UltimateTicTacToe import UltimateTicTacToe
from model.TicTacToe import TicTacToe


class TestUltimateTicTacToe(unittest.TestCase):
    def setUp(self):
        self.ultimate_tic_tac_toe = UltimateTicTacToe()

    def test_initialization(self):
        self.assertIsInstance(self.ultimate_tic_tac_toe, UltimateTicTacToe, "Should be an instance of UltimateTicTacToe")
        self.assertTrue(all(isinstance(x, TicTacToe) for row in self.ultimate_tic_tac_toe.get_childs() for x in row), "All childs should be instances of TicTacToe")


if __name__ == '__main__':
    unittest.main()