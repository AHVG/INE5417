import tkinter as tk

from PIL import Image, ImageTk
from functools import partial

from utils.Coordinate import Coordinate


class UIBuilder:

    def __init__(self, player_actor) -> None:
        self._root = tk.Tk()
        self._root.title("Ultimate Tic Tac Toe")
        self._root.config(bg="white")
        self._player_actor = player_actor

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

    def get_player_img(self):
        return self._player_img
    
    def get_red_x_bg_white(self):
        return self._red_x_bg_white
    
    def get_blue_o_bg_white(self):
        return self._blue_o_bg_white

    def get_buttons(self):
        return self._buttons

    def get_player_status(self):
        return self._player_status

    def get_board_frame(self):
        return self._board_frame

    def get_root(self):
        return self._root

    def build_menu(self):
        menu = tk.Menu(self._root)
        menu.add_command(label="Start match", command=lambda: self._player_actor.start_match)
        menu.add_command(label="Reset", command=lambda: self._player_actor.reset)
        menu.add_command(label="Exit", command=self._root.quit)
        self._root.config(menu=menu)

    def build_player_status(self):
        self._player_status: tk.Frame = tk.Frame(self._root)
        self._player_status.grid(row=0, column=0)

        self.load_imgs()

        label = tk.Label(self._player_status, image=self._player_img)
        label.grid(row=0, column=0)
        label.config(bg="white")

        label = tk.Label(self._player_status, image=self._player_img)
        label.grid(row=1, column=0)
        label.config(bg="white")

    def build_board(self):
        self._board_frame: tk.Frame = tk.Frame(self._root, bg='white')
        self._board_frame.grid(row=0, column=1, padx=50, pady=50)

        def build_tic_tac_toe(tic_tac_toe, frame) -> list[list[tk.Button]]:
            buttons = []

            for k, line in enumerate(tic_tac_toe.get_childs()):
                buttons_line = []

                for h, position in enumerate(line):
                    button = tk.Button(frame, text=position.get_value(), font=('Arial', 20), height=2, width=4,
                                        bg='white', fg='gray', command=partial(self._player_actor.on_click_board, Coordinate(j, i), Coordinate(h, k)))
                    button.grid(row=k, column=h, sticky='nsew', padx=1, pady=1)
                    buttons_line.append(button)

                buttons.append(buttons_line)

            return buttons
    
        self._buttons: list[list[list[list[tk.Button]]]] = []

        for i, line in enumerate(self._player_actor._ultimate_ttt.get_childs()):
            buttons_line = []

            for j, tic_tac_toe in enumerate(line):

                def change_bg(event, frame, color):
                    frame.config(bg=color)

                big_frame = tk.Frame(self._board_frame, bg='white', name=f'{i}x{j}')
                big_frame.grid(row=i, column=j)

                frame = tk.Frame(big_frame, bg='white')
                frame.grid(row=0, column=0, padx=4, pady=4)

                frame.bind("<Enter>", partial(change_bg, frame=frame, color="gray"))
                frame.bind("<Leave>", partial(change_bg, frame=frame, color="white"))

                buttons_line.append(build_tic_tac_toe(tic_tac_toe, frame))
            
            self._buttons.append(buttons_line)
