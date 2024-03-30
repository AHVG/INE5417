from abc import ABC, abstractmethod


# TODO: a ideia seria migrar para QT, pois TK é muito limitado (precisa perguntar para o professor se pode)
class IBoardBuilder(ABC):

    @abstractmethod
    def build(self):
        pass
