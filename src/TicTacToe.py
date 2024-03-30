
from ITicTacToe import ITicTacToe, SIZE
from IPosition import IPosition, Position


class TicTacToe(ITicTacToe, IPosition):
    def __init__(self) -> None:
        super().__init__()
        self.initialize_board()

    
    def initialize_board(self):
        self.board = [[Position() for _ in range(0, SIZE)] for _ in range(0, SIZE)]


    def get_value(self):
        return self.winner


    def set_value(self, new_value):
        self.winner = new_value
