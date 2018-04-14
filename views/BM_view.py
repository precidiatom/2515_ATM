class CommandInterface:

    def __init__(self):
        self.teller_id = input('Teller ID: ')
        self.teller_pin = input('PIN: ')
        self.action = None
        self.new_acc = {}
        self.new_user = {}
        self.view_logs_for = None
        self.view_user_info_for = None
        self.view_acc_info_for = None
        self.view_acc_num = None
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
        print('8 - Delete a saving account')
        print('q - QUIT')

        self.action = input()
        return self.action if self.action in self.actions_list or self.action == 'q' else self.main_menu(failed=True)

    def create_user_inputs(self):
        self.new_user['user_name'] = input('\nEnter the first and last name of the user: ')

        if len(self.new_user['user_name']) > 0:
            return self.create_pin()
        else:
            self.output({'error': 'please enter valid user name'})
            return self.create_user_inputs()

    def create_pin(self):
        self.new_user['pin'] = input('Create PIN: ')
        if len(self.new_user['pin']) > 0:
            return self.new_user
        else:
            self.output({'error': 'please enter valid PIN'})
            return self.create_pin()

    def create_account_inputs(self):
        self.new_acc['account_holder'] = input('User ID of account holder: ')
        return self.choose_account_inputs()

    def choose_account_inputs(self):
        print('\nWhat kind of account would you like to create?')
        print('------------------------')
        print('1 - Chequing Account')
        print('2 - Saving Account')
        account_type = input()

        self.new_acc['account_type'] = self._resolve_account_type(account_type)
        return self.initial_balance_input()

    def initial_balance_input(self):
        self.new_acc['initial_balance'] = input('Enter initial balance for account or press ENTER to skip: ')
        return self.new_acc

    def view_user_info_inputs(self):
        self.view_user_info_for = input('Enter the user ID you want to view info for: ')
        return self.view_user_info_for

    def view_acc_info_for_user_input(self):
        self.view_acc_info_for = input('Enter the user ID of the account holder: ')
        return self.view_acc_info_for

    def delete_cheq_acc_inputs(self):
        self.delete_cheq_acc_for = input('Enter the user ID of the account holder: ')
        return self.delete_cheq_acc_for

    def delete_sav_acc_inputs(self):
        self.delete_sav_acc_for = input('Enter the user ID of the account holder: ')
        return self.delete_sav_acc_for

    def delete_user_inputs(self):
        self.delete_user = input('Enter the ID for the user you want to delete: ')
        return self.delete_user

    @staticmethod
    def output(obj, msg=''):
        print(msg)
        for k, v in obj.items():
            print('{}: {}'.format(k.replace('_', ' ').upper(), v))

    def _resolve_account_type(self, num):
        if str(num) == '1':
            return 'chequing_account'
        elif str(num) == '2':
            return 'saving_account'
        else:
            self.output({'error': 'invalid account type'})
            self.choose_account_inputs()
