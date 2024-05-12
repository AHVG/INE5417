import random
import tkinter as tk

from tkinter import simpledialog, messagebox

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from dog.start_status import StartStatus

from utils.Constants import SIZE_OF_BOARD
from utils.Coordinate import Coordinate

from view.UIDirector import UIDirector
from view.UIBuilder import UIBuilder

from controller.RoundManager import RoundManager

from model.UltimateTicTacToe import UltimateTicTacToe
from model.Player import Player
from model.Board import Board


class PlayerActor(DogPlayerInterface):
    """
    Classe que modela a interação do player e do DOG com a aplicação    

    Atributos
    ----------
        _ultimate_ttt : Board
            Ultimate Tic Tac Toe
        _local_player : Player
            Player local
        _remote_player : Player
            Player remoto
        _round_manager : RoundManager
            Gerenciador de round que controla toda a lógica do jogo
        _root : tk.Tk
            Objeto do Tkidocsnter que gerencia a window
        _player_status : tk.Frame
            Frame da tela onde estão as informações do jogadores
        _board_frame : tk.Frame
            Frame da tela onde está o Ultimate Tic Tac Toe
        _buttons : list[list[list[list[tk.Button]]]]
            Botões que representam a casa de um tabuleiro Tic Tac Toe
        _player_img : ImageTk.PhotoImage
            Imagem do player
        _red_x_bg_white : ImageTk.PhotoImage
            Imagem do x vermelho com fundo branco
        _blue_o_bg_white : ImageTk.PhotoImage
            Imagem do o azul com fundo branco
        _dog_server : DogActor
            Ator DOG que age sobre PlayerActor (receive_move, receive_start, receive_withdrawal_notification)
    """

    def __init__(self) -> None:
        """
        Inicializa toda a aplicação: define o nome do player local; conecta-se com o DOG e cria tabuleiro
        """
        self._ultimate_ttt: Board = UltimateTicTacToe()
        self._local_player: Player = Player("Jogador local", "X")
        self._remote_player: Player = Player("Jogador remoto", "O")
        self._dog_server: DogActor = DogActor()
        self._round_manager: RoundManager = RoundManager(self._ultimate_ttt, self._local_player, self._remote_player, self._dog_server)

        self._ui_builder = UIBuilder(self)
        self._ui_director = UIDirector(self._ui_builder)
        self._ui_director.build()

        self._root = self._ui_director.get_root()

        self._red_x_bg_white = self._ui_director.get_red_x_bg_white()
        self._blue_o_bg_white = self._ui_director.get_blue_o_bg_white()

        self._board_frame = self._ui_director.get_board_frame()
        self._local_player_frame = self._ui_director.get_local_player_frame()
        self._remote_player_frame = self._ui_director.get_remote_player_frame()
        self._buttons = self._ui_director.get_buttons()

        self.connect_to_dog()
    
    def get_root(self):
        return self._root

    def get_buttons(self):
        return self._buttons
    
    def get_local_player_frame(self):
        return self._local_player_frame

    def get_remote_player_frame(self):
        return self._remote_player_frame

    def run(self):
        self._root.mainloop()

    def update_gui(self) -> None:
        """
        Atualiza o estado da GUI após processamento da lógica do jogo
        """
        coordinates = [Coordinate(x, y) for x in range(SIZE_OF_BOARD) for y in range(SIZE_OF_BOARD)]
        
        for u_coordinate in coordinates:
            u_x, u_y = u_coordinate.get_x(), u_coordinate.get_y()
            for ttt_coordinate in coordinates:
                ttt_x, ttt_y = ttt_coordinate.get_x(), ttt_coordinate.get_y()
                symbol = self._ultimate_ttt.get_childs()[u_y][u_x].get_childs()[ttt_y][ttt_x].get_value()
                symbol = "" if symbol is None else symbol
                self._buttons[u_y][u_x][ttt_y][ttt_x].config(text=symbol)
        
        self._local_player_frame.set_player_name(self._local_player.get_name())
        self._remote_player_frame.set_player_name(self._remote_player.get_name())

    def connect_to_dog(self):
        player_name = simpledialog.askstring(title="Player identifcation", prompt="Qual o seu nome?")
        message = self._dog_server.initialize(player_name, self)
        messagebox.showinfo(message=message)

        self._local_player.set_name(player_name)
        self.update_gui()

    def reset(self):
        print("reset chamado")
        self._round_manager.reset()
        self.update_gui()
        
    def quit(self):
        print("quit chamado")
        self._root.quit()

    def start_match(self) -> None:
        print("start_match chamado")
        self._round_manager.start_match()
        self.update_gui()

    def receive_start(self, start_status: StartStatus) -> None:
        print("receive_start chamado")
        self._round_manager.receive_start(start_status)
        self.update_gui()

    def receive_move(self, a_move) -> None:
        print("receive_move chamado")
        self._round_manager.receive_move(a_move)
        self.update_gui()

    def receive_withdrawal_notification(self) -> None:
        print("receive_withdrawal_notification chamado")
        self._round_manager.receive_withdrawal_notification()
        self.update_gui()

    def on_click_board(self, u_position: Coordinate, ttt_position: Coordinate) -> None:
        """
        Lida com o click do usuário no tabuleiro
        
        Args:
            u_position (Coordinate): Coordenada no tabuleiro maior (Ultimate)
            ttt_position (Coordinate): Coordenada no tabuleiro menor (Tic Tac Toe)
        """
        print("on_click_board chamado")
        self._round_manager.on_click_board(u_position, ttt_position)
        self.update_gui()
