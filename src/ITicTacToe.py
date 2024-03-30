from abc import ABC, abstractmethod

# TOOD: Encapsular isso
SIZE = 3


class ITicTacToe(ABC):
    def __init__(self) -> None:
        self.winner = None
        self.board = [[None for _ in range(0, SIZE)] for _ in range(0, SIZE)]


    def get_lines(self):
        return [line[:] for line in self.board]


    def get_columns(self):
        return [[self.board[i][j] for i in range(SIZE)] for j in range(SIZE)]


    def get_diagonals(self):
        return [[self.board[i][i] for i in range(SIZE)], [self.board[j][i] for j, i in zip(list(range(SIZE)), list(range(SIZE - 1, -1, -1)))]]

    @abstractmethod
    def checkWinner(self):
        pass
