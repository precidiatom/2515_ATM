from models.account import Account
from models.chequing_account import ChequingAccount
from models.saving_account import SavingAccount
from models.user import User
from views.BM_view import CommandInterface


class BMController:

    def __init__(self):
        self.session = CommandInterface()
        while not self._login():
            self.session = CommandInterface()

        self._navigate_mainmenu(self.session.main_menu())

        # user_pin_created = False
        # while not user_pin_created:
        #     user_pin_created = self.session.create_pin('user')
        # self._create_user()
        #
        # if self.session.new_acc:
        #     self._create_account()
        #
        # if self.session.delete_user:
        #     self._delete_user()
        #
        # if self.session.delete_acc_for and self.session.delete_account:
        #     self._delete_account()
        #
        # if self.session.view_user_info_for:
        #     self._get_user_info()
        #
        # if self.session.view_acc_info_for and self.session.view_acc_num:
        #     self.account = Account.get_persist_account(self.session.view_acc_info_for, self.session.view_acc_num)
        #     self._get_account_info()
        #     if self.session.view_logs_for:
        #         self._get_logs_for_account()

    def _navigate_mainmenu(self, action):
        if action == '1':
            new_user = self.session.create_user_inputs()
            self._create_user(new_user)
        elif action == '2':
            new_account = self.session.create_account_inputs()
            while not self._create_account(new_account):
                new_account = self.session.create_account_inputs()
        elif action == '3':
            view_user_info = self.session.view_user_info_inputs()
            while not self._get_user_info(view_user_info):
                view_user_info = self.session.view_user_info_inputs()
        elif action == '4' or action == '5':
            self.session.view_acc_info_inputs(action)
        elif action == '6':
            self.session.delete_user_inputs()
        elif action == '7':
            self.session.delete_acc_inputs()

    def _login(self):
        if User.login(self.session.teller_id, self.session.teller_pin, 'teller'):
            return True
        else:
            self.session.output({'authentication_failure': 'wrong ID or PIN\n'}, '[ Login failed ]')
            return False

    def _create_user(self, new_user):
        new_user = User(new_user['user_name'], new_user['pin'], 'customer')
        self.session.output(new_user.get_user_info(), '\n[ New user created ]')

    def _delete_user(self):
        User.delete_user(self.session.delete_user)
        self.session.output({'deleted': 'user {} and their related accounts'.format(self.session.delete_user)})

    def _delete_account(self):
        Account.delete_account(self.session.delete_acc_for, self.session.delete_account)
        self.session.output(
            {'deleted': 'Account #{} for user {}'.format(self.session.delete_account, self.session.delete_acc_for)})

    def _create_account(self, new_account):
        new_account_created = None
        if User.check_valid_user(new_account['account_holder']):
            if new_account['account_type'] == 'chequing':
                new_account_created = ChequingAccount(new_account['account_holder'])
            elif new_account['account_type'] == 'saving':
                new_account_created = SavingAccount(self.session.new_acc['account_holder'])

            self.session.output(new_account_created.get_info(),
                                '\n[ New account created for user {} ]'.format(new_account['account_holder']))
            return True
        else:
            self.session.output({'invalid_account_holder': 'please enter valid account holder id\n'},
                                '\n[ USER ID ERROR ]')
            return False

    def _get_logs_for_account(self):
        self.session.output({}, self.account['transaction_log'])

    def _get_account_info(self):
        account = dict(self.account)
        del account['transaction_log']
        self.session.output(account)

    def _get_user_info(self, userid):
        if User.check_valid_user(userid):
            user = dict(User.get_persist_user_obj(userid))
            del user['pin']
            self.session.output(user)
            return True
        else:
            self.session.output({'invalid_user': 'please enter valid user ID!\n'}, '[ Fail to see user info ]')
            return False


if __name__ == '__main__':
    controller = BMController()
