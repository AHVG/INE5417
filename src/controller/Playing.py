from utils.Coordinate import Coordinate

from controller.State import State


class Playing(State):
    
    def receive_move(self):
        pass
    
    def receive_withdrawal_notification(self):
        self._round_manager.switch_state("GameOver")

    def put_marker(self, u_position: Coordinate, ttt_position: Coordinate) -> bool:
        """
        Coloca marcador se for uma casa válida (se está vazia e se está de acordo com o movimento anterior)

        Args:
            u_position (Coordinate): Coordenada no tabuleiro maior (referencia um tabuleiro menor)
            ttt_position (Coordinate): Coordenada no tabuleiro menor

        Returns:
            bool: Se houve colocação de marcador retorna True; do contrário False
        """
        # Verificar se é válido

        # Atualizando o tabuleiro
        ttt = self._round_manager.get_ultimate_tic_tac_toe().get_childs()[u_position.get_y()][u_position.get_x()]
        ttt.get_childs()[ttt_position.get_y()][ttt_position.get_x()].set_value(self._round_manager.get_current_player().get_symbol())
        
        # Verificar vencedor
        if self._round_manager.get_ultimate_tic_tac_toe().check():
            print("vencedor")
        else:
            print("sem vencedor")

        self._round_manager.switch_player()

        return True