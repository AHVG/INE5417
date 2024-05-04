from utils.Coordinate import Coordinate

from controller.State import State


class Waiting(State):

    def receive_move(self, a_move):
        print(a_move)
        u_position = Coordinate(a_move["u"][0], a_move["u"][1])
        ttt_position = Coordinate(a_move["ttt"][0], a_move["ttt"][1])
        # Verificar se é válido

        # Atualizando o tabuleiro
        ttt = self._round_manager.get_ultimate_tic_tac_toe().get_childs()[u_position.get_y()][u_position.get_x()]
        ttt.get_childs()[ttt_position.get_y()][ttt_position.get_x()].set_value(self._round_manager.get_current_player().get_symbol())
        
        # Verificar vencedor
        if self._round_manager.get_ultimate_tic_tac_toe().check():
            self._round_manager.switch_state("GameOver")
            print("vencedor")
            return True
        
        print("sem vencedor")
        self._round_manager.switch_state("Playing")
        self._round_manager.switch_player()

        return True
    
    def receive_withdrawal_notification(self):
        self._round_manager.switch_state("GameOver")
