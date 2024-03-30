from abc import ABC, abstractmethod


class IPosition(ABC):

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, new_value):
        pass


class Position(IPosition):

    def __init__(self) -> None:
        super().__init__()
        self.value = None


    def get_value(self):
        return self.value
    

    def set_value(self, new_value):
        self.value = new_value