from TicTacToe import TicTacToe
from Board import Board

from Constants import SIZE_OF_BOARD


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