

class TicTacToe:
    def __init__(self) -> None:
        self.board = [[None for _ in range(0, 3)] for _ in range(0, 3)]


    def get_lines(self):
        return [line[:] for line in self.board]


    def get_columns(self):
        return [[self.board[i][j] for i in range(len(self.board))] for j in range(len(self.board[0]))]


    def get_diagonals(self):
        return [[self.board[i][i] for i in range(len(self.board))], [self.board[j][i] for j, i in zip(list(range(3)), list(range(2, -1, -1)))]]


    def checkWinner(self):
        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set(region)) == 1 and region[0]:
                return region[0]

        return None

