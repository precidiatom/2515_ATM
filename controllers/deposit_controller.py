"""
    Authors: Emilie Zhang & Precidia Tom
"""
from tkinter import messagebox

from models.account import Account
from models.user import User
from views.deposit_entry_frame import ViewDepositInput
from views.deposit_view import ViewDeposit


class DepositController:
    def __init__(self, frame_controller, user_id):
        """
        The deposit controller that controls the event listeners and widgets of the
        deposit view.

        Args:
            frame_controller: the controller that controls the current frame
            user_id: the user id that is logged in to this sessions
        """

        self.user_id = user_id
        self.chq_account = None
        self.sav_account = None

        self.frame_controller = frame_controller
        self.interface = ViewDeposit(frame_controller.master)

        self.interface.main_menu_btn.config()
        self.interface.main_menu_btn.config(
            command=lambda: self.frame_controller.change_controller('main_menu', self.frame_controller.user_id))

        # Checks if user has chequing/saving account - only existing account info is displayed
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
        """
        Configures the buttons and account balance for chequing account
        """
        self.deposit_interface = ViewDepositInput(self.frame_controller.master)
        self.deposit_interface.welcome_account.config(text="Chequing")
        self.deposit_interface.current_balance.config(text=self.chq_account.balance)
        self.deposit_interface.mainmenu.config(command=lambda: self.deposit_interface.overall_frame.destroy())
        self.deposit_interface.deposit_but.bind("<Button-1>",
                                                lambda ev, account=self.chq_account: self._deposit(ev, account))

    def _click_saving(self):
        """
        Configures the buttons and account balance for savings account
        """
        self.deposit_interface = ViewDepositInput(self.frame_controller.master)
        self.deposit_interface.welcome_account.config(text="Savings")
        self.deposit_interface.current_balance.config(text=self.sav_account.balance)
        self.deposit_interface.mainmenu.config(command=lambda: self.deposit_interface.overall_frame.destroy())
        self.deposit_interface.deposit_but.bind("<Button-1>",
                                                lambda ev, account=self.sav_account: self._deposit(ev, account))

    def _deposit(self, ev, account):
        """
        The controller method that deposits the entered amount into an account

        Args:
            ev: the event handled
            account: the account being deposited into

        Raises:
            ValueError: if the deposit_amt does not contain only integers

        """

        try:
            deposit_amt = float(self.deposit_interface.deposit_amt.get())
            if deposit_amt <= 0:
                raise ValueError
            account.deposit(deposit_amt)
            if self.chq_account:
                messagebox.showinfo("Transaction", "You have deposited {}".format(deposit_amt))
                self.deposit_interface.current_balance.config(text=account.balance)
                self.interface.show_chq_balance(account.balance)
            elif self.sav_account:
                messagebox.showinfo("Transaction", "You have deposited {}".format(deposit_amt))
                self.deposit_interface.current_balance.config(text=account.balance)
                self.interface.show_sav_balance(account.balance)
        except ValueError:
            messagebox.showinfo("Invalid input", "Please enter only numbers greater than 0")
