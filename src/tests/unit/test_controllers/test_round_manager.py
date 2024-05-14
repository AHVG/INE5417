import random
import unittest

from unittest.mock import MagicMock
from tkinter import messagebox

from dog.dog_actor import DogActor
from dog.start_status import StartStatus

from controller.RoundManager import RoundManager

from model.UltimateTicTacToe import UltimateTicTacToe
from model.Player import Player


class TestRoundManager(unittest.TestCase):
    def setUp(self):
        # Mocking dependencies
        self.board = UltimateTicTacToe()
        self.local_player = Player(name="Local Player", id="1", symbol="X")
        self.remote_player = Player(name="Remote Player", id="2", symbol="O")
        self.dog_actor = MagicMock(spec=DogActor)

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        self.dog_actor.initialize.return_value = "Alo"
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
        pass

    def test_switch_player(self):
        self.round_manager.set_current_player(self.local_player)
        self.round_manager.switch_player()
        self.assertIs(self.round_manager.get_current_player(), self.remote_player)
        self.round_manager.switch_player()
        self.assertIs(self.round_manager.get_current_player(), self.local_player)

    def test_verify_move_validity(self):
        pass

    def test_put_marker(self):
        pass

    def test_set_start(self):
        pass

    def test_reset_game(self):
        self.round_manager.reset_game()
        self.assertIsNone(self.round_manager.get_last_move())
        self.assertEqual(self.round_manager.get_current_state(), "init")

    def test_start_match(self):
        pass

    def test_receive_start(self):
        pass

    def test_receive_move(self):
        pass

    def test_receive_withdrawal_notification(self):
        pass

    def test_on_click_board(self):
        pass


if __name__ == '__main__':
    unittest.main()
