from tkinter import messagebox

from models.account import Account
from models.user import User
from views.deposit_entry_frame import ViewDepositInput
from views.deposit_view import ViewDeposit


class DepositController:
    def __init__(self, frame_controller, user_id):
        self.user_id = user_id
        self.chq_account = None
        self.sav_account = None

        self.frame_controller = frame_controller
        self.interface = ViewDeposit(frame_controller.master)

        self.interface.main_menu_btn.config()
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

        if 'chequing_account' in User(user_id).accounts.keys():
            self.chq_account = Account(userid=user_id, account_type='chequing_account')
            self.interface.show_chequing()
            self.interface.show_chq_balance(self.chq_account.balance)
            self.interface.chequing_but.config(command=self._click_chequing)

        if 'saving_account' in User(user_id).accounts.keys():
            self.sav_account = Account(userid=user_id, account_type='saving_account')
            self.interface.show_saving()
            self.interface.show_sav_balance(self.sav_account.balance)
            self.interface.savings_but.config(command=self._click_saving)

    def _click_chequing(self):
        self.interface = ViewDepositInput(self.frame_controller.master)
        self.interface.welcome_account.config(text="Chequing")
        self.interface.current_balance.config(text=self.chq_account.balance)
        self.interface.mainmenu.config(command=lambda: self.interface.overall_frame.destroy())
        self.interface.deposit_but.bind("<Button-1>", lambda ev, account_type="chequing_account": self._deposit(ev,
                                                                                                                "chequing_account"))

    def _click_saving(self):
        self.interface = ViewDepositInput(self.frame_controller.master)
        self.interface.welcome_account.config(text="Savings")
        self.interface.current_balance.config(text=self.sav_account.balance)
        self.interface.mainmenu.config(command=lambda: self.interface.overall_frame.destroy())
        self.interface.deposit_but.bind("<Button-1>", lambda ev, account_type="saving_account": self._deposit(ev,
                                                                                                              "saving_account"))

    def _deposit(self, ev, account_type):
        account = Account(self.user_id, account_type=account_type)
        deposit_amt = float(self.interface.deposit_amt.get())
        account.deposit(deposit_amt)
        if self.chq_account:
            messagebox.showinfo("Transaction", "You have deposited {}".format(deposit_amt))
            self.interface.current_balance.config(text=self.chq_account.balance)
        elif self.sav_account:
            messagebox.showinfo("Transaction", "You have deposited {}".format(deposit_amt))
            self.interface.current_balance.config(text=self.sav_account.balance)
