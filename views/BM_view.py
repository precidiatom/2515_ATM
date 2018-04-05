class CommandInterface:

    def __init__(self):
        self.teller_id = input('Teller ID: ')
        self.teller_pin = input('PIN: ')
        self.new_acc = {}
        self.new_user = {}
        self.view_logs_for = None

    def main_menu(self):
        print('\nMAIN MENU')
        print('------------------------')
        print('1 - Create an user')
        print('2 - Create an account for an user')
        print('3 - View logs for an account')

        action = input()

        if action == '1':
            self.create_user_inputs()
        elif action == '2':
            self.create_account_inputs()
        elif action == '3':
            self.view_logs_inputs()

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

    def view_logs_inputs(self):
        self.view_logs_for = input('Enter the account number you want to view logs for: ')

    @staticmethod
    def _resolve_account_type(num):
        if str(num) == '1':
            return 'chequing'
        elif str(num) == '2':
            return 'saving'
        elif str(num) == '3':
            return 'term_saving'
