import tkinter as tk
from tkinter import simpledialog, messagebox

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from Constants import SIZE_OF_BOARD
from UltimateTicTacToe import UltimateTicTacToe
from TKLayoutBuilder import TKLayoutBuilder
from PlayManager import PlayManager


class App(tk.Tk, DogPlayerInterface):
    def __init__(self):
        super().__init__()
        self.ultimate_ttt = UltimateTicTacToe()
        self.play_manager = PlayManager(self.ultimate_ttt)

        self.title("Ultimate Tic Tac Toe")
        self.initialize_board()

        # Adicionanod barra de menu
        # drop down?
        menu = tk.Menu(self)
        menu.add_command(label="iniciar jogo", command=self.start_match)
        menu.add_command(label="restaurar estado inicial", command=lambda: print("restaurando estado inicial"))
        self.config(menu=menu)

        # Se conectando ao dog serve
        player_name = simpledialog.askstring(title="Player identifcation", prompt="Qual o seu nome?")
        self.dog_server = DogActor()
        message = self.dog_server.initialize(player_name, self)
        messagebox.showinfo(message=message)

    def initialize_board(self):
        TKLayoutBuilder(self).build(self.ultimate_ttt, self.on_click)

    def start_match(self):
        start_status = self.dog_server.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_move(self, a_move):
        print("O método receive_move() precisa ser sobrescrito")

    def receive_withdrawal_notification(self):
        print("O método receive_withdrawal_notification() precisa ser sobrescrito")

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