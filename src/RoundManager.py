

class RoundManager:
    
    def __init__(self, ultimate_tic_tac_toe, local_player, remote_player):
        self._ultimate_tic_tac_toe = ultimate_tic_tac_toe
        self._local_player = local_player
        self._remote_player = remote_player
        self._current_player = local_player

    def get_ultimate_tic_tac_toe(self):
        return self._ultimate_tic_tac_toe
    
    def set_ultimate_tic_tac_toe(self, new_ultimate_tic_tac_toe):
        self._ultimate_tic_tac_toe = new_ultimate_tic_tac_toe

    def get_local_player(self):
        return self._local_player
    
    def set_local_player(self, new_local_player):
        self._local_player = new_local_player

    def get_remote_player(self):
        return self._remote_player
    
    def set_remote_player(self, new_remote_player):
        self._remote_player = new_remote_player

    def get_current_player(self):
        return self._current_player
    
    def set_current_player(self, new_current_player):
        self._current_player = new_current_player

    def switch_player(self):
        self._current_player = self._remote_player if self._current_player.get_symbol() == self._local_player.get_symbol() else self._local_player

    def put_marker(self, u_position, ttt_position):

        # Verificar se é válido

        # Atualizando o tabuleiro
        ttt = self._ultimate_tic_tac_toe.get_childs()[u_position.get_y()][u_position.get_x()]
        ttt.get_childs()[ttt_position.get_y()][ttt_position.get_x()].set_value(self._current_player.get_symbol())
        
        # Verificar vencedor
        if self._ultimate_tic_tac_toe.check():
            print("vencedor")
        else:
            print("sem vencedor")

        self.switch_player()

        return True
