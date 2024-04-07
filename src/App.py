import tkinter as tk
from PIL import Image, ImageTk

from functools import partial

from Constants import SIZE_OF_BOARD
from UltimateTicTacToe import UltimateTicTacToe


class App:
    def __init__(self):
        self.ultimate_ttt = UltimateTicTacToe()
        self.current_player = "O"

        self.root = tk.Tk()
        self.root.title("Ultimate Tic Tac Toe")
        self.root.config(bg="white")

        self.player_status = tk.Frame(self.root)
        self.player_status.grid(row=0, column=0)

        img = Image.open("src/imgs/player_image.png")
        img = img.resize((300, 300))

        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self.player_status, image=photo)
        label.grid(row=0, column=0)
        label.config(bg="white")

        label = tk.Label(self.player_status, image=photo)
        label.grid(row=1, column=0)
        label.config(bg="white")

        self.board_frame = tk.Frame(self.root, bg='white')
        self.board_frame.grid(row=0, column=1, padx=50, pady=50)

        for i, line in enumerate(self.ultimate_ttt.childs):
            for j, tic_tac_toe in enumerate(line):
                x0, y0 = j * 4, i * 4

                def changeBg(event, frame, color):
                    frame.config(bg=color)

                big_frame = tk.Frame(self.board_frame, bg='white')
                big_frame.grid(row=i, column=j)

                frame = tk.Frame(big_frame, bg='white')
                frame.grid(row=0, column=0, padx=4, pady=4)

                frame.bind("<Enter>", partial(changeBg, frame=frame, color="gray"))
                frame.bind("<Leave>", partial(changeBg, frame=frame, color="white"))

                for k, line in enumerate(tic_tac_toe.childs):
                    for h, position in enumerate(line):
                        button = tk.Button(frame, text=position.get_value(), font=('Arial', 20), height=2, width=4,
                                           bg='white', fg='gray',)
                        button.config(command=partial(self.on_click, (i, j), (k, h), button))
                        button.grid(row=k + y0, column=h + x0, sticky='nsew', padx=1, pady=1)
    
        self.root.mainloop()

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def on_click(self, u_position, ttt_position, button):
        
        i, j = u_position
        k, h = ttt_position

        ttt = self.ultimate_ttt.childs[i][j]
        ttt.childs[k][h].set_value(self.current_player)
        button.config(text=self.current_player)

        self.switch_player()
