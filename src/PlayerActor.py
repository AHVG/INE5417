import tkinter as tk

from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from functools import partial

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from dog.start_status import StartStatus

from UltimateTicTacToe import UltimateTicTacToe
from RoundManager import RoundManager
from Coordinate import Coordinate
from Player import Player
from Board import Board

from Constants import SIZE_OF_BOARD


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
        self._local_player: Player = Player("123", "X")
        self._remote_player: Player = Player("312", "O")
        self._round_manager: RoundManager = RoundManager(self._ultimate_ttt, self._local_player, self._remote_player)

        self._root: tk.Tk = tk.Tk()
        self._root.title("Ultimate Tic Tac Toe")
        self._root.config(bg="white")

        menu = tk.Menu(self._root)
        menu.add_command(label="Start match", command=lambda: self.start_match)
        menu.add_command(label="Reset", command=lambda: print("Reset"))
        menu.add_command(label="Exit", command=self._root.quit)
        self._root.config(menu=menu)

        self._player_status: tk.Frame = tk.Frame(self._root)
        self._player_status.grid(row=0, column=0)

        self.load_imgs()

        label = tk.Label(self._player_status, image=self._player_img)
        label.grid(row=0, column=0)
        label.config(bg="white")

        label = tk.Label(self._player_status, image=self._player_img)
        label.grid(row=1, column=0)
        label.config(bg="white")

        self._board_frame: tk.Frame = tk.Frame(self._root, bg='white')
        self._board_frame.grid(row=0, column=1, padx=50, pady=50)

        def build_board(tic_tac_toe, frame) -> list[list[tk.Button]]:
            buttons = []

            for k, line in enumerate(tic_tac_toe.get_childs()):
                buttons_line = []

                for h, position in enumerate(line):
                    button = tk.Button(frame, text=position.get_value(), font=('Arial', 20), height=2, width=4,
                                        bg='white', fg='gray', command=partial(self.on_click_board, Coordinate(j, i), Coordinate(h, k)))
                    button.grid(row=k, column=h, sticky='nsew', padx=1, pady=1)
                    buttons_line.append(button)

                buttons.append(buttons_line)

            return buttons

        self._buttons: list[list[list[list[tk.Button]]]] = []

        for i, line in enumerate(self._ultimate_ttt.get_childs()):
            buttons_line = []

            for j, tic_tac_toe in enumerate(line):

                def changeBg(event, frame, color):
                    frame.config(bg=color)

                big_frame = tk.Frame(self._board_frame, bg='white', name=f'{i}x{j}')
                big_frame.grid(row=i, column=j)

                frame = tk.Frame(big_frame, bg='white')
                frame.grid(row=0, column=0, padx=4, pady=4)

                frame.bind("<Enter>", partial(changeBg, frame=frame, color="gray"))
                frame.bind("<Leave>", partial(changeBg, frame=frame, color="white"))

                buttons_line.append(build_board(tic_tac_toe, frame))
            
            self._buttons.append(buttons_line)

        # Assegura que todos os tamanhos estão corretos
        self._root.update()

        # Se conectando ao dog serve
        player_name = simpledialog.askstring(title="Player identifcation", prompt="Qual o seu nome?")
        self._dog_server: DogActor = DogActor()
        message = self._dog_server.initialize(player_name, self)
        messagebox.showinfo(message=message)
    
        self._root.mainloop()

    def load_img(self, path: str, size: tuple = None) -> Image:
        try:
            img = Image.open(path)
            if size:
                img = img.resize(size)

            return img
        except:
            return None            

    def load_imgs(self) -> None:
        """
        Carrega as imagens para serem renderizadas quando necessário
        """
        self._player_img: ImageTk.PhotoImage = ImageTk.PhotoImage(self.load_img("imgs/player_image.png", (300, 300)))
        self._red_x_bg_white: ImageTk.PhotoImage = ImageTk.PhotoImage(self.load_img("imgs/red_x_bg_white.png", (278, 242)))
        self._blue_o_bg_white: ImageTk.PhotoImage = ImageTk.PhotoImage(self.load_img("imgs/blue_o_bg_white.png", (278, 242)))

    def update_gui(self) -> None:
        """
        Atualiza o estado da GUI após processamento da lógica do jogo
        """
        coordinates = [Coordinate(x, y) for x in range(SIZE_OF_BOARD) for y in range(SIZE_OF_BOARD)]
        
        for u_coordinate in coordinates:
            u_x, u_y = u_coordinate.get_x(), u_coordinate.get_y()
            if self._ultimate_ttt.get_childs()[u_y][u_x].get_value():
                width = self._board_frame.children[f"{u_y}x{u_x}"].winfo_width()
                height = self._board_frame.children[f"{u_y}x{u_x}"].winfo_height()

                if self._ultimate_ttt.get_childs()[u_y][u_x].get_value() == "X":
                    label = tk.Label(self._board_frame.children[f"{u_y}x{u_x}"], image=self._red_x_bg_white, width=width, height=height)
                else:
                    label = tk.Label(self._board_frame.children[f"{u_y}x{u_x}"], image=self._blue_o_bg_white, width=width, height=height)

                label.place(relx=0.5, rely=0.5, anchor='center')
            else:
                for ttt_coordinate in coordinates:
                    ttt_x, ttt_y = ttt_coordinate.get_x(), ttt_coordinate.get_y()
                    symbol = self._ultimate_ttt.get_childs()[u_y][u_x].get_childs()[ttt_y][ttt_x].get_value()
                    self._buttons[u_y][u_x][ttt_y][ttt_x].config(text=symbol)

    def start_match(self) -> None:
        start_status = self._dog_server.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_start(self, start_status: StartStatus) -> None:
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_move(self, a_move: dict[str, str]) -> None:
        print("O método receive_move() precisa ser sobrescrito")

    def receive_withdrawal_notification(self) -> None:
        print("O método receive_withdrawal_notification() precisa ser sobrescrito")

    def on_click_board(self, u_position: Coordinate, ttt_position: Coordinate) -> None:
        """
        Lida com o click do usuário no tabuleiro
        
        Args:
            u_position (Coordinate): Coordenada no tabuleiro maior (Ultimate)
            ttt_position (Coordinate): Coordenada no tabuleiro menor (Tic Tac Toe)
        """
        self._round_manager.put_marker(u_position, ttt_position)
        self.update_gui()
