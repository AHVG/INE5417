
from tkinter import messagebox

from dog.start_status import StartStatus

from controller.State import State


class Ready(State):

    def _set_players(self, start_status: StartStatus):
        local_player = self._round_manager.get_local_player()
        local_player.set_id(start_status.get_local_id())
        local_player.set_symbol("X")

        remote_player = self._round_manager.get_remote_player()
        remote_player.set_name(start_status.get_players()[1][0])
        remote_player.set_id(start_status.get_players()[1][1])
        remote_player.set_symbol("O")

        first_player = local_player if start_status.get_players()[0][2] == "1" else remote_player
        self._round_manager.set_current_player(first_player)

    def entry(self):
        self._round_manager.get_ultimate_tic_tac_toe.reset()

    def start_match(self, start_status: StartStatus):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

        print(f"local_player_id {start_status.get_local_id()}")
        print(f"player {start_status.get_players()}")

        if start_status.code == '2':
            self._set_players(start_status)
            self._round_manager.switch_state("Playing")

    def receive_start(self, start_status: StartStatus):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

        print(f"local_player_id {start_status.get_local_id()}")
        print(f"player {start_status.get_players()}")

        self._set_players(start_status)
        self._round_manager.switch_state("Waiting")
