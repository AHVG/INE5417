import tkinter as tk

from Constants import SIZE_OF_BOARD
from UltimateTicTacToe import UltimateTicTacToe
from TKLayoutBuilder import TKLayoutBuilder
from PlayManager import PlayManager


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ultimate_ttt = UltimateTicTacToe()
        self.play_manager = PlayManager(self.ultimate_ttt)

        self.title("Ultimate Tic Tac Toe")
        self.initialize_board()

    def initialize_board(self):
        TKLayoutBuilder(self).build(self.ultimate_ttt, self.on_click)

    def on_click(self, u_position, ttt_position, button):

        if not self.play_manager.play_allowed(u_position, ttt_position):
            return
        
        i, j = u_position
        k, h = ttt_position

        ttt = self.ultimate_ttt.childs[i][j]
        ttt.childs[k][h].set_value(self.play_manager.current_player)
        button.config(text=self.play_manager.current_player)

        if ttt.check():
            if self.ultimate_ttt.check():
                print(f"Player {self.play_manager.current_player} won")

        window = button.master.master.master

        for frame in window.winfo_children():
            frame.config(bg="white")

        next_frame = window.winfo_children()[k * SIZE_OF_BOARD + h]
        next_frame.config(bg="gray")

        self.play_manager.set_last_play(ttt_position)
        self.play_manager.switch_player()