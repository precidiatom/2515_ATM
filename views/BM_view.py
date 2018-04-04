class CommandInterface:

    def __init__(self):
        self.teller_id = input('Teller ID: ')
        self.teller_password = input('Password: ')
        self.new_acc = {}
        self.view_logs_for = None

    def main_menu(self):
        print('MAIN MENU')
        print('------------------------')
        print('1 - Create an account')
        print('2 - View logs for an account')

        action = input()

        if action == '1':
            self.create_account_inputs()
        elif action == '2':
            self.view_logs_inputs()

    def create_account_inputs(self):
        print('What kind of account would you like to create?')
        print('------------------------')
        print('1 - Chequing Account')
        print('2 - Saving Account')
        print('3 - Term Saving Account')
        account_type = input()
        self.new_acc['account_type'] = CommandInterface._resolve_account_type(account_type)

        self.new_acc['account_holder'] = input('Name of account holder: ')

    def view_logs_inputs(self):
        self.view_logs_for = input('Enter the account number you want to view logs for: ')

    @staticmethod
    def _resolve_account_type(id):
        if str(id) == '1':
            return 'chequing'
        elif str(id) == '2':
            return 'saving'
        elif str(id) == '3':
            return 'term_saving'
