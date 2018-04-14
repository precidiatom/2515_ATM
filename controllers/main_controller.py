from models.user import User
from views.ATM_view import MainWindow


class MainController:
    def __init__(self, frame_controller, user_id):
        self.frame_controller = frame_controller
        self.master = frame_controller.master
        self.user = User(user_id)

        self.interface = MainWindow(self.master)
        self.set_main_window()

    def set_main_window(self):
        self.interface.welcome_value.config(text=self.user.user_name)
        self.interface.balance_button.config(command=self._view_balance)
        self.interface.withdraw_button.config(command=self._view_withdraw)
        self.interface.deposit_button.config(command=self._view_deposit)
        self.interface.logout_button.config(command=self._view_login)

    def set_current_frame(self, frame):
        self.interface.current_frame = frame

    def _view_balance(self):
        self.frame_controller.change_controller("view_balance")

    def _view_deposit(self):
        self.frame_controller.change_controller("view_deposit")

    def _view_withdraw(self):
        self.frame_controller.change_controller("view_withdraw")

    def _view_login(self):
        self.frame_controller.change_login()
