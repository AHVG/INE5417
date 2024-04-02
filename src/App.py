import tkinter as tk

from UltimateTicTacToe import UltimateTicTacToe
from TKLayoutBuilder import TKLayoutBuilder
from PlayManager import PlayManager
from WinnerChecker import WinnerChecker


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ultimate_ttt = UltimateTicTacToe()
        self.play_manager = PlayManager(self.ultimate_ttt)
        self.winner_checker = WinnerChecker()

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

        if self.winner_checker.check(ttt):
            if self.winner_checker.check(self.ultimate_ttt):
                print(f"Player {self.play_manager.current_player} won")
        
        # TODO: Arrumar gambiarra
        if self.ultimate_ttt.childs[k][h].get_value():
            self.play_manager.last_play = None
        else:
            self.play_manager.last_play = (k, h)

        self.play_manager.switch_player()