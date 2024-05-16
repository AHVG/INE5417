from utils.Constants import SIZE_OF_BOARD

from model.TicTacToe import TicTacToe
from model.Board import Board


class UltimateTicTacToe(Board):
    """
    A classe representa um Ultimate Tic Tac Toe, isto é, um tabuleiro de jogo da velha de tabuleiros de jogos da velha
    """

    def __init__(self) -> None:
        """
        Inicializa um tabuleiro de jogo da velha com jogos da velha
        """
        super().__init__()
        self._childs = [[TicTacToe() for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)]

    def __str__(self) -> str:
        s = ""

        for line in range(SIZE_OF_BOARD * SIZE_OF_BOARD):
            for column in range(SIZE_OF_BOARD * SIZE_OF_BOARD):
                if column % SIZE_OF_BOARD == 0:
                    s += "  "

                child = self.get_childs()[line // SIZE_OF_BOARD][column // SIZE_OF_BOARD].get_childs()[line % 3][column % 3]
                s += child.get_value() if child.get_value() else "_"

            if (line + 1) % SIZE_OF_BOARD == 0:
                s += "\n"

            s += "\n"

        return s