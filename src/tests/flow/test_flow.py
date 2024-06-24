import random
import _tkinter
import unittest

from unittest.mock import patch

from generate_game import generate_game

from dog.start_status import StartStatus

from view.PlayerActor import PlayerActor

from utils.Constants import SIZE_OF_BOARD

import unittest


# @see https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app
class TKinterTestCase(unittest.TestCase):
    """
    These methods are going to be the same for every GUI test,
    so refactored them into a separate class
    """
    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass

class TestFlow(TKinterTestCase):
    # TODO: usar thread para simular o jogador remoto?
    # TODO: Adicionar comparação de tabuleiro?
    # TODO: Criar outra classe para outros testes?

    def run_round(self, moves):
        self.local_actor.start_match()
        
        for i, move in enumerate(moves):
            u_move = (move[0][0], move[0][1])
            ttt_move = (move[1][0], move[1][1])

            if (i + 1) % 2:
                self.local_actor.get_buttons()[u_move[1]][u_move[0]][ttt_move[1]][ttt_move[0]].invoke()
                self.pump_events()
            else:
                self.local_actor.receive_move({"u": u_move, "ttt": ttt_move})
                self.pump_events()

            # from time import sleep
            # sleep(1)

    @patch('view.PlayerActor.simpledialog.askstring')
    @patch('view.PlayerActor.DogActor')
    def test_when_the_game_local_player_wins(self, mock_dog_actor, mock_askstring):

        mock_askstring.return_value = "Local player"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Conectado ao Dog Server"
        mock_instance.start_match.return_value = start_status

        self.local_actor = PlayerActor()
        self.root = self.local_actor.get_root()
        self.pump_events()

        # X _ O  _ X _  O _ X
        # _ X _  _ X _  _ X _
        # _ _ X  _ X _  X _ _
        # 
        # _ _ _  O O O  _ _ _
        # _ _ _  _ _ _  _ _ _
        # _ _ _  _ _ _  _ _ _
        # 
        # _ _ O  _ O _  _ _ O
        # _ _ _  _ _ _  _ _ _
        # _ _ _  _ _ _  _ _ _

        plays = [([0, 0], [0, 0]),
                 ((0, 0), (2, 0)),
                 ([2, 0], [2, 0]),
                 ((2, 0), (0, 0)),
                 ([0, 0], [2, 2]),
                 ((2, 2), (2, 0)),
                 ([2, 0], [0, 2]),
                 ((0, 2), (2, 0)),
                 ([2, 0], [1, 1]),
                 ((1, 1), (0, 0)),
                 ([0, 0], [1, 1]),
                 ((1, 1), (1, 0)),
                 ([1, 0], [1, 1]),
                 ((1, 1), (2, 0)),
                 ([1, 0], [1, 2]),
                 ((1, 2), (1, 0)),
                 ((1, 0), (1, 0))]

        self.run_round(plays)
        self.pump_events()

        self.local_actor.reset_game()

    @patch('view.PlayerActor.simpledialog.askstring')
    @patch('view.PlayerActor.DogActor')
    def test_when_the_game_remote_player_wins(self, mock_dog_actor, mock_askstring):
        
        mock_askstring.return_value = "Local player"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Conectado ao Dog Server"
        mock_instance.start_match.return_value = start_status

        self.local_actor = PlayerActor()
        self.root = self.local_actor.get_root()
        self.pump_events()

        # _ _ X  _ _ _  O _ X
        # _ _ _  _ _ _  _ O _
        # _ _ _  X _ _  _ _ O
        # 
        # _ _ X  _ _ O  _ _ _
        # _ _ _  _ X O  _ X _
        # _ _ _  _ _ O  _ _ _
        # 
        # _ O _  _ _ _  _ _ _
        # _ O _  _ _ _  _ X _
        # _ O _  X _ _  _ _ _

        plays = [((2, 2), (0, 2)),
                 ((0, 2), (1, 0)),
                 ((1, 0), (0, 2)),
                 ((0, 2), (1, 2)),
                 ((1, 2), (0, 2)),
                 ((0, 2), (1, 1)),
                 ((1, 1), (1, 1)),
                 ((1, 1), (2, 2)),
                 ((2, 2), (1, 1)),
                 ((1, 1), (2, 1)),
                 ((2, 1), (1, 1)),
                 ((1, 1), (2, 0)),
                 ((2, 0), (2, 0)),
                 ((2, 0), (0, 0)),
                 ((0, 0), (2, 0)),
                 ((2, 0), (1, 1)),
                 ((0, 1), (2, 0)),
                 ((2, 0), (2, 2))]

        self.run_round(plays)
        self.pump_events()

        self.local_actor.reset_game()

    @patch('view.PlayerActor.simpledialog.askstring')
    @patch('view.PlayerActor.DogActor')
    def test_when_the_game_ends_in_a_draw(self, mock_dog_actor, mock_askstring):

        mock_askstring.return_value = "Local player"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Conectado ao Dog Server"
        mock_instance.start_match.return_value = start_status

        self.local_actor = PlayerActor()
        self.root = self.local_actor.get_root()
        self.pump_events()

        # X _ _  _ _ O  O X O
        # X _ O  O X O  X X O
        # X X O  O _ O  O O X

        # X X _  O X O  _ _ X
        # _ _ _  O O X  O X O
        # O O O  X X O  X O _

        # O X X  X O _  X X O
        # _ O X  X X X  X O X
        # _ O O  X O _  X O X

        plays = [((2, 2), (0, 1)), ((0, 1), (1, 2)), ((1, 2), (0, 0)), ((0, 0), (2, 2)), ((2, 2), (0, 2)), ((0, 2), (1, 2)), ((1, 2), (1, 1)), ((1, 1), (2, 0)), ((2, 0), (0, 1)), ((0, 1), (0, 2)), ((0, 2), (2, 0)), ((2, 0), (0, 0)), ((0, 0), (1, 2)), ((1, 2), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((0, 1), (1, 0)), ((1, 0), (0, 2)), ((0, 2), (1, 0)), ((1, 0), (2, 1)), ((2, 1), (2, 0)), ((2, 0), (0, 2)), ((0, 2), (2, 1)), ((2, 1), (0, 1)), ((0, 1), (0, 0)), ((0, 0), (2, 1)), ((2, 1), (1, 1)), ((1, 1), (1, 1)), ((1, 1), (2, 1)), ((2, 1), (1, 2)), ((1, 2), (2, 1)), ((2, 1), (2, 1)), ((2, 1), (0, 2)), ((0, 2), (0, 0)), ((0, 0), (0, 2)), ((0, 2), (2, 2)), ((2, 2), (2, 2)), ((2, 2), (1, 2)), ((1, 2), (0, 2)), ((0, 2), (1, 1)), ((1, 1), (1, 2)), ((1, 2), (1, 2)), ((1, 2), (0, 1)), ((0, 1), (2, 2)), ((2, 2), (1, 0)), ((1, 0), (2, 0)), ((2, 0), (1, 1)), ((1, 1), (0, 0)), ((0, 0), (0, 1)), ((2, 2), (2, 0)), ((2, 0), (2, 2)), ((2, 2), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (0, 1)), ((0, 0), (0, 0)), ((1, 0), (2, 2)), ((2, 2), (2, 1)), ((2, 0), (2, 0)), ((2, 0), (1, 0)), ((2, 0), (1, 2)), ((1, 1), (0, 2)), ((2, 0), (2, 1)), ((2, 2), (0, 0)), ((1, 1), (2, 2))]

        self.run_round(plays)
        self.pump_events()

        self.local_actor.reset_game()

    @patch('view.PlayerActor.simpledialog.askstring')
    @patch('view.PlayerActor.DogActor')
    def test_when_playing_more_than_once(self, mock_dog_actor, mock_askstring):
        
        mock_askstring.return_value = "Local player"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Conectado ao Dog Server"
        mock_instance.start_match.return_value = start_status

        self.local_actor = PlayerActor()
        self.root = self.local_actor.get_root()
        self.pump_events()

        plays, _ = generate_game()

        self.run_round(plays)
        self.pump_events()

        self.local_actor.reset_game()

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Conectado ao Dog Server"
        mock_instance.start_match.return_value = start_status

        plays, _ = generate_game()

        self.run_round(plays)
        self.pump_events()

        self.local_actor.reset_game()

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["Remote player " + str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Conectado ao Dog Server"
        mock_instance.start_match.return_value = start_status

        plays, _ = generate_game()

        self.run_round(plays)
        self.pump_events()

        self.local_actor.reset_game()
