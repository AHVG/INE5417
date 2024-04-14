from Constants import SIZE_OF_BOARD


class Board:

    def __init__(self) -> None:
        self._childs: list[list[Board]] = []
        self._value = None

    def get_childs(self):
        return self._childs
    
    def set_childs(self, new_childs):
        self._childs = new_childs

    def get_value(self):
        return self._value
    
    def set_value(self, new_value):
        self._value = new_value

    def get_lines(self):
        return [line[:] for line in self._childs]

    def get_columns(self):
        return [[self._childs[i][j] for i in range(SIZE_OF_BOARD)] for j in range(SIZE_OF_BOARD)]

    def get_diagonals(self):
        return [[self._childs[i][i] for i in range(SIZE_OF_BOARD)],
                [self._childs[j][i] for j, i in zip(list(range(SIZE_OF_BOARD)), list(range(SIZE_OF_BOARD - 1, -1, -1)))]]

    def check(self):
        if self.get_value():
            return self.get_value()
        
        if not self._childs:
            return self.get_value()

        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set([position.check() for position in region])) == 1 and region[0].get_value():
                self.set_value(region[0].get_value())
                print(f"Player {self.get_value()} won")
                return region[0].get_value()

        return None
