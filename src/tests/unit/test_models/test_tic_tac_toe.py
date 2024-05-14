import unittest

from model.Board import Board
from model.TicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def test_initialization(self):
        self.assertIsInstance(self.tic_tac_toe, TicTacToe, "Should be an instance of UltimateTicTacToe")
        self.assertTrue(all(isinstance(x, Board) for row in self.tic_tac_toe.get_childs() for x in row), "All childs should be instances of Board")

    def test_check_result_without_result(self):
        self.tic_tac_toe.check_result()
        self.assertEqual(self.tic_tac_toe.check_result(), None, "Result should be None")

    def test_check_result_winner_on_the_line(self):
        childs = self.tic_tac_toe.get_childs()
        line = childs[0]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")
        self.assertEqual(self.tic_tac_toe.check_result(), "O", "Result should be O")

    def test_check_result_winner_on_the_column(self):
        childs = self.tic_tac_toe.get_childs()
        childs[0][0].set_value("X")
        childs[1][0].set_value("X")
        childs[2][0].set_value("X")
        self.assertEqual(self.tic_tac_toe.check_result(), "X", "Result should be X")
        
    def test_check_result_winner_on_the_diagonal(self):
        childs = self.tic_tac_toe.get_childs()
        childs[0][0].set_value("X")
        childs[1][1].set_value("X")
        childs[2][2].set_value("X")
        self.assertEqual(self.tic_tac_toe.check_result(), "X", "Result should be X")
    
    def test_draw(self):
        # O X O
        # O X O
        # X O X
        childs = self.tic_tac_toe.get_childs()
        childs[0][0].set_value("O")
        childs[0][1].set_value("X")
        childs[0][2].set_value("O")

        childs[1][0].set_value("O")
        childs[1][1].set_value("X")
        childs[1][2].set_value("O")

        childs[2][0].set_value("X")
        childs[2][1].set_value("O")
        childs[2][2].set_value("X")
        self.assertEqual(self.tic_tac_toe.check_result(), "-", "Result should be -")


if __name__ == '__main__':
    unittest.main()