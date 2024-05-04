from controller.State import State


class Waiting(State):

    def receive_move(self):
        pass
    
    def receive_withdrawal_notification(self):
        self._round_manager.switch_state("GameOver")
