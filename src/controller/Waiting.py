from tkinter import messagebox

from dog.start_status import StartStatus

from controller.State import State
from controller.Playing import Playing


class Waiting(State):
    
    def start_match(self, start_status: StartStatus):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        
        print(start_status.get_local_id())
        print(start_status.get_players())
        
        if start_status.code == 2:
            self._round_manager.switch_state(Playing(self._round_manager))
    
    def receive_start(self, start_status: StartStatus):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        self._round_manager.switch_state(Playing(self._round_manager))
