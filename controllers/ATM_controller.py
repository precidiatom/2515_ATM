from models.account import Account
from views.ATM_view import MainWindow


class ATMController:
    def __init__(self, master, account):
        self.master = master
        self.account_db = Account.get_persist_account(account.user['user_id'], account.account_number)
        self.atm_window = MainWindow(master)
        self.atm_window.welcome_value.config(text=self.account_db['holder_name'])
        self.atm_window.balance_button.config(command=self._view_balance())
        self.atm_window.withdraw_button.config(command=self._withdraw_fund())
        self.atm_window.deposit_button.config(command=self._deposit_fund())

        self._refresh_window()

    def _confirm_pin(self, account_num, pin):
        if Account.login(account_num, pin):
            self.account_db = Account.get_persist_account(account_num)

    def _view_balance(self):
        pass

    def _withdraw_fund(self):
        pass

    def _deposit_fund(self):
        pass

    def _refresh_window(self):
        pass
