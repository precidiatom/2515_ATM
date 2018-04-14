from models.user import User
from views.balance_view import ViewBalance


class ViewBalanceController:
    def __init__(self, frame_controller, user_id):
        self.user = User(user_id)
        self.frame_controller = frame_controller
        self.interface = ViewBalance(self.frame_controller.master)

        for acc in self.user.accounts.keys():
            self.interface.show_balance(self.user.accounts[acc]['balance'], account_type=acc)
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

