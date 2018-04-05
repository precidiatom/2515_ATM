class CommandInterface:

    def __init__(self):
        self.teller_id = input('Teller ID: ')
        self.teller_pin = input('PIN: ')
        self.new_acc = {}
        self.new_user = {}
        self.view_logs_for = None
        self.view_user_info_for = None
        self.view_acc_info_for = None
        self.view_acc_num = None
        self.delete_user = None
        self.delete_accout = None

    def main_menu(self):
        print('\nMAIN MENU')
        print('------------------------')
        print('1 - Create a user')
        print('2 - Create an account for an user\n')
        print('3 - View info for a user')
        print('4 - View info for an account\n')
        print('5 - Delete a user')
        print('6 - Delete an account')

        action = input()

        if action == '1':
            self.create_user_inputs()
        elif action == '2':
            self.create_account_inputs()
        elif action == '3':
            self.view_user_info_inputs()
        elif action == '4':
            self.view_acc_info_inputs()
        elif action == '5':
            self.delete_user_inputs()
        elif action == '6':
            self.delete_acc_inputs()

    def create_user_inputs(self):
        self.new_user['user_name'] = input('\nEnter the name of the user: ')
        self.new_user['pin'] = input('Create PIN for the user: ')

    def create_account_inputs(self):
        self.new_acc['account_holder'] = input('User ID of account holder: ')

        print('\nWhat kind of account would you like to create?')
        print('------------------------')
        print('1 - Chequing Account')
        print('2 - Saving Account')
        print('3 - Term Saving Account')
        account_type = input()
        self.new_acc['account_type'] = CommandInterface._resolve_account_type(account_type)
        self.new_acc['pin'] = input('\nCreate account PIN: ')

    def view_user_info_inputs(self):
        self.view_user_info_for = input('Enter the user ID you want to view info for: ')

    def view_acc_info_inputs(self):
        self.view_acc_info_for = input('Enter the user ID of the account holder: ')
        self.view_acc_num = input('Enter the account number you want to view the info for: ')

    def delete_acc_inputs(self):
        pass

    def delete_user_inputs(self):
        self.delete_user = input('Enter the ID for the user you want to delete: ')

    @staticmethod
    def output(obj, msg=''):
        print(msg)
        for k, v in obj.items():
            print('{}: {}'.format(k.replace('_', ' ').upper(), v))

    @staticmethod
    def _resolve_account_type(num):
        if str(num) == '1':
            return 'chequing'
        elif str(num) == '2':
            return 'saving'
        elif str(num) == '3':
            return 'term_saving'
