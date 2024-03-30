import tkinter as tk

from TicTacToe import TicTacToe


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tic_tac_toe = TicTacToe()
        self.current_player = 'X'
        self.title("Ultimate Tic Tac Toe")
        self.initialize_board()


    def initialize_board(self):
        for i, line in enumerate(self.tic_tac_toe.board):
            for j, element in enumerate(line):
                button = tk.Button(self, text=element, font=('Arial', 20), height=2, width=4,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.tic_tac_toe.board[i][j] = button


    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"


    def on_click(self, i, j):
        self.tic_tac_toe.board[i][j]['text'] = self.current_player
        self.switch_player()