from models.user import User
from views.deposit_entry_frame import ViewDepositInput
from views.deposit_view import ViewDeposit


class DepositController():
    def __init__(self, frame_controller, user_id):
        self.user = User.get_persist_user_obj(user_id)
        self.frame_controller = frame_controller
        self.interface = ViewDeposit(frame_controller.master)

        self.interface.main_menu_btn.config()
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))
        self.interface.chequing_but.config(command=self._click_chequing)
        self.interface.savings_but.config(command=self._click_saving)

    def set_deposit_window(self):
        self.view = ViewDeposit(self.frame_controller.atm_window.mid_frame)

    def _click_chequing(self):
        self.interface = ViewDepositInput()
        self.interface.welcome_account.config(text="Chequing")
        self.interface.mainmenu.config(command=lambda: self.interface.window.destroy())
        deposit_amt = self.interface.deposit_amt.get()

    def _click_saving(self):
        self.interface = ViewDepositInput()
        self.interface.welcome_account.config(text="Savings")
        self.interface.mainmenu.config(command=lambda: self.interface.window.destroy())
