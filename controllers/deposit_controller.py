from models.account import Account
from views.deposit_entry_frame import ViewDepositInput
from views.deposit_view import ViewDeposit


class DepositController():
    def __init__(self, frame_controller, user_id):
        self.user_id = user_id
        self.frame_controller = frame_controller
        self.interface = ViewDeposit(frame_controller.master)

        self.interface.main_menu_btn.config()
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))
        self.interface.chequing_but.config(command=self._click_chequing)
        self.interface.savings_but.config(command=self._click_saving)

    def _click_chequing(self):
        self.interface = ViewDepositInput()
        self.interface.welcome_account.config(text="Chequing")
        self.interface.mainmenu.config(command=lambda: self.interface.window.destroy())
        self.interface.deposit_but.bind("<Button-1>", lambda ev, account_type="chequing_account": self._deposit(ev,
                                                                                                                "chequing_account"))

    def _click_saving(self):
        self.interface = ViewDepositInput()
        self.interface.welcome_account.config(text="Savings")
        self.interface.mainmenu.config(command=lambda: self.interface.window.destroy())
        self.interface.deposit_but.bind("<Button-1>", lambda ev, account_type="saving_account": self._deposit(ev,
                                                                                                              "saving_account"))

    def _deposit(self, ev, account_type):
        account = Account(self.user_id, account_type=account_type)
        deposit_amt = int(self.interface.deposit_amt.get())
        account.deposit(deposit_amt)
        self.interface.current_balance.config(text=account.balance)
