import tkinter as tk

from functools import partial
from tkinter import simpledialog, messagebox

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from dog.start_status import StartStatus

from utils.Constants import SIZE_OF_BOARD
from utils.Coordinate import Coordinate

from view.PlayerStatusFrame import PlayerStatusFrame

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
        
        self._root = tk.Tk()
        self._root.title("Ultimate Tic Tac Toe")
        self._root.config(bg="white")

        self._player_frame = None
        self._board_frame = None
        
        self._local_player_frame = None
        self._remote_player_frame = None

        self._buttons = None
        self._frames = None

        self.fill_main_window()

        self.connect_to_dog()
    
    def get_ultimate_tic_tac_toe(self):
        return self._ultimate_ttt
    
    def get_local_player(self):
        return self._local_player
    
    def get_remote_player(self):
        return self._remote_player

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

    def build_menu(self):
        menu = tk.Menu(self._root)
        menu.add_command(label="Start match", command=self.start_match)
        menu.add_command(label="Reset", command=self.reset_game)
        menu.add_command(label="Quit", command=self.quit)
        self._root.config(menu=menu)

    def build_player_status(self):
        self._player_frame: tk.Frame = tk.Frame(self._root)
        self._player_frame.grid(row=0, column=0)

        self._local_player_frame = PlayerStatusFrame(self._player_frame, "Jogador local", "imgs/player_image.png", bg="white")
        self._local_player_frame.grid(column=0, row=0)

        self._remote_player_frame = PlayerStatusFrame(self._player_frame, "Jogador remoto", "imgs/player_image.png", bg="white")
        self._remote_player_frame.grid(column=0, row=1)
    
    def build_board(self, parent, board, level=1):
        buttons = []
        frames = []

        if board.get_childs():
            big_frame = tk.Frame(parent, bg='black')
            big_frame.grid(row=0, column=0, padx=10, pady=10)

            def change_bg(_, frame, color):
                # Gambiarra para não trocar a cor de fundo quando alguém vence ou empata
                if frame.cget('bg') in ("#dcdcdc", "white"):
                    frame.config(bg=color)

            for i in range(3):
                buttons_line = []
                frames_line = []
                for j in range(3):
                    frame = tk.Frame(big_frame, bg='white')
                    frame.grid(row=i, column=j)
                    frame.bind("<Enter>", partial(change_bg, frame=frame, color="#dcdcdc"))
                    frame.bind("<Leave>", partial(change_bg, frame=frame, color="white"))

                    button_or_buttons = self.build_board(frame, board.get_childs()[i][j], level + 1)
                    
                    buttons_line.append(button_or_buttons)
                    frames_line.append(frame)

                buttons.append(buttons_line)
                frames.append(frames_line)

            frames[0][0].grid_configure(padx=(0, 2), pady=(0, 2))
            frames[0][2].grid_configure(padx=(2, 0), pady=(0, 2))
            frames[2][0].grid_configure(padx=(0, 2), pady=(2, 0))
            frames[2][2].grid_configure(padx=(2, 0), pady=(2, 0))

            frames[1][1].grid_configure(padx=(2, 2), pady=(2, 2))

            frames[0][1].grid_configure(padx=(2, 2), pady=(0, 2))
            frames[1][0].grid_configure(padx=(0, 2), pady=(2, 2))
            frames[1][2].grid_configure(padx=(2, 0), pady=(2, 2))
            frames[2][1].grid_configure(padx=(2, 2), pady=(2, 0))

            if level == 1:
                self._frames = frames

            return buttons

        button = tk.Button(parent, text=board.get_value(), font=('Arial', 20), height=2, width=4,
                            bg='white', fg='black', relief='flat', bd=0, highlightthickness=0)
        button.grid(row=0, column=0)
        return button

    def add_command_to_buttons(self, buttons):
        coordinates = []

        for x in range(SIZE_OF_BOARD):
            for y in range(SIZE_OF_BOARD):
                coordinates.append(Coordinate(x, y))
        
        for u_ttt in coordinates:
            u_ttt_x = u_ttt.get_x()
            u_ttt_y = u_ttt.get_y()

            for ttt in coordinates:
                ttt_x = ttt.get_x()
                ttt_y = ttt.get_y()
                buttons[u_ttt_y][u_ttt_x][ttt_y][ttt_x].config(command=partial(self.on_click_board, u_ttt, ttt))

    def build_ultimate_tic_tac_toe(self):
        self._board_frame: tk.Frame = tk.Frame(self._root, bg='white')
        self._board_frame.grid(row=0, column=1, padx=50, pady=50)
        self._buttons = self.build_board(self._board_frame, self._ultimate_ttt)
        self.add_command_to_buttons(self._buttons)

    def fill_main_window(self):
        self.build_menu()
        self.build_player_status()
        self.build_ultimate_tic_tac_toe()

    def update_gui(self) -> None:
        """
        Atualiza o estado da GUI após processamento da lógica do jogo
        """
        coordinates = []

        for x in range(SIZE_OF_BOARD):
            for y in range(SIZE_OF_BOARD):
                coordinates.append(Coordinate(x, y))
        
        for i in range(0, 9):
            u_x = coordinates[i].get_x()
            u_y = coordinates[i].get_y()

            for j in range(0, 9):
                ttt_x = coordinates[j].get_x()
                ttt_y = coordinates[j].get_y()

                tic_tac_toes = self._ultimate_ttt.get_childs()
                tic_tac_toe = tic_tac_toes[u_y][u_x]

                winner = tic_tac_toe.get_value()

                if winner == "X":
                    self._frames[u_y][u_x].config(bg="red")
                elif winner == "O":
                    self._frames[u_y][u_x].config(bg="blue")
                elif winner == "-":
                    self._frames[u_y][u_x].config(bg="gray")
                else:  # Corrige a cor quando se reseta o jogo?
                    self._frames[u_y][u_x].config(bg="white")

                positions = tic_tac_toe.get_childs()
                position = positions[ttt_y][ttt_x]

                symbol = position.get_value()
                
                if symbol is None:
                    symbol = ""
                
                button = self._buttons[u_y][u_x][ttt_y][ttt_x]
                if symbol == "X":
                    button.config(text=symbol, fg="red")
                elif symbol == "O":
                    button.config(text=symbol, fg="blue")
                elif symbol == "-":
                    button.config(text=symbol, fg="gray")
                else:
                    button.config(text=symbol, fg="black")

        if self._local_player.get_is_turn():
            self._local_player_frame.set_playing()
            self._remote_player_frame.set_waiting()
        elif self._remote_player.get_is_turn():
            self._remote_player_frame.set_playing()
            self._local_player_frame.set_waiting()
        else:
            self._remote_player_frame.set_waiting()
            self._local_player_frame.set_waiting()

        # Gambiarra para atualizar sempre o nome do jogador caso termine a partida
        local_player_name = self._local_player.get_name()
        remote_player_name = self._remote_player.get_name()
        self._local_player_frame.set_player_name(local_player_name)
        self._remote_player_frame.set_player_name(remote_player_name)

    def connect_to_dog(self):
        player_name = simpledialog.askstring(title="Player identifcation", prompt="Qual o seu nome?")
        message = self._dog_server.initialize(player_name, self)
        messagebox.showinfo(message=message)

        self._local_player.set_name(player_name)
        self.update_gui()

    def reset_game(self):
        print("reset chamado")
        self._round_manager.reset_game()
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
