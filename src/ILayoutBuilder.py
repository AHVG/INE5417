from abc import ABC, abstractmethod


class ILayoutBuilder(ABC):

    @abstractmethod
    def build(self):
        pass
