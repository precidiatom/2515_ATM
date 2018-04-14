from models.account import Account
from models.account import User
from views.withdraw_options_frame import ViewWithdrawOptions
from views.withdraw_view import ViewWithdraw


class WithdrawController:
    def __init__(self, frame_controller, user_id):
        self.chq_account = None
        self.sav_account = None

        self.frame_controller = frame_controller
        self.interface = ViewWithdraw(self.frame_controller.master)
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))


        if 'chequing_account' in User(user_id).accounts.keys():
            self.chq_account = Account(userid=user_id, account_type='chequing_account')
            self.interface.show_current_balance('chequing account', self.chq_account.balance)
            self.interface.show_chequing()
            self.interface.chequing_but.config(command=self._click_chequing)

        if 'saving_account' in User(user_id).accounts.keys():
            self.sav_account = Account(userid=user_id, account_type='chequing_account')
            self.interface.show_current_balance('saving account', self.sav_account.balance)
            self.interface.show_saving()
            self.interface.savings_but.config(command=self._click_saving)

    def _click_chequing(self):
        self.withdraw_interface = ViewWithdrawOptions()
        self.withdraw_interface.welcome_account.config(text="Chequing")
        self.withdraw_interface.minus_20.config(
            command=lambda account=self.chq_account, amt=20: self._withdraw(account, amt))
        self.withdraw_interface.minus_40.config(
            command=lambda account=self.chq_account, amt=40: self._withdraw(account, amt))
        self.withdraw_interface.minus_60.config(
            command=lambda account=self.chq_account, amt=60: self._withdraw(account, amt))
        self.withdraw_interface.minus_80.config(
            command=lambda account=self.chq_account, amt=80: self._withdraw(account, amt))
        self.withdraw_interface.minus_100.config(
            command=lambda account=self.chq_account, amt=100: self._withdraw(account, amt))
        self.withdraw_interface.mainmenu.config(command=lambda: self.withdraw_interface.window.destroy())

    def _click_saving(self):
        self.withdraw_interface = ViewWithdrawOptions()
        self.withdraw_interface.welcome_account.config(text="Savings")
        self.withdraw_interface.minus_20.config(
            command=lambda account=self.sav_account, amt=20: self._withdraw(account, amt))
        self.withdraw_interface.minus_40.config(
            command=lambda account=self.sav_account, amt=40: self._withdraw(account, amt))
        self.withdraw_interface.minus_60.config(
            command=lambda account=self.sav_account, amt=60: self._withdraw(account, amt))
        self.withdraw_interface.minus_80.config(
            command=lambda account=self.sav_account, amt=80: self._withdraw(account, amt))
        self.withdraw_interface.minus_100.config(
            command=lambda account=self.sav_account, amt=100: self._withdraw(account, amt))
        self.withdraw_interface.mainmenu.config(command=lambda: self.withdraw_interface.window.destroy())

    def _withdraw(self, account, amount):
        if not account.withdraw(amount):
            self.interface.show_insufficient_funds()

    def set_withdraw_window(self):
        self.view = ViewWithdraw(self.frame_controller)
