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
        menu.add_command(label="Restart", command=lambda: print("Restart"))
        menu.add_command(label="Exit", command=self._root.quit)
        self._root.config(menu=menu)

        self._player_status = tk.Frame(self._root)
        self._player_status.grid(row=0, column=0)

        img = Image.open("src/imgs/player_image.png")
        img = img.resize((300, 300))

        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self._player_status, image=photo)
        label.grid(row=0, column=0)
        label.config(bg="white")

        label = tk.Label(self._player_status, image=photo)
        label.grid(row=1, column=0)
        label.config(bg="white")

        self._board_frame = tk.Frame(self._root, bg='white')
        self._board_frame.grid(row=0, column=1, padx=50, pady=50)

        for i, line in enumerate(self._ultimate_ttt.get_childs()):
            for j, tic_tac_toe in enumerate(line):

                def changeBg(event, frame, color):
                    frame.config(bg=color)

                big_frame = tk.Frame(self._board_frame, bg='white')
                big_frame.grid(row=i, column=j)

                frame = tk.Frame(big_frame, bg='white')
                frame.grid(row=0, column=0, padx=4, pady=4)

                frame.bind("<Enter>", partial(changeBg, frame=frame, color="gray"))
                frame.bind("<Leave>", partial(changeBg, frame=frame, color="white"))

                for k, line in enumerate(tic_tac_toe.get_childs()):
                    for h, position in enumerate(line):
                        button = tk.Button(frame, text=position.get_value(), font=('Arial', 20), height=2, width=4,
                                           bg='white', fg='gray',)
                        button.config(command=partial(self.put_marker, Coordinate(j, i), Coordinate(h, k), button))
                        button.grid(row=k, column=h, sticky='nsew', padx=1, pady=1)
    
        self._root.mainloop()

    def put_marker(self, u_position, ttt_position, button):
        symbol = self._round_manager.get_current_player().get_symbol()

        if self._round_manager.put_marker(u_position, ttt_position):
            button.config(text=symbol)
