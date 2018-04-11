from controllers.deposit_controller import DepositController
from controllers.view_balance_controller import ViewBalanceController
from controllers.withdraw_controller import WithdrawController
from models.account import Account
from views.ATM_view import MainWindow
from views.login_view import LoginWindow


class MainController:
    def __init__(self, master, account):
        self.master = master
        self.account_db = Account.get_persist_account(account.user['user_id'], account.account_number)
        self.atm_window = MainWindow(self.master)
        self.atm_window.welcome_value.config(text=self.account_db['holder_name'])
        self.atm_window.balance_button.config(command=self._view_balance)
        self.atm_window.withdraw_button.config(command=self._view_withdraw)
        self.atm_window.deposit_button.config(command=self._view_deposit)
        self.atm_balance_controller = ViewBalanceController(self)
        self.atm_deposit_controller = DepositController(self)
        self.atm_withdraw_controller = WithdrawController(self)
        self.atm_window.logout_button.config(command=self._view_login)

        #self.atm_window.chequing_but.config(command=DepositController.parent_controller)

        self._refresh_window()

    def set_main_window(self):
        self.atm_window.set_main_frame()

    def set_current_frame(self, frame):
        self.atm_window.current_frame = frame

    def _confirm_pin(self, account_num, pin):
        if Account.login(account_num, pin):
            self.account_db = Account.get_persist_account(account_num)

    def _view_balance(self):
        self.atm_balance_controller.set_balance_window()
        self.atm_window.mainframe.grid_remove()

    def _view_deposit(self):
        self.atm_deposit_controller.set_deposit_window()
        self.atm_window.mainframe.grid_remove()

    def _deposit_fund(self):
        pass

    def _view_withdraw(self):
        self.atm_withdraw_controller.set_withdraw_window()
        self.atm_window.mainframe.grid_remove()

    def _withdraw_fund(self):
        pass

    def _refresh_window(self):
        pass

    def _view_login(self):
        self.atm_window = LoginWindow(self.master)