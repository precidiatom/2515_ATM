from models.account import Account
from models.chequing_account import ChequingAccount
from models.saving_account import SavingAccount
from models.teller import Teller
from models.term_saving_account import TermSavingAccount
from views.BM_view import CommandInterface


class BMController:

    def __init__(self):
        self.session = CommandInterface()
        while not self._login(self.session):
            self.session = CommandInterface()

        self.session.main_menu()

        if self.session.new_acc:
            self._create_account()

        if self.session.view_logs_for:
            self._get_transaction_logs()

    def _login(self, session):
        if Teller.login(session.teller_id, session.teller_password):
            print('Login successful\n')
            return True
        else:
            print('Authentication failure\n')
            return False

    def _create_account(self):
        if self.session.new_acc['account_type'] == 'chequing':
            new_account = ChequingAccount(self.session.new_acc['account_holder'])
        elif self.session.new_acc['account_type'] == 'saving':
            new_account = SavingAccount(self.session.new_acc['account_holder'])
        elif self.session.new_acc['account_type'] == 'term_saving':
            new_account = TermSavingAccount(self.session.new_acc['account_holder'])

    def _get_transaction_logs(self):
        account = Account.get_persist_account(self.session.view_logs_for)
        print(account['transaction_log'])


if __name__ == '__main__':
    bmController = BMController()
