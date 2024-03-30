
from ITicTacToe import ITicTacToe, SIZE
from TicTacToe import TicTacToe


class UltimateTicTacToe(ITicTacToe):
    def __init__(self) -> None:
        super().__init__()


    def initialize_board(self):
        self.board = [[TicTacToe() for _ in range(0, SIZE)] for _ in range(0, SIZE)]
