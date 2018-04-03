from observer import Observer
from views.ATM_view import MainWindow


class ATMController(Observer):
    def __init__(self, master, account_db):
        self.master = master
        self.account_db = account_db
        self.atm_window = MainWindow(master)
        self.atm_window.balance_button.config(command=self._view_balance())
        self.atm_window.withdraw_button.config(command=self._withdraw_fund())
        self.atm_window.deposit_button.config(command=self._deposit_fund())

    def _view_balance(self):
        pass

    def _withdraw_fund(self):
        pass

    def _deposit_fund(self):
        pass

    def _refresh_window(self):
        pass

    def update(self, obj, **kwargs):
        self._refresh_window()
