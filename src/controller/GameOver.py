from controller.State import State
from controller.Waiting import Waiting


class GameOver(State):

    def reset(self):
        self._round_manager.switch_state(Waiting(self._round_manager))
