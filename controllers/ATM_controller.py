from models.account import Account
from observer import Observer
from views.ATM_view import MainWindow


class ATMController(Observer):
    def __init__(self, master, userid):
        self.master = master
        self.account_db = Account.get_persist_account(userid)
        self.atm_window = MainWindow(master)
        self.atm_window.balance_button.config(command=self._view_balance())
        self.atm_window.withdraw_button.config(command=self._withdraw_fund())
        self.atm_window.deposit_button.config(command=self._deposit_fund())

        self._refresh_window()
        self.account_db.add_observer(self)

    def _confirm_pin(self, account_num, pin):
        if Account.login(account_num, pin):
            self.account_db = Account.get_persist_account(account_num)

    def _view_balance(self):
        self.account_db.get_balance()

    def _withdraw_fund(self):
        pass

    def _deposit_fund(self):
        pass

    def _refresh_window(self):
        pass

    def update(self, obj, **kwargs):
        self._refresh_window()
