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
        lines = []
        childs = self.get_childs()

        for i in range(SIZE_OF_BOARD):
            lines.append(childs[i])

        return lines[:]

    def get_columns(self):
        columns = []
        childs = self.get_childs()

        for j in range(SIZE_OF_BOARD):
            column = []
            
            for i in range(SIZE_OF_BOARD):
                column.append(childs[i][j])

            columns.append(column)

        return columns[:]

    def get_diagonals(self):
        primary_diagonal = []
        secondary_diagonal = []
        childs = self.get_childs()

        for i in range(SIZE_OF_BOARD):
            primary_diagonal.append(childs[i][i])

        # equivalente a for (int i = 0, j = 2; i < 3; i++, j--) em C
        for i, j in zip(list(range(SIZE_OF_BOARD)), list(range(SIZE_OF_BOARD - 1, -1, -1))):
            secondary_diagonal.append(childs[i][j])

        diagonals = [primary_diagonal, secondary_diagonal]
        return diagonals

    def get_regions(self):
        lines = self.get_lines()
        columns = self.get_columns()
        diagonals = self.get_diagonals()
        return [*lines, *columns, *diagonals]

    def reset(self):
        self._value = None

        if not self._childs:
            return

        for line in self._childs:
            for element in line:
                element.reset()
    
    def check_region_winner(self, region):
        values = []

        for i in range(3):
            position = region[i]
            aux = position.get_value()
            values.append(aux)

        symbols = set(values)

        number_of_symbols = len(symbols)
        value = region[0].get_value()

        if number_of_symbols == 1 and value in ("X", "O"):
            return True
        
        return False

    def is_completely_filled(self) -> bool:
        filled_positions = 0
        childs = self.get_childs()

        for i in range(SIZE_OF_BOARD):
            for j in range(SIZE_OF_BOARD):
                position = childs[i][j]
                value = position.get_value()

                if value:
                    filled_positions += 1
                    
        if filled_positions == SIZE_OF_BOARD * SIZE_OF_BOARD:
            return True
        
        return False
    
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

        regions = self.get_regions()

        for region in regions:
            result = self.check_region_winner(region)

            if result:
                self.set_value(region[0].get_value())
                print(f"Player {self.get_value()} won")
                return region[0].get_value()

        if self.is_completely_filled():
            self.set_value("-")
            print(f"Draw")
            return "-"

        return None
