

class Coordinate:

    def __init__(self, x=0, y=0) -> None:
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def set_x(self, new_x):
        self._x = new_x

    def get_y(self):
        return self._y
    
    def set_y(self, new_y):
        self._y = new_y
