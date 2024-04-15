from Coordinate import Coordinate
from Player import Player
from Board import Board


class RoundManager:
    """
    Classe que gerencia o round do jogo. A lógica do jogo de lance está aqui.

    Atributos
    ----------
        _ultimate_tic_tac_toe : Board
            Tabuleiro Ultimate Tic Tac Toe (tabuleiro de tabuleiros)
        _local_player : Player
            Player local (o que interage com a interface)
        _remote_player : Player
            Player remoto (O que envia movimentos para o player local ou o que envia proposta de início de partida)
        _current_player : Player
            Player que está atualmente jogando
    """
    
    def __init__(self, ultimate_tic_tac_toe: Board, local_player: Player, remote_player: Player) -> None:
        """
        Inicializa o gerenciador de round

        Args:
            ultimate_tic_tac_toe (Board): Um tabuleiro Ultimate Tic Tac Toe
            local_player (Player): Player local
            remote_player (Player): Player remoto
        """
        self._ultimate_tic_tac_toe: Board = ultimate_tic_tac_toe
        self._local_player: Player = local_player
        self._remote_player: Player = remote_player
        self._current_player: Player = local_player

    def get_ultimate_tic_tac_toe(self) -> Board:
        return self._ultimate_tic_tac_toe
    
    def set_ultimate_tic_tac_toe(self, new_ultimate_tic_tac_toe: Board) -> None:
        self._ultimate_tic_tac_toe = new_ultimate_tic_tac_toe

    def get_local_player(self) -> Player:
        return self._local_player
    
    def set_local_player(self, new_local_player: Player) -> None:
        self._local_player = new_local_player

    def get_remote_player(self) -> Player:
        return self._remote_player
    
    def set_remote_player(self, new_remote_player: Player) -> None:
        self._remote_player = new_remote_player

    def get_current_player(self) -> Player:
        return self._current_player
    
    def set_current_player(self, new_current_player: Player) -> None:
        self._current_player = new_current_player

    def switch_player(self) -> None:
        self._current_player = self._remote_player if self._current_player.get_symbol() == self._local_player.get_symbol() else self._local_player

    def put_marker(self, u_position: Coordinate, ttt_position: Coordinate) -> bool:
        """
        Coloca marcador se for uma casa válida (se está vazia e se está de acordo com o movimento anterior)

        Args:
            u_position (Coordinate): Coordenada no tabuleiro maior (referencia um tabuleiro menor)
            ttt_position (Coordinate): Coordenada no tabuleiro menor

        Returns:
            bool: Se houve colocação de marcador retorna True; do contrário False
        """

        # Verificar se é válido

        # Atualizando o tabuleiro
        ttt = self._ultimate_tic_tac_toe.get_childs()[u_position.get_y()][u_position.get_x()]
        ttt.get_childs()[ttt_position.get_y()][ttt_position.get_x()].set_value(self._current_player.get_symbol())
        
        # Verificar vencedor
        if self._ultimate_tic_tac_toe.check():
            print("vencedor")
        else:
            print("sem vencedor")

        self.switch_player()

        return True
