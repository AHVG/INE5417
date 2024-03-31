from Position import Position



class Board(Position):

    SIZE = 3

    def __init__(self, position_type=Position) -> None:
        super().__init__()
        self.board = None
        self.initialize_board(position_type)


    def initialize_board(self, position_type):
        self.board = [[position_type() for _ in range(0, Board.SIZE)] for _ in range(0, Board.SIZE)]


    def get_lines(self):
        return [line[:] for line in self.board]


    def get_columns(self):
        return [[self.board[i][j] for i in range(Board.SIZE)] for j in range(Board.SIZE)]


    def get_diagonals(self):
        return [[self.board[i][i] for i in range(Board.SIZE)], [self.board[j][i] for j, i in zip(list(range(Board.SIZE)), list(range(Board.SIZE - 1, -1, -1)))]]


    def check_winner(self):
        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set([position.get_value() for position in region])) == 1 and region[0].get_value():
                self.set_value(region[0].get_value())
                return region[0].get_value()

        return None
