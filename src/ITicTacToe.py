from abc import ABC, abstractmethod

# TOOD: Encapsular isso
SIZE = 3


class ITicTacToe(ABC):
    def __init__(self) -> None:
        self.winner = None
        self.board = None

        self.initialize_board()


    @abstractmethod
    def initialize_board(self):
        pass


    def get_lines(self):
        return [line[:] for line in self.board]


    def get_columns(self):
        return [[self.board[i][j] for i in range(SIZE)] for j in range(SIZE)]


    def get_diagonals(self):
        return [[self.board[i][i] for i in range(SIZE)], [self.board[j][i] for j, i in zip(list(range(SIZE)), list(range(SIZE - 1, -1, -1)))]]


    def check_winner(self):
        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set([position.get_value() for position in region])) == 1 and region[0].get_value():
                self.winner = region[0].get_value()
                return region[0].get_value()

        return None
