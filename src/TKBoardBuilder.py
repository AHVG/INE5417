import tkinter as tk

from functools import partial

from IBoardBuilder import IBoardBuilder


class TKBoardBuilder(IBoardBuilder):

    def __init__(self, root) -> None:
        self.root = root


    def build(self, tic_tac_toe, x0, y0, callback):
        board = tic_tac_toe.board

        for i, line in enumerate(board):
            for j, position in enumerate(line):
                button = tk.Button(self.root, text=position.get_value(), font=('Arial', 20), height=2, width=4)
                button.config(command=partial(callback, i, j, button))
                button.grid(row=i + y0, column=j + x0)
