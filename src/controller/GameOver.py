from controller.State import State


class GameOver(State):

    def reset(self):
        self._round_manager.switch_state("Ready")
