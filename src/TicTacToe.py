
from ITicTacToe import ITicTacToe
from IPosition import IPosition, Position


class TicTacToe(ITicTacToe, IPosition):
    def __init__(self) -> None:
        super().__init__()
        self.initialize_board()

    
    def initialize_board(self):
        self.board = [[Position() for _ in range(0, 3)] for _ in range(0, 3)]


    def get_value(self):
        return self.winner


    def set_value(self, new_value):
        self.winner = new_value
