from models.user import User
from views.withdraw_view import ViewWithdraw


class WithdrawController():
    def __init__(self, frame_controller, user_id):
        self.user = User.get_persist_user_obj(user_id)
        self.frame_controller = frame_controller
        self.interface = ViewWithdraw(self.frame_controller.master)
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

        self.interface.chequing_but.config(command=self._click_chequing)
        self.interface.savings_but.config(command=self._click_saving)

    def _click_chequing(self):
        print('wow')

    def _click_saving(self):
        print('bow')

    def set_withdraw_window(self):
        self.view = ViewWithdraw(self.frame_controller)
