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
        self.delete_acc_for = None
        self.delete_account = None

    def main_menu(self):
        print('\nMAIN MENU')
        print('------------------------')
        print('1 - Create a user')
        print('2 - Create an account for an user\n')
        print('3 - View info for a user')
        print('4 - View info for an account')
        print('5 - View transaction logs for an account\n')
        print('6 - Delete a user')
        print('7 - Delete an account')

        action = input()

        if action == '1':
            # self.create_user_inputs()
            return True
        elif action == '2':
            self.create_account_inputs()
            return True
        elif action == '3':
            self.view_user_info_inputs()
            return True
        elif action == '4' or action == '5':
            self.view_acc_info_inputs(action)
            return True
        elif action == '6':
            self.delete_user_inputs()
            return True
        elif action == '7':
            self.delete_acc_inputs()
            return True
        else:
            self.output({'Error': 'please choose from available actions'}, '\n[ Invalid Input ]')
            return False

    def create_user_inputs(self):
        self.new_user['user_name'] = input('\nEnter the name of the user: ')
        if len(self.new_user['user_name']) <= 0:
            self.output({'error': 'please enter valid user name'})
            return False
        else:
            return True

    def create_account_inputs(self):
        self.new_acc['account_holder'] = input('User ID of account holder: ')
        self.choose_account_inputs()

    def choose_account_inputs(self):
        print('\nWhat kind of account would you like to create?')
        print('------------------------')
        print('1 - Chequing Account')
        print('2 - Saving Account')
        print('3 - Term Saving Account')
        account_type = input()
        self.new_acc['account_type'] = CommandInterface._resolve_account_type(account_type)
        self.create_pin(self.new_acc)

    def create_pin(self, obj):
        if obj == 'user':
            obj = self.new_user
        elif obj == 'acc':
            obj = self.new_acc

        obj['pin'] = input('\nCreate PIN: ')
        if len(obj['pin']) <= 0:
            self.output({'error': 'please enter valid PIN'})
            return False
        else:
            return True

    def view_user_info_inputs(self):
        self.view_user_info_for = input('Enter the user ID you want to view info for: ')

    def view_acc_info_inputs(self, action):
        self.view_acc_info_for = input('Enter the user ID of the account holder: ')
        self.view_acc_num = input('Enter the account number you want to view the info for: ')
        self.view_logs_for = self.view_acc_info_for if action == '5' else None

    def delete_acc_inputs(self):
        self.delete_acc_for = input('Enter the user ID of the account holder: ')
        self.delete_account = input('Enter the account number you want to delete: ')

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
