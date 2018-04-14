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
            self.interface.show_chequing()
            self.interface.show_chq_balance(self.chq_account.balance)
            self.interface.chequing_but.config(command=self._click_chequing)

        if 'saving_account' in User(user_id).accounts.keys():
            self.sav_account = Account(userid=user_id, account_type='saving_account')
            self.interface.show_saving()
            self.interface.show_sav_balance(self.sav_account.balance)
            self.interface.savings_but.config(command=self._click_saving)

    def _click_chequing(self):
        self.withdraw_interface = ViewWithdrawOptions(self.frame_controller.master)
        self.withdraw_interface.welcome_account.config(text="Chequing")
        self.withdraw_interface.display_balance.config(text="Current balance: $" + str(self.chq_account.balance))
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

        self.withdraw_interface.minus_other.bind(
            "<Button-1>", lambda ev, account=self.chq_account: self._withdraw(account=account))

        self.withdraw_interface.mainmenu.config(command=lambda: self.withdraw_interface.overall_frame.destroy())

    def _click_saving(self):
        self.withdraw_interface = ViewWithdrawOptions(self.frame_controller.master)
        self.withdraw_interface.welcome_account.config(text="Savings")
        self.withdraw_interface.display_balance.config(text="Current balance: $" + str(self.sav_account.balance))
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

        self.withdraw_interface.minus_other.bind(
            "<Button-1>", lambda ev, account=self.sav_account: self._withdraw(account=account))

        self.withdraw_interface.mainmenu.config(command=lambda: self.withdraw_interface.overall_frame.destroy())

    def _withdraw(self, account, amount=0):
        if amount == 0 and len(self.withdraw_interface.get_other_amount()) > 0:
            try:
                amount = float(self.withdraw_interface.get_other_amount())
                if not account.withdraw(amount) and amount > 0:
                    self.interface.show_msg_box('Error', 'Insufficient funds!')
                else:
                    self.interface.show_msg_box('Withdrawal', 'You withdrew $' + str(amount))
                    if self.chq_account:
                        self.withdraw_interface.display_balance.config(
                            text="Current balance: $" + str(self.chq_account.balance))
                        self.interface.show_chq_balance(self.chq_account.balance)
                    if self.sav_account:
                        self.withdraw_interface.display_balance.config(
                            text="Current balance: $" + str(self.sav_account.balance))
                        self.interface.show_sav_balance(self.sav_account.balance)
            except ValueError:
                self.interface.show_msg_box('Invalid input', 'Please enter only numbers greater than 0')

    def set_withdraw_window(self):
        self.view = ViewWithdraw(self.frame_controller)
