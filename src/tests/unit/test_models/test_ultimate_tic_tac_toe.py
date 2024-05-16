import unittest

from model.UltimateTicTacToe import UltimateTicTacToe
from model.TicTacToe import TicTacToe


class TestUltimateTicTacToe(unittest.TestCase):
    def setUp(self):
        self.ultimate_tic_tac_toe = UltimateTicTacToe()

    def test_initialization(self):
        self.assertIsInstance(self.ultimate_tic_tac_toe, UltimateTicTacToe, "Should be an instance of UltimateTicTacToe")
        self.assertTrue(all(isinstance(x, TicTacToe) for row in self.ultimate_tic_tac_toe.get_childs() for x in row), "All childs should be instances of TicTacToe")

    def test_check_result_winner_on_the_line(self):
        childs = self.ultimate_tic_tac_toe.get_childs()
        
        tic_tac_toe = childs[1][0]
        line = tic_tac_toe.get_childs()[0]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")
        
        tic_tac_toe = childs[1][1]
        line = tic_tac_toe.get_childs()[2]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")

        tic_tac_toe = childs[1][2]
        line = tic_tac_toe.get_childs()[1]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")
        
        self.assertEqual(self.ultimate_tic_tac_toe.check_result(), "O", "Result should be O")

    def test_check_result_winner_on_the_column(self):
        childs = self.ultimate_tic_tac_toe.get_childs()
        
        tic_tac_toe = childs[0][2]
        line = tic_tac_toe.get_childs()[0]
        line[0].set_value("X")
        line[1].set_value("X")
        line[2].set_value("X")
        
        tic_tac_toe = childs[1][2]
        line = tic_tac_toe.get_childs()[2]
        line[0].set_value("X")
        line[1].set_value("X")
        line[2].set_value("X")

        tic_tac_toe = childs[2][2]
        line = tic_tac_toe.get_childs()[1]
        line[0].set_value("X")
        line[1].set_value("X")
        line[2].set_value("X")
        
        self.assertEqual(self.ultimate_tic_tac_toe.check_result(), "X", "Result should be X")

    def test_check_result_winner_on_the_diagonal(self):
        childs = self.ultimate_tic_tac_toe.get_childs()
        
        tic_tac_toe = childs[0][2]
        line = tic_tac_toe.get_childs()[0]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")
        
        tic_tac_toe = childs[1][1]
        line = tic_tac_toe.get_childs()[2]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")

        tic_tac_toe = childs[2][0]
        line = tic_tac_toe.get_childs()[1]
        line[0].set_value("O")
        line[1].set_value("O")
        line[2].set_value("O")
        
        self.assertEqual(self.ultimate_tic_tac_toe.check_result(), "O", "Result should be O")

    def test_draw(self):
        # O X O
        # O X O
        # X O X

        for line in self.ultimate_tic_tac_toe.get_childs():
            for tic_tac_toe in line:
                childs = tic_tac_toe.get_childs()
                childs[0][0].set_value("O")
                childs[0][1].set_value("X")
                childs[0][2].set_value("O")

                childs[1][0].set_value("O")
                childs[1][1].set_value("X")
                childs[1][2].set_value("O")

                childs[2][0].set_value("X")
                childs[2][1].set_value("O")
                childs[2][2].set_value("X")

        self.assertEqual(self.ultimate_tic_tac_toe.check_result(), "-", "Result should be -")


if __name__ == '__main__':
    unittest.main()