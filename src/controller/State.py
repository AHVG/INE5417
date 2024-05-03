from abc import ABC
from utils.Coordinate import Coordinate


class State(ABC):

    def __init__(self, round_manager) -> None:
        super().__init__()
        self._round_manager = round_manager

    def reset(self):
        pass
    
    def start_match(self):
        pass
    
    def receive_start(self):
        pass
    
    def receive_move(self):
        pass
    
    def receive_withdrawal_notification(self):
        pass

    def put_marker(self, u_position: Coordinate, ttt_position: Coordinate) -> bool:
        pass
