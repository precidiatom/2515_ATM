"""
    Author: Precidia Tom & Emilie Zhang
"""
from tkinter import *

from controllers.deposit_controller import DepositController
from controllers.login_controller import LoginController
from controllers.main_controller import MainController
from controllers.view_balance_controller import ViewBalanceController
from controllers.withdraw_controller import WithdrawController


class FrameController:
    def __init__(self, master):
        """
        The main controller of the ATM, handles the switching of controllers for the different views.

        Arg:
            master: Tkinter module

        Attributes:
            user_id: the user id to retrieve account information
            current_controller: keeps record of the active controller
        """
        self.master = master
        self.current_controller = None
        self.user_id = None
        self.current_controller = LoginController(self)

    def change_login(self):
        """
        Changes controller back to Login Controller - does not pass in user id
        """
        self.current_controller.interface.overall_frame.destroy()
        del self.current_controller
        self.current_controller = LoginController(self)

    def change_controller(self, controller_name, user_id=None):
        """
        The decision tree that assigns new active controllers
        Args:
            controller_name: the name used to determine which controller to make active
            user_id: the user_id to be able to retrieve account information
        """
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
