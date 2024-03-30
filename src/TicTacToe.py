
from ITicTacToe import ITicTacToe

class TicTacToe(ITicTacToe):
    def __init__(self) -> None:
        self.winner = None
        self.board = [[None for _ in range(0, 3)] for _ in range(0, 3)]


    def checkWinner(self):
        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set(region)) == 1 and region[0]:
                self.winner = region[0]
                return region[0]

        return None

