import tkinter as tk

from Constants import SIZE_OF_BOARD
from UltimateTicTacToe import UltimateTicTacToe
from TKLayoutBuilder import TKLayoutBuilder


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ultimate_ttt = UltimateTicTacToe()
        self.current_player = "O"

        self.title("Ultimate Tic Tac Toe")
        TKLayoutBuilder(self).build(self.ultimate_ttt, self.on_click)

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def on_click(self, u_position, ttt_position, button):
        
        i, j = u_position
        k, h = ttt_position

        ttt = self.ultimate_ttt.childs[i][j]
        ttt.childs[k][h].set_value(self.current_player)
        button.config(text=self.current_player)

        self.switch_player()
