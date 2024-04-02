import tkinter as tk

from functools import partial

from ILayoutBuilder import ILayoutBuilder


class TKLayoutBuilder(ILayoutBuilder):

    def __init__(self, root) -> None:
        self.root = root

    def build(self, ultimate_tic_tac_toe, callback):
        for i, line in enumerate(ultimate_tic_tac_toe.childs):
            for j, tic_tac_toe in enumerate(line):
                x0, y0 = j * 4, i * 4

                def changeBg(event, frame, color):
                    frame.config(bg=color)

                big_frame = tk.Frame(self.root, bg='white')
                big_frame.grid(row=i, column=j, padx=4, pady=4)
                frame = tk.Frame(big_frame, bg='white')
                frame.grid(row=0, column=0, padx=4, pady=4)

                frame.bind("<Enter>", partial(changeBg, frame=frame, color="gray"))
                frame.bind("<Leave>", partial(changeBg, frame=frame, color="white"))

                for k, line in enumerate(tic_tac_toe.childs):
                    for h, position in enumerate(line):
                        button = tk.Button(frame, text=position.get_value(), font=('Arial', 20), height=2, width=4,
                                           bg='white', fg='gray',)
                        button.config(command=partial(callback, (i, j), (k, h), button))
                        button.grid(row=k + y0, column=h + x0, sticky='nsew', padx=2, pady=2)