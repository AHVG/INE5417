from dog.start_status import StartStatus

from utils.Coordinate import Coordinate

from controller.Ready import Ready
from controller.Playing import Playing
from controller.Waiting import Waiting
from controller.GameOver import GameOver

from model.Player import Player
from model.Board import Board


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
        self._current_player: Player = None
        self._current_state = Ready(self)
        self._states = {
            "Ready": Ready(self),
            "Playing": Playing(self),
            "Waiting": Waiting(self),
            "GameOver": GameOver(self),
        }

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

    def get_current_state(self):
        return self._state

    def set_current_state(self, current_state):
        self._current_state = current_state

    def switch_player(self) -> None:
        self._current_player = self._remote_player if self._current_player.get_symbol() == self._local_player.get_symbol() else self._local_player

    def switch_state(self, new_state) -> None:
        print(f"Trocando de estado de {type(self._current_state)} para {self._states[new_state]}")
        self._current_state.exit()
        self.set_current_state(self._states[new_state])
        self._current_state.entry()

    def reset(self):
        self._current_state.reset()
    
    def start_match(self, start_status: StartStatus):
        self._current_state.start_match(start_status)
    
    def receive_start(self, start_status: StartStatus):
        self._current_state.receive_start(start_status)
    
    def receive_move(self, a_move):
        self._current_state.receive_move(a_move)
    
    def receive_withdrawal_notification(self):
        self._current_state.receive_withdrawal_notification()

    def put_marker(self, u_position: Coordinate, ttt_position: Coordinate) -> bool:
        return self._current_state.put_marker(u_position, ttt_position)
