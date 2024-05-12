from tkinter import messagebox

from dog.start_status import StartStatus
from dog.dog_actor import DogActor

from utils.Coordinate import Coordinate

from model.Player import Player
from model.Board import Board


states = ("init", "playing", "waiting_for_oponent", "gameover")


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
    
    def __init__(self, ultimate_tic_tac_toe: Board, local_player: Player, remote_player: Player, dog_server: DogActor) -> None:
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
        self._current_state = "init"
        self._dog_server = dog_server
        self._last_move = None

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
        return self._current_state

    def set_current_state(self, current_state):
        self._current_state = current_state
    
    def get_last_move(self) -> Coordinate:
        return self._last_move
    
    def set_last_move(self, last_move: tuple):  # primeiro elemento é a coordenada do ultimate e o segundo é a coordenada do ttt
        self._last_move = last_move

    def convert_dict_to_coordinates(self, a_move: dict):
        u_position = Coordinate(a_move["u"][0], a_move["u"][1])
        ttt_position = Coordinate(a_move["ttt"][0], a_move["ttt"][1])
        return u_position, ttt_position

    def switch_player(self) -> None:
        self._current_player = self._remote_player if self._current_player.get_symbol() == self._local_player.get_symbol() else self._local_player

    def verify_move_validity(self, u_position, ttt_position):
        # Atualizando o tabuleiro
        last_move = self.get_last_move()

        # Ou seja, se não for a primeira jogada verifica se é possível colocar marcador
        if last_move:
            _, previous_ttt_position = last_move

            correct_ttt = self._ultimate_tic_tac_toe.get_childs()[previous_ttt_position.get_y()][previous_ttt_position.get_x()]

            current_ttt = self._ultimate_tic_tac_toe.get_childs()[u_position.get_y()][u_position.get_x()]
            current_position = current_ttt.get_childs()[ttt_position.get_y()][ttt_position.get_x()]

            # Verifica se o ttt que o jogador deve jogar tem vencedor
            if not correct_ttt.get_value():
                if u_position != previous_ttt_position:
                    return False

            # Verificar se tem vencedor no ttt e se sua posição está ocupada
            if current_ttt.get_value() or current_position.get_value():
                return False

        return True

    def put_marker(self, u_position: Coordinate, ttt_position: Coordinate):
        
        if not self.verify_move_validity():
            return False

        ttt = self.get_ultimate_tic_tac_toe().get_childs()[u_position.get_y()][u_position.get_x()]

        ttt.get_childs()[ttt_position.get_y()][ttt_position.get_x()].set_value(self.get_current_player().get_symbol())

        self.switch_player()

        self._last_ttt_position = (u_position, ttt_position)

        return True

    def set_start(self, start_status: StartStatus):
        players = start_status.get_players()
        local_id = start_status.get_local_id()

        self._local_player.set_id(local_id)
        self._local_player.set_symbol("X")

        self._remote_player.set_name(players[1][0])
        self._remote_player.set_id(players[1][1])
        self._remote_player.set_symbol("O")

        if players[0][2] == "1":
            self._current_state = "playing"
            self._current_player = self._local_player
        else:
            self._current_state = "waiting_for_oponent"
            self._current_player = self._remote_player

    def reset(self):
        print(f"reset acionado no estado {self.get_current_state()}")
        if self.get_current_state() == "init" or self.get_current_state() == "gameover":
            self._ultimate_tic_tac_toe.reset()
            self._local_player.reset(name=self.get_local_player().get_name())
            self._remote_player.reset()
    
    def start_match(self):
        print(f"start_match acionado no estado {self.get_current_state()}")
        if self.get_current_state() == "init":
            start_status = self._dog_server.start_match(2)
            messagebox.showinfo(message=start_status.get_message())

            if start_status.code == '2':
                self.set_start(start_status)

    def receive_start(self, start_status: StartStatus):
        print(f"receive_start acionado no estado {self.get_current_state()}")
        if self.get_current_state() == "init" or self.get_current_state() == "gameover":
            self.reset()
            self.set_start(start_status)

        messagebox.showinfo(message=start_status.get_message())
    
    def receive_move(self, a_move):
        print(f"receive_move acionado no estado {self.get_current_state()}")
        if self.get_current_state() == "waiting_for_oponent":
            u_position, ttt_position = self.convert_dict_to_coordinates(a_move)
            
            if self.put_marker(u_position, ttt_position):
                if self._ultimate_tic_tac_toe.check():
                    self.set_current_state("gameover")
                    self._remote_player.set_winner(True)
                else:
                    self.set_current_state("playing")

        messagebox.showinfo(message="Recebendo movimento")
    
    def receive_withdrawal_notification(self):
        print(f"receive_withdrawal_notification acionado no estado {self.get_current_state()}")

        if self.get_current_state() == "playing" or self.get_current_state() == "wating_for_oponent":
            self.set_current_state("gameover")
            self._local_player.set_winner(True) # Colocar no documento que, quando alguem desiste, esta pessoa perde

        messagebox.showinfo(message="Oponente desistiu")

    def on_click_board(self, u_position: Coordinate, ttt_position: Coordinate) -> bool:
        print(f"on_click_board acionado no estado {self.get_current_state()}")
        if self.get_current_state() == "playing":
            if self.put_marker(u_position, ttt_position):
                
                if self._ultimate_tic_tac_toe.check():
                    self.set_current_state("gameover")
                    self._local_player.set_winner(True)
                else:
                    self.set_current_state("waiting_for_oponent")

                self._dog_server.send_move({
                    "u": (u_position.get_x(), u_position.get_y()),
                    "ttt": (ttt_position.get_x(), ttt_position.get_y()),
                    "match_status": "next",
                })

        messagebox.showinfo(message=f"Colocando marcador no tabuleiro {u_position} na posição {ttt_position}")
