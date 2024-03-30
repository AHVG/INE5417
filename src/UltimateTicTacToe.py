
from ITicTacToe import ITicTacToe, SIZE
from TicTacToe import TicTacToe


class UltimateTicTacToe(ITicTacToe):
    def __init__(self) -> None:
        super().__init__()


    def initialize_board(self):
        for i in range(SIZE):
            for j in range(SIZE):
                self.board[i][j] = TicTacToe()
