from views.balance_view import ViewBalance
from views.balance_view import ViewBalance


class ViewBalanceController():
    def __init__(self, frame_controller, user_id):
        self.user = User.get_persist_user_obj(user_id)
        self.frame_controller = frame_controller
        self.interface = ViewBalance(self.frame_controller.master)

        self.interface.show_balance(self.frame_controller.user_id)
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

    def set_balance_window(self):
        self.view = ViewBalance(self.frame_controller.atm_window.mid_frame)
        super().set_current_window(self.view)
