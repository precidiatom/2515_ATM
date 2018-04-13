from models.account import Account
from views.withdraw_options_frame import ViewWithdrawOptions
from views.withdraw_view import ViewWithdraw


class WithdrawController():
    def __init__(self, frame_controller, user_id):
        self.user_id = user_id

        self.frame_controller = frame_controller
        self.interface = ViewWithdraw(self.frame_controller.master)
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

        self.interface.chequing_but.config(command=self._click_chequing)
        self.interface.savings_but.config(command=self._click_saving)

    def _click_chequing(self):
        self.interface = ViewWithdrawOptions()
        self.interface.welcome_account.config(text="Chequing")
        self.interface.minus_20.config(
            command=lambda account_type='chequing_account', amt=20: self._withdraw(account_type, amt))
        self.interface.minus_40.config(
            command=lambda account_type='chequing_account', amt=40: self._withdraw(account_type, amt))
        self.interface.minus_60.config(
            command=lambda account_type='chequing_account', amt=60: self._withdraw(account_type, amt))
        self.interface.minus_80.config(
            command=lambda account_type='chequing_account', amt=80: self._withdraw(account_type, amt))
        self.interface.minus_100.config(
            command=lambda account_type='chequing_account', amt=100: self._withdraw(account_type, amt))
        self.interface.mainmenu.config(command=lambda: self.interface.window.destroy())

    def _click_saving(self):
        self.interface = ViewWithdrawOptions()
        self.interface.welcome_account.config(text="Savings")
        self.interface.minus_20.config(
            command=lambda account_type='saving_account', amt=20: self._withdraw(account_type, amt))
        self.interface.minus_40.config(
            command=lambda account_type='saving_account', amt=40: self._withdraw(account_type, amt))
        self.interface.minus_60.config(
            command=lambda account_type='saving_account', amt=60: self._withdraw(account_type, amt))
        self.interface.minus_80.config(
            command=lambda account_type='saving_account', amt=80: self._withdraw(account_type, amt))
        self.interface.minus_100.config(
            command=lambda account_type='saving_account', amt=100: self._withdraw(account_type, amt))
        self.interface.mainmenu.config(command=lambda: self.interface.window.destroy())

    def _withdraw(self, account_type, amount):
        account = Account(self.user_id, account_type=account_type)
        account.withdraw(amount)
        print(account.balance, account.user.accounts[account_type]['balance'])

    def set_withdraw_window(self):
        self.view = ViewWithdraw(self.frame_controller)
