from Constants import SIZE_OF_BOARD
from Board import Board


class TicTacToe(Board):

    def __init__(self) -> None:
        super().__init__()
        self._childs = [[Board() for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)]
