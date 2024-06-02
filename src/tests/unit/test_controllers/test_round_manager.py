import unittest

from unittest.mock import MagicMock
from tkinter import messagebox

from dog.dog_actor import DogActor
from dog.start_status import StartStatus

from utils.Coordinate import Coordinate

from controller.RoundManager import RoundManager

from model.UltimateTicTacToe import UltimateTicTacToe
from model.Player import Player


class TestRoundManager(unittest.TestCase):
    def setUp(self):
        # Mocking dependencies
        self.board = UltimateTicTacToe()
        self.local_player = Player(name="Local player", id="1", symbol="X")
        self.remote_player = Player(name="1", id="2", symbol="O")
        self.dog_actor = MagicMock(spec=DogActor)

        self.dog_actor.initialize.return_value = "Alo"
        start_status = StartStatus("2", "A partida começou", [["Local player", "1", "1"], ["Remote player", "2", "2"]], "123")
        self.dog_actor.start_match.return_value = start_status

        # RoundManager instance
        self.round_manager = RoundManager(self.board, self.local_player, self.remote_player, self.dog_actor)
        
        # Mock messagebox to avoid GUI pop up during tests
        messagebox.showinfo = MagicMock()

    def test_initialization(self):
        self.assertIs(self.round_manager.get_ultimate_tic_tac_toe(), self.board)
        self.assertIs(self.round_manager.get_local_player(), self.local_player)
        self.assertIs(self.round_manager.get_remote_player(), self.remote_player)
    
    def test_convert_dict_to_coordinates(self):
        a_move = {"u": (1, 2), "ttt": (0, 1)}
        u_position, ttt_position = self.round_manager.convert_dict_to_coordinates(a_move)
        self.assertEqual(Coordinate(1, 2), u_position, "Ultimate Coordinate should be Coordinate(x=1, y=2)")
        self.assertEqual(Coordinate(0, 1), ttt_position, "TicTacToe Coordinate should be Coordinate(x=0, y=1)")

    def test_switch_player(self):
        self.local_player.set_is_turn(True)
        self.round_manager.toogle_player()
        self.assertTrue(self.remote_player.get_is_turn())
        self.round_manager.toogle_player()
        self.assertTrue(self.local_player.get_is_turn())

    def test_verify_move_validity(self):
        # Primeiro movimento
        self.assertEqual(self.round_manager.verify_move_validity(Coordinate(1, 1), Coordinate(0, 1)), True)

        # Movimento no tabuleiro correto vazio
        self.round_manager.set_last_move((Coordinate(2, 1), Coordinate(1, 1)))
        self.assertEqual(self.round_manager.verify_move_validity(Coordinate(1, 1), Coordinate(0, 1)), True)

        # Movimento no tabuleiro, mas com posição preenchida
        self.round_manager.set_last_move((Coordinate(2, 1), Coordinate(1, 1)))
        self.round_manager.get_ultimate_tic_tac_toe().get_childs()[1][1].get_childs()[1][0].set_value("X")
        self.assertEqual(self.round_manager.verify_move_validity(Coordinate(1, 1), Coordinate(0, 1)), False)

        # Movimento em um tabuleiro diferente, mas com o tabuleiro correto cheio
        self.round_manager.set_last_move((Coordinate(2, 1), Coordinate(1, 2)))
        self.round_manager.get_ultimate_tic_tac_toe().get_childs()[2][1].set_value("O")
        self.assertEqual(self.round_manager.verify_move_validity(Coordinate(0, 2), Coordinate(0, 1)), True)

    def test_put_marker(self):
        self.local_player.set_is_turn(True)

        # O jogador local joga
        self.assertEqual(self.round_manager.put_marker(Coordinate(2, 0), Coordinate(1, 1)), True)
        self.assertEqual(self.round_manager.get_ultimate_tic_tac_toe().get_childs()[0][2].get_childs()[1][1].get_value(), "X")
        self.assertEqual((Coordinate(2, 0), Coordinate(1, 1)), self.round_manager.get_last_move())

        # O jogador remoto joga
        self.assertEqual(self.round_manager.put_marker(Coordinate(1, 1), Coordinate(2, 2)), True)
        self.assertEqual(self.round_manager.get_ultimate_tic_tac_toe().get_childs()[1][1].get_childs()[2][2].get_value(), "O")
        self.assertEqual((Coordinate(1, 1), Coordinate(2, 2)), self.round_manager.get_last_move())

        # O jogador local joga, porém numa posição inválida
        self.assertEqual(self.round_manager.put_marker(Coordinate(1, 1), Coordinate(2, 2)), False)
        self.assertEqual(self.round_manager.get_ultimate_tic_tac_toe().get_childs()[1][1].get_childs()[2][2].get_value(), "O")
        self.assertEqual((Coordinate(1, 1), Coordinate(2, 2)), self.round_manager.get_last_move())

    def test_set_start(self):
        start_status = StartStatus("2", "A partida começou", [["Local player 123", "123123", "1"], ["Remote player 234", "234234", "2"]], "987654321")
        self.round_manager.set_start(start_status)

        self.assertEqual(self.local_player.get_name(), "Local player")
        self.assertEqual(self.local_player.get_id(), "123123")
        self.assertEqual(self.local_player.get_symbol(), "X")
        
        self.assertEqual(self.remote_player.get_name(), "Remote player 234")
        self.assertEqual(self.remote_player.get_id(), "234234")
        self.assertEqual(self.remote_player.get_symbol(), "O")

        self.assertIs(self.round_manager.get_last_move(), None)

        self.assertEqual(self.round_manager.get_current_state(), "playing")

    def test_reset_game(self):
        self.round_manager.set_current_state("gameover")
        self.round_manager.reset_game()
        self.assertEqual(self.round_manager.get_current_state(), "init")

        self.round_manager.reset_game()
        self.assertEqual(self.round_manager.get_current_state(), "init")

    def test_start_match(self):
        self.round_manager.start_match()

        self.assertEqual(self.round_manager.get_current_state(), "playing")

        self.assertEqual(self.local_player.get_name(), "Local player")
        self.assertEqual(self.local_player.get_id(), "1")
        self.assertEqual(self.local_player.get_symbol(), "X")
        
        self.assertEqual(self.remote_player.get_name(), "Remote player")
        self.assertEqual(self.remote_player.get_id(), "2")
        self.assertEqual(self.remote_player.get_symbol(), "O")

        self.assertIs(self.round_manager.get_last_move(), None)

    def test_receive_start(self):
        start_status = StartStatus("2", "A partida começou", [["Local player", "321", "2"], ["Guest123321", "2", "1"]], "local_id")
        self.round_manager.receive_start(start_status)

        self.assertEqual(self.round_manager.get_current_state(), "waiting_for_oponent")

        self.assertEqual(self.local_player.get_name(), "Local player")
        self.assertEqual(self.local_player.get_id(), "321")
        self.assertEqual(self.local_player.get_symbol(), "O")
        
        self.assertEqual(self.remote_player.get_name(), "Guest123321")
        self.assertEqual(self.remote_player.get_id(), "2")
        self.assertEqual(self.remote_player.get_symbol(), "X")

        self.assertIs(self.round_manager.get_last_move(), None)

    def test_receive_move(self):
        start_status = StartStatus("2", "A partida começou", [["Local player", "1", "2"], ["Guest123321", "2", "1"]], "321")
        self.round_manager.receive_start(start_status)

        a_move = {"u": (0, 0), "ttt": (2, 2)}
        self.round_manager.receive_move(a_move)

        self.assertEqual(self.round_manager.get_current_state(), "playing")

    def test_receive_move_gameover(self):
        start_status = StartStatus("2", "A partida começou", [["Local player", "1", "2"], ["Guest123321", "2", "1"]], "321")
        self.round_manager.receive_start(start_status)

        self.board.set_value("O")
        a_move = {"u": (0, 0), "ttt": (2, 2)}
        self.round_manager.receive_move(a_move)

        self.assertEqual(self.round_manager.get_current_state(), "gameover")
        self.assertEqual(self.local_player.get_winner(), False)
        self.assertEqual(self.remote_player.get_winner(), True)

    def test_receive_withdrawal_notification(self):
        self.round_manager.set_current_state("playing")

        self.assertIs(self.board.get_value(), None, "Board value should be None")
        self.assertEqual(self.local_player.get_winner(), False, "Should there isn't winner")
        self.assertEqual(self.remote_player.get_winner(), False, "Should there isn't winner")
        
        self.round_manager.receive_withdrawal_notification()

        self.assertEqual(self.board.get_value(), self.local_player.get_symbol(), "Board value should be equal to player symbol")
        self.assertEqual(self.local_player.get_winner(), True, "Local player should be the winner")
        self.assertEqual(self.remote_player.get_winner(), False, "Remote player should not be the winner")

    def test_on_click_board(self):
        self.round_manager.start_match()

        self.round_manager.on_click_board(Coordinate(1, 1), Coordinate(1, 1))
        self.assertEqual(self.round_manager.get_current_state(), "waiting_for_oponent")

    def test_on_click_board_gameover(self):
        self.round_manager.start_match()
        self.board.set_value("-")
        self.round_manager.on_click_board(Coordinate(1, 1), Coordinate(1, 1))
        self.assertEqual(self.round_manager.get_current_state(), "gameover")

        self.assertEqual(self.local_player.get_winner(), False)
        self.assertEqual(self.remote_player.get_winner(), False)


if __name__ == '__main__':
    unittest.main()
