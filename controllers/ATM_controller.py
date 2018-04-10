from controllers.ViewBalanceController import ViewBalanceController
from models.account import Account
from views.ATM_view import MainWindow


class ATMController:
    def __init__(self, master, account):
        self.master = master
        self.account_db = Account.get_persist_account(account.user['user_id'], account.account_number)
        self.atm_window = None
        self.atm_balance_controller = ViewBalanceController(self)
        # self.atm_deposit_window = ViewDeposit(self.atm_window.mid_frame, self).grid(row=1, padx=150, pady=55)
        # self.atm_withdrawal_window = ViewWithdraw(self.atm_window.mid_frame, self).grid(row=1, padx=300, pady=55)

        # this auto calls the method but more cleaner???<_>
        # self.atm_window.balance_button.config(command=self._change_view('balance'))
        # self.atm_window.withdraw_button.config(command=self._withdraw_fund)
        # self.atm_window.deposit_button.config(command=self._change_view('deposit'))

        # self.atm_window.ViewBalance.mainmenu.config(command=self._returnmainmenu)
        self._refresh_window()

    def set_main_window(self):
        self.atm_window = MainWindow(self.master)
        self.atm_window.welcome_value.config(text=self.account_db['holder_name'])
        self.atm_window.balance_button.config(command=self._view_balance)
        self.atm_window.withdraw_button.config(command=self._view_withdraw)
        self.atm_window.deposit_button.config(command=self._view_deposit)

    def set_current_frame(self, frame):
        self.atm_window.current_frame = frame

    def _confirm_pin(self, account_num, pin):
        if Account.login(account_num, pin):
            self.account_db = Account.get_persist_account(account_num)

# wip??
    def _change_view(self, frame_type):
        if frame_type == 'balance':
            self.atm_window.mainframe.grid_remove()
            print('bal')
            self.current_frame = self.atm_balance_window
        elif frame_type == 'deposit':
            self.atm_window.mainframe.grid_remove()
            print('dep')
            self.current_frame = self.atm_deposit_window

    def _view_balance(self):
        self.atm_balance_controller.set_balance_window()
        self.atm_window.mainframe.grid_remove()
        self.set_current_frame(self.atm_balance_controller.atm_balance_window)

    def _view_deposit(self):
        self.atm_window.mainframe.grid_remove()
        self.current_frame = self.atm_deposit_window

    def _deposit_fund(self):
        pass

    def _view_withdraw(self):
        self.atm_window.mainframe.grid_remove()
        self.current_frame = self.atm_withdrawal_window

    def _withdraw_fund(self):
        pass

    def _refresh_window(self):
        pass
