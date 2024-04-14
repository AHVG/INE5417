import tkinter as tk

from PIL import Image, ImageTk
from functools import partial

from UltimateTicTacToe import UltimateTicTacToe
from Player import Player
from RoundManager import RoundManager
from Coordinate import Coordinate


class App:
    def __init__(self):
        self._ultimate_ttt = UltimateTicTacToe()
        self._local_player = Player("123", "X")
        self._remote_player = Player("312", "O")
        self._round_manager = RoundManager(self._ultimate_ttt, self._local_player, self._remote_player)

        self._root = tk.Tk()
        self._root.title("Ultimate Tic Tac Toe")
        self._root.config(bg="white")

        # Adicionanod barra de menu
        # drop down?
        menu = tk.Menu(self._root)
        menu.add_command(label="Start match", command=lambda: print("Start match"))
        menu.add_command(label="Reset", command=lambda: print("Reset"))
        menu.add_command(label="Exit", command=self._root.quit)
        self._root.config(menu=menu)

        self._player_status = tk.Frame(self._root)
        self._player_status.grid(row=0, column=0)

        self.load_imgs()

        label = tk.Label(self._player_status, image=self.player_img)
        label.grid(row=0, column=0)
        label.config(bg="white")

        label = tk.Label(self._player_status, image=self.player_img)
        label.grid(row=1, column=0)
        label.config(bg="white")

        self._board_frame = tk.Frame(self._root, bg='white')
        self._board_frame.grid(row=0, column=1, padx=50, pady=50)

        def build_board(tic_tac_toe, frame):
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

        self.buttons = []

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
            
            self.buttons.append(buttons_line)

        # Assegura que todos os tamanhos estão corretos
        self._root.update()
    
        self._root.mainloop()

    def load_img(self, path, size=None):
        try:
            img = Image.open(path)
            if size:
                img = img.resize(size)

            return img
        except:
            return None            

    def load_imgs(self):

        self.player_img = ImageTk.PhotoImage(self.load_img("src/imgs/player_image.png", (300, 300)))
        self.red_x_bg_white = ImageTk.PhotoImage(self.load_img("src/imgs/red_x_bg_white.png", (278, 242)))
        self.blue_o_bg_white = ImageTk.PhotoImage(self.load_img("src/imgs/blue_o_bg_white.png", (278, 242)))

    def update_gui(self):
        coordinates = [Coordinate(x, y) for x in range(3) for y in range(3)]
        
        for u_coordinate in coordinates:
            u_x, u_y = u_coordinate.get_x(), u_coordinate.get_y()
            if self._ultimate_ttt.get_childs()[u_y][u_x].get_value():
                width = self._board_frame.children[f"{u_y}x{u_x}"].winfo_width()
                height = self._board_frame.children[f"{u_y}x{u_x}"].winfo_height()

                if self._ultimate_ttt.get_childs()[u_y][u_x].get_value() == "X":
                    label = tk.Label(self._board_frame.children[f"{u_y}x{u_x}"], image=self.red_x_bg_white, width=width, height=height)
                else:
                    label = tk.Label(self._board_frame.children[f"{u_y}x{u_x}"], image=self.blue_o_bg_white, width=width, height=height)

                label.place(relx=0.5, rely=0.5, anchor='center')
            else:
                for ttt_coordinate in coordinates:
                    ttt_x, ttt_y = ttt_coordinate.get_x(), ttt_coordinate.get_y()
                    symbol = self._ultimate_ttt.get_childs()[u_y][u_x].get_childs()[ttt_y][ttt_x].get_value()
                    self.buttons[u_y][u_x][ttt_y][ttt_x].config(text=symbol)

    def receive_move(self, a_move):
        u_position, ttt_position = Coordinate(a_move["move_u"]), Coordinate(a_move["move_ttt"])
        self._round_manager.put_marker(u_position, ttt_position)
        self.update_gui()

    def on_click_board(self, u_position, ttt_position):
        self._round_manager.put_marker(u_position, ttt_position)
        self.update_gui()
