from Constants import SIZE_OF_BOARD


class Board:

    def __init__(self) -> None:
        self.childs: list[list[Board]] = []
        self.value = None

    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value

    def get_lines(self):
        return [line[:] for line in self.childs]

    def get_columns(self):
        return [[self.childs[i][j] for i in range(SIZE_OF_BOARD)] for j in range(SIZE_OF_BOARD)]

    def get_diagonals(self):
        return [[self.childs[i][i] for i in range(SIZE_OF_BOARD)], [self.childs[j][i] for j, i in zip(list(range(SIZE_OF_BOARD)), list(range(SIZE_OF_BOARD - 1, -1, -1)))]]

    def check(self):
        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set([position.get_value() for position in region])) == 1 and region[0].get_value():
                self.set_value(region[0].get_value())
                print(f"Player {self.get_value()} won")
                return region[0].get_value()

        return None
