from Constants import SIZE_OF_BOARD
from Board import Board
from TicTacToe import TicTacToe


class UltimateTicTacToe(Board):

    def __init__(self) -> None:
        super().__init__()
        self._childs = [[TicTacToe() for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)]