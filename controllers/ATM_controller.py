import tkinter as tk
from models.account import Account
from views.ATM_view import MainWindow
from views.view_balance_frame import ViewBalance
from views.deposit_frame import ViewDeposit
from views.withdraw_frame import ViewWithdraw
from views.withdraw_options import ViewWithdrawOptions

class ATMController:
    def __init__(self, master, account):
        self.master = master
        self.account_db = Account.get_persist_account(account.user['user_id'], account.account_number)
        self.atm_window = MainWindow(master)
        self.atm_window.welcome_value.config(text=self.account_db['holder_name'])
        self.atm_window.balance_button.config(command=self._view_balance)
        self.atm_window.withdraw_button.config(command=self._view_withdraw)
        self.atm_window.deposit_button.config(command=self._view_deposit)

        # this auto calls the method but more cleaner???<_>
        # self.atm_window.balance_button.config(command=self._change_view('balance'))
        # self.atm_window.withdraw_button.config(command=self._withdraw_fund)
        # self.atm_window.deposit_button.config(command=self._change_view('deposit'))

        # self.atm_window.ViewBalance.mainmenu.config(command=self._returnmainmenu)
        self._refresh_window()

    def _confirm_pin(self, account_num, pin):
        if Account.login(account_num, pin):
            self.account_db = Account.get_persist_account(account_num)

# wip??
    def _change_view(self, frame_type):
        if frame_type == 'balance':
            self.atm_window.mainframe.grid_remove()
            print('bal')
            self.current_frame = ViewBalance(self.atm_window.mid_frame, self).grid(row=1, padx=150, pady=55)
        elif frame_type == 'deposit':
            self.atm_window.mainframe.grid_remove()
            print('dep')
            self.current_frame = ViewDeposit(self.atm_window.mid_frame, self).grid(row=1, padx=150, pady=55)

    def _view_balance(self):
        self.atm_window.mainframe.grid_remove()
        self.current_frame = ViewBalance(self.atm_window.mid_frame, self).grid(row=1, padx=300, pady=55)

    def _view_deposit(self):
        self.atm_window.mainframe.grid_remove()
        self.current_frame = ViewDeposit(self.atm_window.mid_frame, self).grid(row=1, padx=300, pady=55)

    def _deposit_fund(self):
        pass

    def _view_withdraw(self):
        self.atm_window.mainframe.grid_remove()
        self.current_frame = ViewWithdraw(self.atm_window.mid_frame, self).grid(row=1, padx=300, pady=55)

    def _withdraw_fund(self):
        pass

    def _returnmainmenu(self):
        del self.atm_window.MainWindow.current_frame
        self.atm_window.welcome.destroy()
        self.atm_window.acc_balance.grid_remove()
        self.atm_window.mainmenu.grid_remove()
        self.atm_window.MainWindow.current_frame = tk.Frame(self.MainWindow.mainframe.grid(row=1, padx=150, pady=55))

    def _refresh_window(self):
        pass
