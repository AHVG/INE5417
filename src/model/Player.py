

class Player:
    """
    Classe que representa o player
    
    Atributos
    ----------
        _name : str
            Nome do jogador
        _symbol : str
            Simbolo que representa o jogador
        _winner : bool
            Indica se veceu ou não
    """

    def __init__(self, name: str = "", id: str = "", symbol: str = "", is_turn: bool = False, winner: bool = False) -> None:
        """
        Inicializa o jogador

        Args:
            name (str, optional): Nome do jogador. Defaults to "".
            id (str, optional): ID do jogador. Defaults to "".
            symbol (str, optional): Símbolo do jogador. Defaults to "".
            turn (bool, optional): É o turno do player. Defaults to False.
            winner (bool, optional): Venceu ou não venceu. Defaults to False.
        """
        self._name: str = name
        self._id = id
        self._symbol: str = symbol
        self._is_turn: bool = is_turn
        self._winner: bool = winner

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_id(self) -> str:
        return self._id
    
    def set_id(self, new_id: str) -> None:
        self._id = new_id

    def get_symbol(self) -> str:
        return self._symbol
    
    def set_symbol(self, new_symbol: str) -> None:
        self._symbol = new_symbol

    def get_winner(self) -> bool:
        return self._winner
    
    def set_winner(self, new_winner: bool) -> None:
        self._winner = new_winner
    
    def get_is_turn(self):
        return self._is_turn

    def set_is_turn(self, is_turn) -> None:
        self._is_turn = is_turn

    def set_as_first(self):
        self.set_is_turn(True)
        self.set_symbol("X")
    
    def set_as_second(self):
        self.set_is_turn(False)
        self.set_symbol("O")

    def toggle_turn(self):
        self._is_turn = not self._is_turn

    def reset(self, name: str = "", id: str = "", symbol: str = "", is_turn: bool = False, winner: bool = False):
        self._name: str = name
        self._id: str = id
        self._symbol: str = symbol
        self._is_turn: bool = is_turn
        self._winner: bool = winner
