import tkinter as tk

from functools import partial

from IBoardBuilder import IBoardBuilder


class TKBoardBuilder(IBoardBuilder):

    def __init__(self, root) -> None:
        self.root = root


    def build(self, ultimate_tic_tac_toe, callback):
        for i, line in enumerate(ultimate_tic_tac_toe.board):
            for j, tic_tac_toe in enumerate(line):
                x0, y0 = j * 4, i * 4

                for k, line in enumerate(tic_tac_toe.board):
                    for h, position in enumerate(line):
                        button = tk.Button(self.root, text=position.get_value(), font=('Arial', 20), height=2, width=4)
                        button.config(command=partial(callback, (i, j), (k, h), button))
                        button.grid(row=k + y0, column=h + x0)
