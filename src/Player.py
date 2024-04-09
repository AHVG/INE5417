

class Player:

    def __init__(self, name="", symbol="", winner=False) -> None:
        self._name = name
        self._symbol = symbol
        self._winner = winner

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

    def get_symbol(self):
        return self._symbol
    
    def set_symbol(self, new_symbol):
        self._symbol = new_symbol

    def get_winner(self):
        return self._winner
    
    def set_winner(self, new_winner):
        self._winner = new_winner
