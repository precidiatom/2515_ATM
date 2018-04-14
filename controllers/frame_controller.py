from tkinter import *

from controllers.deposit_controller import DepositController
from controllers.login_controller import LoginController
from controllers.main_controller import MainController
from controllers.view_balance_controller import ViewBalanceController
from controllers.withdraw_controller import WithdrawController


class FrameController:
    def __init__(self, master):
        self.master = master
        self.current_controller = None
        self.user_id = None
        self.current_controller = LoginController(self)

    def change_login(self):
        self.current_controller.interface.overall_frame.destroy()
        del self.current_controller
        self.current_controller = LoginController(self)

    def change_controller(self, controller_name, user_id=None):
        self.current_controller.interface.overall_frame.destroy()
        del self.current_controller
        if controller_name == 'main_menu':
            self.current_controller = MainController(self, self.user_id)
        elif controller_name == 'view_balance':
            self.current_controller = ViewBalanceController(self, self.user_id)
        elif controller_name == 'view_deposit':
            self.current_controller = DepositController(self, self.user_id)
        elif controller_name == 'view_withdraw':
            self.current_controller = WithdrawController(self, self.user_id)


if __name__ == '__main__':
    root = Tk()
    new_frame_controller = FrameController(root)
    mainloop()
