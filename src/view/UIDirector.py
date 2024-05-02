

class UIDirector:

    def __init__(self, ui_builder) -> None:
        self._ui_builder = ui_builder

    def build(self):
        self._ui_builder.build_menu()
        self._ui_builder.build_player_status()
        self._ui_builder.build_board()
        self._ui_builder.get_root().update()  # Assegura que todos os tamanhos estão corretos

    def get_player_img(self):
        return self._ui_builder.get_player_img()
    
    def get_red_x_bg_white(self):
        return self._ui_builder.get_red_x_bg_white()
    
    def get_blue_o_bg_white(self):
        return self._ui_builder.get_blue_o_bg_white()

    def get_buttons(self):
        return self._ui_builder.get_buttons()

    def get_player_status(self):
        return self._ui_builder.get_player_status()

    def get_board_frame(self):
        return self._ui_builder.get_board_frame()

    def get_root(self):
        return self._ui_builder.get_root()
    