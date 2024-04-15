from Board import Board

from Constants import SIZE_OF_BOARD


class TicTacToe(Board):
    """
    A classe representa um jogo da velha padrão
    """

    def __init__(self) -> None:
        """
        Inicializa o jogo da velha com casas vazias
        """
        super().__init__()
        self._childs = [[Board() for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)]
