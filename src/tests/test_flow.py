import threading
import unittest
import time

from unittest.mock import patch, Mock

from dog.start_status import StartStatus

from view.PlayerActor import PlayerActor


class TestFlow(unittest.TestCase):

    async def _start_app(self):
        self.local_actor.run()

    @patch('controller.Ready.messagebox.showinfo')
    @patch('view.PlayerActor.DogActor')
    def test_start_match(self, mock_dog_actor, mock_showinfo):

        mock_instance = mock_dog_actor.return_value

        mock_instance.initialize.return_value = "Alo"

        start_status = StartStatus("2", "A partida começou", [["123", "1", "1"], ["321", "2", "2"]], "123")
        mock_instance.start_match.return_value = start_status

        self.local_actor = PlayerActor(True)

        self._start_app()

        self.local_actor.start_match()
        self.local_actor.get_buttons()[0][0][0][0].invoke()
        self.local_actor.get_buttons()[0][0][0][0].config(text="123123")

        time.sleep(4)