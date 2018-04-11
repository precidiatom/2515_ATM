from controllers.deposit_controller import DepositController
from controllers.view_balance_controller import ViewBalanceController
from controllers.withdraw_controller import WithdrawController
from models.account import Account
from views.ATM_view import MainWindow
from views.login_view import LoginWindow

class LoginController:
    def __init__(self, master, account):
        self.master = master
        self.account_db = Account.get_persist_account(account.user['user_id'], account.account_number)
        self.atm_window = LoginWindow(self.master)

        self._refresh_window()

    def set_main_window(self):
        self.atm_window.set_main_frame()

    def set_current_frame(self, frame):
        self.atm_window.current_frame = frame

    def _confirm_pin(self, account_num, pin):
        if Account.login(account_num, pin):
            self.account_db = Account.get_persist_account(account_num)

    def _refresh_window(self):
        pass

    def _view_login(self):
        self.atm_window = LoginWindow(self.master)