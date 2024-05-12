from utils.Constants import SIZE_OF_BOARD

class Board: pass


SYMBOLS = (None, "-", "X", "O")

class Board:
    """
    Classe que representa tanto uma casa no tabuleiro quanto um tabuleiro padrão de jogo da velha e um Ultimate tabuleiro de jogo da velha

    Atributos
    ----------
        _childs : list[list[Board]]
            Casas, para o caso de ser um Tic Tac Toe, ou tabuleiros, para o caso de um Ultimate Tic Tac Toe
        _value : str
            Representa o ganhador do board. Se for uma casa, representa quem a ocupou
    """

    def __init__(self) -> None:
        """
        Inicializa um tabuleiro como se fosse uma casa por padrão
        """
        self._childs: list[list[Board]] = None
        self._value: str = None

    def get_childs(self):
        return self._childs
    
    def set_childs(self, new_childs) -> None:
        self._childs = new_childs

    def get_value(self) -> str:
        return self._value
    
    def set_value(self, new_value: str) -> None:
        self._value = new_value

    def get_lines(self):
        return [line[:] for line in self._childs]

    def get_columns(self):
        return [[self._childs[i][j] for i in range(SIZE_OF_BOARD)] for j in range(SIZE_OF_BOARD)]

    def get_diagonals(self):
        return [[self._childs[i][i] for i in range(SIZE_OF_BOARD)],
                [self._childs[j][i] for j, i in zip(list(range(SIZE_OF_BOARD)), list(range(SIZE_OF_BOARD - 1, -1, -1)))]]

    def reset(self):
        self._value = None

        if not self._childs:
            return

        for line in self._childs:
            for element in line:
                element.reset()

    def check_result(self) -> str:
        """
        Checa a vitória do tabuleiro. Se alguem venceu, então define value como o vencedor.

        Returns:
            str: Retorna o vencedor ("X" ou "O"); Se não tiver um, retornar None
        """
        if self.get_value():
            return self.get_value()
        
        if not self.get_childs():
            return self.get_value()

        for line in self.get_childs():
            for position in line:
                position.check_result()

        regions = [*self.get_lines(), *self.get_columns(), *self.get_diagonals()]

        for region in regions:
            if len(set(map(lambda position: position.get_value(), region))) == 1 and region[0].get_value() in ("X", "O"):
                self.set_value(region[0].get_value())
                print(f"Player {self.get_value()} won")
                return region[0].get_value()

        filled_positions = 0

        for line in self.get_childs():
            for position in line:
                if position.get_value():
                    filled_positions += 1

        if filled_positions == SIZE_OF_BOARD * SIZE_OF_BOARD:
            self.set_value("-")
            return "-"

        return None
