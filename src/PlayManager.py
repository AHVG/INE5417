


class PlayManager:

    def __init__(self, ultimate_ttt, first_player='X') -> None:
        self.current_player = first_player
        self.ultimate_ttt = ultimate_ttt
        self.last_play = None

    def play_allowed(self, u_position, ttt_position):
        i, j = u_position
        k, h = ttt_position

        tic_tac_toe = self.ultimate_ttt.board[i][j]

        if self.last_play:
            if self.last_play != u_position:
                return False

        if tic_tac_toe.get_value():
            return False

        if tic_tac_toe.board[h][k].get_value():
            return False

        return True

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"
