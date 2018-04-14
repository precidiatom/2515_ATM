"""
    Author: Emile Zhang
"""


class CommandInterface:

    def __init__(self):
        """
        The View for the CLI. Generally prints all of the menus and messages.

        Attributes:
            teller_id: to start a employee session, will need their id
            teller_pin: to authenticate identity, will need their pin
            new_acc: empty dict to store new account info
            new_user: empty dict to store new user info
            view_user_info_for: variable to store CLI user input for the queried user_id
            view_acc_info_for: variable to store account holder user id
            delete_user = stores the CLI user requested user to delete
            delete_cheq_acc_for = stores the CLI user requested chequing account to delete
            delete_sav_acc_for = stores the CLI user requested saving account to delete
            actions_list: stores available list of actions CLI user can do

        Author:
            Emilie Zhang

        """
        self.teller_id = input('Teller ID: ')
        self.teller_pin = input('PIN: ')
        self.action = None
        self.new_acc = {}
        self.new_user = {}
        self.view_user_info_for = None
        self.view_acc_info_for = None
        self.delete_user = None
        self.delete_cheq_acc_for = None
        self.delete_sav_acc_for = None

        self.actions_list = [str(i) for i in range(1, 9)]

    def main_menu(self, failed=False):

        if failed:
            self.output({'Error': 'please choose from available actions'}, '\n[ Invalid Input ]')

        print('\nMAIN MENU')
        print('------------------------')
        print('1 - Create a user')
        print('2 - Create an account for an user\n')
        print('3 - View info for a user')
        print('4 - View account info for a user')
        print('5 - View transaction logs for a user\n')
        print('6 - Delete a user')
        print('7 - Delete a chequing account')
        print('8 - Delete a saving account\n')
        print('q - QUIT')

        self.action = input()
        return self.action if self.action in self.actions_list or self.action == 'q' else self.main_menu(failed=True)

    def create_user_inputs(self):
        """
        Creates a new user by retrieving CLI user input, needs name length greater than one.

        Returns:
            self.create_pin() if input length is greater than one
            create_user_inputs repeatedly if invalid input

        """
        self.new_user['user_name'] = input('\nEnter the first and last name of the user: ')

        if len(self.new_user['user_name']) > 0:
            return self.create_pin()
        else:
            self.output({'error': 'please enter valid user name'})
            return self.create_user_inputs()

    def create_pin(self):
        """
        Creates a new user's pin by retrieving user input

        Returns:
            self.new_user (dict): contains key-value pairs of user id and pin
            self.create_pin is returned repeatedly until valid input

        """
        self.new_user['pin'] = input('Create PIN: ')
        if len(self.new_user['pin']) > 0:
            return self.new_user
        else:
            self.output({'error': 'please enter valid PIN'})
            return self.create_pin()

    def create_account_inputs(self):
        """
        The menu option to Creating accounts for a user

        Returns:
            self.choose_account_inputs - the sub-menu of account types to create
        """
        self.new_acc['account_holder'] = input('User ID of account holder: ')
        return self.choose_account_inputs()

    def choose_account_inputs(self):
        """
        Presents the menu to select type of account to create.

        Returns:
             self.initial_balance_input - the method requesting for account initial balance.
        """
        print('\nWhat kind of account would you like to create?')
        print('------------------------')
        print('1 - Chequing Account')
        print('2 - Saving Account')
        account_type = input()

        self.new_acc['account_type'] = self._resolve_account_type(account_type)
        return self.initial_balance_input()

    def initial_balance_input(self):
        """
        Initializes the new account's balance.

        Returns:
             self.new_acc (dict) - the container of new user information
        """
        self.new_acc['initial_balance'] = input('Enter initial balance for account or press ENTER to skip: ')
        return self.new_acc

    def view_user_info_inputs(self):
        """
        Stores and retrieves user id to view the user's information

        Returns:
             self.view_user_info_for (str) - CLI user's input
        """
        self.view_user_info_for = input('Enter the user ID you want to view info for: ')
        return self.view_user_info_for

    def view_acc_info_for_user_input(self):
        """
        Retrieves and stores the user id to view their account information.

        Returns:
             self.view_acc_info_for (str) - CLI user's input
        """
        self.view_acc_info_for = input('Enter the user ID of the account holder: ')
        return self.view_acc_info_for

    def delete_cheq_acc_inputs(self):
        """
        Retrieves and stores user id in order to delete their chequing account.

        Returns:
             self.delete_cheq_acc_for (str) - CLI user's input
        """
        self.delete_cheq_acc_for = input('Enter the user ID of the account holder: ')
        return self.delete_cheq_acc_for

    def delete_sav_acc_inputs(self):
        """
        Stores and retrieves user id to delete their savings account.

        Returns:
             self.delete_sav_acc_for (str) - CLI user's input
        """
        self.delete_sav_acc_for = input('Enter the user ID of the account holder: ')
        return self.delete_sav_acc_for

    def delete_user_inputs(self):
        """
        Retrieve and store user id to delete that user from the system.

        Returns:
             self.delete_user(str) - CLI user's input
        """
        self.delete_user = input('Enter the ID for the user you want to delete: ')
        return self.delete_user

    @staticmethod
    def output(obj, msg=''):
        """
        Prints output; for error messages or items in a dictionary container

        Args:
            obj (dict): The object that contains the information to print/simple print statement
            msg (str): any additional print statements, is optional
        """
        print(msg)
        for k, v in obj.items():
            print('{}: {}'.format(k.replace('_', ' ').upper(), v))

    def _resolve_account_type(self, num):
        """
        Resolve the user's account type by passing in the correct string for the self.new_user dict

        Args:
            num (str): the number that represents the user's account creation

        Returns:
             "chequing_account" as value for new_user["account_type"] if choice is 1
             "saving_account" as value for new_user["account_type"] if choice is 2
        """
        if str(num) == '1':
            return 'chequing_account'
        elif str(num) == '2':
            return 'saving_account'
        else:
            self.output({'error': 'invalid account type'})
            self.choose_account_inputs()
