import _tkinter
import tkinter
import unittest
import time

from unittest.mock import patch, Mock

from dog.start_status import StartStatus

from view.PlayerActor import PlayerActor

import unittest

import _tkinter
import tkinter



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

    async def _start_app(self):
        self.local_actor.run()

    @patch('controller.Ready.messagebox.showinfo')
    @patch('view.PlayerActor.DogActor')
    def test_start_match(self, mock_dog_actor, mock_showinfo):

        mock_instance = mock_dog_actor.return_value

        mock_instance.initialize.return_value = "Alo"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["321", "2", "2"]], "123")
        mock_instance.start_match.return_value = start_status

        self._start_app()

        self.local_actor = PlayerActor(True)
        self.root = self.local_actor.get_root()
        self.pump_events()

        self.local_actor.start_match()
        self.local_actor.get_buttons()[0][0][0][0].invoke()
        self.pump_events()

        self.local_actor.receive_move({"u": (1, 1), "ttt": (1, 1)})
        self.pump_events()

        time.sleep(4)