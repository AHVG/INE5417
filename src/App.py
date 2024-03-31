import tkinter as tk

from Board import Board
from TKBoardBuilder import TKBoardBuilder
from PlayManager import PlayManager

# TODO: desacoplar lógica de criação de layout desta classe
# TODO: Colocar todos atributos como protegido


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ultimate_ttt = Board(Board)
        self.play_manager = PlayManager(self.ultimate_ttt)

        self.title("Ultimate Tic Tac Toe")
        self.initialize_board()


    def initialize_board(self):
        TKBoardBuilder(self).build(self.ultimate_ttt, self.on_click)


    # TODO: tirar isso daqui
    def on_click(self, u_position, ttt_position, button):

        if not self.play_manager.play_allowed(u_position, ttt_position):
            return
        
        i, j = u_position
        k, h = ttt_position

        ttt = self.ultimate_ttt.board[i][j]
        ttt.board[k][h].set_value(self.play_manager.current_player)
        button.config(text=self.play_manager.current_player)

        self.play_manager.last_play = ttt_position

        if ttt.check_winner():
            if self.ultimate_ttt.check_winner():
                print(f"Player {self.play_manager.current_player} won", self.play_manager.current_player)

        self.play_manager.switch_player()