import tkinter as tk

from PIL import Image, ImageTk
    

class PlayerStatusFrame(tk.Frame):
    def __init__(self, parent, player_name, player_image_path, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.player_image_path = player_image_path
        self.player_image = Image.open(self.player_image_path)
        self.player_image = self.player_image.resize((300, 300))
        self.player_photo = ImageTk.PhotoImage(self.player_image)

        # Criar e posicionar elementos no frame
        self.label_player_image = tk.Label(self, image=self.player_photo, bg="white")
        self.label_player_image.grid(column=0, row=0)

        self.label_player_name = tk.Label(self, text=player_name, bg="white")
        self.label_player_name.grid(column=0, row=1)

        self.config(highlightbackground="white", highlightthickness=2)

    def get_player_name(self):
        return self.label_player_name.cget("text")

    def set_player_name(self, new_name):
        self.label_player_name.config(text=new_name)

    def set_waiting(self):
        # Adiciona uma borda ao redor do frame
        self.config(highlightbackground="white", highlightthickness=2)

    def set_playing(self):
        # Remove a borda do frame
        self.config(highlightbackground="black", highlightthickness=2)
