"""
    Author: Emile Zhang
"""

from models.account import Account
from models.user import User
from views.BM_view import CommandInterface


class BMController:

    def __init__(self):
        """
        BMController is the controller of the CLI.

        Attributes:
            self.session creates the CLI view instance
        """
        self.session = CommandInterface()
        while not self._login():
            self.session = CommandInterface()
        self._navigate_mainmenu(self.session.main_menu())

    def _navigate_mainmenu(self, action):
        """
        This is the main decision tree for the CLI.
        The corresponding actions and integers are found in the BM_View.

        Args:
            action (int): the integer passed in represents the selected action of the CLI user
        """
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
            view_acc_info = self.session.view_acc_info_for_user_input()
            while not self._get_account_info(view_acc_info, action):
                view_acc_info = self.session.view_acc_info_for_user_input()

        elif action == '6':
            delete_user = self.session.delete_user_inputs()
            while not self._delete_user(delete_user):
                delete_user = self.session.delete_user_inputs()
        elif action == '7':
            delete_cheq_acc = self.session.delete_cheq_acc_inputs()
            while not self._delete_cheq_acc(delete_cheq_acc):
                delete_cheq_acc = self.session.delete_cheq_acc_inputs()
        elif action == '8':
            delete_sav_acc = self.session.delete_sav_acc_inputs()
            while not self._delete_sav_acc(delete_sav_acc):
                delete_sav_acc = self.session.delete_sav_acc_inputs()
        elif action == 'q':
            exit()

        self._navigate_mainmenu(self.session.main_menu())

    def _login(self):
        """
        Authenticates the user account by checking if the user id and pin match with the information stored.

        Returns:
             bool:  True if the input user id matches the database user id
                    False if do not match
        """
        if User.login(self.session.teller_id, self.session.teller_pin, 'teller'):
            return True
        else:
            self.session.output({'authentication_failure': 'wrong ID or PIN\n'}, '[ Login failed ]')
            return False

    def _create_user(self, new_user):
        """
        Creates new customer using the User class as the parameter

        Args:
             new_user (obj): User class which requires: user's name, pin, and user-type
        """
        new_user = User(user_name=new_user['user_name'], pin=new_user['pin'], user_type='customer')
        self.session.output(new_user.get_user_info(), '\n[ New user created ]')

    def _delete_user(self, user):
        """
        Deletes an existing user from the model.

        Args:
            user (obj): the User to be deleted
        Returns:
            bool:   True if user exists in the model
                    False if the input user id does not exist in the model
        """
        if User.delete_user(user):
            self.session.output({'deleted': 'user {} and their related accounts'.format(user)})
            return True
        else:
            self.session.output({'invalid_user': 'please enter valid user ID!\n'}, '[ Fail to delete user ]')
            return False

    def _delete_cheq_acc(self, userid):
        """
        Deletes a specified chequing account for a customer.

        Args:
            userid (str): the id for the chequing account
        Returns:
            bool:   True if the user id exists - the chequing account will be deleted
                    False if the user id does not exist - prints a message indicating incorrect id
        """
        if userid == 'b':
            self._navigate_mainmenu(1)

        account = Account(userid=userid, account_type='chequing_account')
        if account.delete_account():
            self.session.output(
                {'deleted': 'Chequing account deleted for user {}'.format(userid)})
            return True
        else:
            self.session.output({'Error': 'Please re-enter user id or press \'b\' to return to main menu!\n'},
                                '[ Invalid user ID or selected account does not exist ]')
            return False

    def _delete_sav_acc(self, userid):
        """
        Deletes a specified savings account for a customer.

        Args:
            userid (str): the savings account id

        Returns:
             bool:  True if the id matches an existing account and will delete from the model
                    False if id does not match and will print error message
        """
        if userid == 'b':
            self._navigate_mainmenu(1)
        account = Account(userid=userid, account_type='saving_account')
        if account.delete_account():
            self.session.output(
                {'deleted': 'Saving account deleted for user {}'.format(userid)})
            return True
        else:
            self.session.output({'Error': 'Invalid user ID or selected account does not exist!\n'},
                                '[ Fail to delete account ]')
            return False

    def _create_account(self, new_account):
        """
        To create new accounts for a customer, check if the customer already has the selected account type.
        If customer does not already have the selected account type, will create new account with initialized balance

        Args:
            new_account (str): the user id of the customer

        Returns:
             bool:  True if user id exists, will create a new chequing/saving account
                    False if user id does not exists, will print error message
        """
        if new_account == 'b':
            self._navigate_mainmenu(1)
        if User.check_existing_user(new_account['account_holder']):
            user = User(new_account['account_holder'])
            if new_account['account_type'] in user.accounts.keys():
                self.session.output({
                    'error':
                        'user already has an account of this type. select another one '
                        'or press \'b\' to return to main menu.\n'}, '[ INVALID ACCOUNT TYPE ERROR ]')
                return False
            else:
                new_account_created = Account(userid=user.user_id, account_type=new_account['account_type'],
                                              balance=new_account['initial_balance'])
                self.session.output(new_account_created.get_info(),
                                    '\n[ New account created for user {} ]'.format(new_account['account_holder']))
                return True
        else:
            self.session.output({'invalid_account_holder': 'please enter valid account holder id\n'},
                                '\n[ USER ID ERROR ]')
            return False

    def _get_account_info(self, user_id, action=''):
        """
        Displays user's account information.

        Args:
            user_id (str): The user id that the CLI user wants to check information about
            action (int): is 5 if CLI user wants to see transaction logs
        """
        if User.check_existing_user(user_id):
            user = User(user_id)
            accounts_info = dict(user.accounts)
            transaction_logs = ''
            for v in accounts_info.values():
                if action == '5':
                    transaction_logs += v['transaction_log']
                del v['transaction_log']
            self.session.output(accounts_info, transaction_logs)
            return True
        else:
            self.session.output({'invalid_user': 'please enter valid user ID!\n'}, '[ Fail to see user info ]')
            return False

    def _get_user_info(self, userid):
        """
        Displays the user's basic information

        Args:
            userid (str): the user's user id which is needed to authenticate user

        Returns:
            bool:   True if user id exists in the model
                    False if user does not exist, will keep asking until valid user id is inputted
        """
        if User.check_existing_user(userid):
            user = User(userid)
            self.session.output({
                'user_id': userid,
                'user_name': user.user_name,
                'user_type': user.user_type
            })
            return True
        else:
            self.session.output({'invalid_user': 'please enter valid user ID!\n'}, '[ Fail to see user info ]')
            return False


if __name__ == '__main__':
    controller = BMController()
