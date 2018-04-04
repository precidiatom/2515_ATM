class CommandInterface:

    def __init__(self):
        pass

    def print_main_menu():
        print('MAIN MENU')
        print('------------------------')
        print('1 - Create an account')

    def get_inputs(self):
        account_type = input('What kind of account would you like to create?')
        account_holder = input('Name of account holder: ')
        initial_balance = input('Initial balance: ')
