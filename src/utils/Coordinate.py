

class Coordinate:
    """
    Classe utilitária para representar coordenadas no campo do jogo da velha

    Atributos
    ----------
        _x : float
            Valor do x no par ordenada
        _y : float
            Valor de y no par ordenado
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self._x: float = x
        self._y: float = y

    def get_x(self) -> float:
        return self._x
    
    def set_x(self, new_x: float) -> None:
        self._x = new_x

    def get_y(self) -> float:
        return self._y
    
    def set_y(self, new_y: float) -> None:
        self._y = new_y
    
    def __str__(self) -> str:
        return f"Cordinate(x={self.get_x()}, y={self.get_y()})"

    def __eq__(self, other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
