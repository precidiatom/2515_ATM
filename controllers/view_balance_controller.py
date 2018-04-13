from controllers.child_controller import ChildController
from models.user import User
from views.balance_view import ViewBalance


class ViewBalanceController(ChildController):
    def __init__(self, frame_controller, user_id):
        super().__init__(frame_controller)
        self.user = User(user_id)
        self.frame_controller = frame_controller
        self.interface = ViewBalance(self.frame_controller.master)
        self.view = None

        for acc in self.user.accounts.keys():
            self.interface.show_balance(self.user.accounts[acc]['balance'], account_type=acc)
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

    def set_balance_window(self):
        self.view = ViewBalance(self.frame_controller.atm_window.mid_frame)
        super().set_current_window(self.view)
