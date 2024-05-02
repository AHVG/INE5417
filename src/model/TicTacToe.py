from model.Constants import SIZE_OF_BOARD

from model.Board import Board


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
