import time
import random
import _tkinter
import unittest

from unittest.mock import patch

from dog.start_status import StartStatus

from view.PlayerActor import PlayerActor

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


class TestStartMatch(TKinterTestCase):

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

    @patch('controller.RoundManager.messagebox.showinfo')
    @patch('view.PlayerActor.simpledialog.askstring')
    @patch('view.PlayerActor.DogActor')
    def test_playing(self, mock_dog_actor, mock_askstring, mock_showinfo):

        mock_askstring.return_value = "Local player"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], [str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance = mock_dog_actor.return_value
        mock_instance.initialize.return_value = "Alo"
        mock_instance.start_match.return_value = start_status

        self.local_actor = PlayerActor()
        self.root = self.local_actor.get_root()
        self.pump_events()

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
        time.sleep(5)

        self.local_actor.reset()
        self.pump_events()

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], [str(random.randint(0, 10000)), "2", "2"]], "123")
        mock_instance.start_match.return_value = start_status

        self.run_round(plays)
        time.sleep(5)