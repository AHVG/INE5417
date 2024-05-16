from utils.Constants import SIZE_OF_BOARD

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
    
    def __str__(self) -> str:
        s = ""
        for line in self.get_childs():
            for child in line:
                s += child.get_value() if child.get_value() else "_"
            s += "\n"
        return s