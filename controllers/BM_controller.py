from models.account import Account
from models.chequing_account import ChequingAccount
from models.saving_account import SavingAccount
from models.term_saving_account import TermSavingAccount
from models.user import User
from views.BM_view import CommandInterface


class BMController:

    def __init__(self):
        self.session = CommandInterface()

        while not self._login():
            self.session = CommandInterface()

        while not self.session.main_menu():
            self.session.main_menu()

        user_created = False
        while not user_created:
            user_created = self.session.create_user_inputs()

        user_pin_created = False
        while not user_pin_created:
            user_pin_created = self.session.create_pin('user')
        self._create_user()

        if self.session.new_acc:
            self._create_account()

        if self.session.delete_user:
            self._delete_user()

        if self.session.delete_acc_for and self.session.delete_account:
            self._delete_account()

        if self.session.view_user_info_for:
            self._get_user_info()

        if self.session.view_acc_info_for and self.session.view_acc_num:
            self.account = Account.get_persist_account(self.session.view_acc_info_for, self.session.view_acc_num)
            self._get_account_info()
            if self.session.view_logs_for:
                self._get_logs_for_account()

    def _login(self):
        if User.login(self.session.teller_id, self.session.teller_pin) and \
                User.teller_access(self.session.teller_id):
            self.session.output({}, 'Login successful\n')
            return True
        else:
            self.session.output({'authentication_failure': 'wrong ID or PIN\n'}, '[ Login failed ]')
            return False

    def _create_user(self):
        new_user = User(self.session.new_user['user_name'], self.session.new_user['pin'], 'customer')
        self.session.output(new_user.get_user_info(), '\n[ New user created ]')

    def _delete_user(self):
        User.delete_user(self.session.delete_user)
        self.session.output({'deleted': 'user {} and their related accounts'.format(self.session.delete_user)})

    def _delete_account(self):
        Account.delete_account(self.session.delete_acc_for, self.session.delete_account)
        self.session.output(
            {'deleted': 'Account #{} for user {}'.format(self.session.delete_account, self.session.delete_acc_for)})

    def _create_account(self):
        new_account = None
        if self.session.new_acc['account_type'] == 'chequing':
            new_account = ChequingAccount(self.session.new_acc['account_holder'])
        elif self.session.new_acc['account_type'] == 'saving':
            new_account = SavingAccount(self.session.new_acc['account_holder'])
        elif self.session.new_acc['account_type'] == 'term_saving':
            new_account = TermSavingAccount(self.session.new_acc['account_holder'])

        self.session.output(new_account.get_info(),
                            '\n[ New account created for user {} ]'.format(self.session.new_acc['account_holder']))

    def _get_logs_for_account(self):
        self.session.output({}, self.account['transaction_log'])

    def _get_account_info(self):
        account = dict(self.account)
        del account['transaction_log']
        self.session.output(account)

    def _get_user_info(self):
        user = dict(User.get_persist_user_obj(self.session.view_user_info_for))
        del user['pin']
        self.session.output(user)


if __name__ == '__main__':
    controller = BMController()
