import tkinter as tk

from functools import partial

from UltimateTicTacToe import UltimateTicTacToe
from TKBoardBuilder import TKBoardBuilder


# TODO: desacoplar lógica de criação de layout desta classe


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ultimate_tic_tac_toe = UltimateTicTacToe()
        self.current_player = 'X'
        self.title("Ultimate Tic Tac Toe")
        self.initialize_board()


    def initialize_board(self):
        for i, line in enumerate(self.ultimate_tic_tac_toe.board):
            for j, tic_tac_toe in enumerate(line):
                TKBoardBuilder(self).build(tic_tac_toe, j * 4, i * 4, partial(self.on_click, tic_tac_toe))


    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"


    def on_click(self, tic_tac_toe, i, j, button):
        tic_tac_toe.board[i][j].set_value(self.current_player)
        button.config(text=self.current_player)

        if tic_tac_toe.check_winner():
            print(f"Player {self.current_player} won", self.current_player)

        self.switch_player()