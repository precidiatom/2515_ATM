"""
    Author: Emile Zhang
"""

from random import choice

from models.constants import *
from models.transaction_log import TransactionLog
from models.user import User


class Account:
    def __init__(self, userid, account_type, balance=0.0):
        """
        The class that handles all actions regarding an account. Init will create a new account if
        it does not already exist for a user, or fetch the account from persisted objects.

        Args:
            userid: the id of the user that the account is for
            account_type: the type of the account
            balance: the initial balance of this account (only used for new accounts)
        """
        self.user = User(userid)

        # If user already has this type of account, get it from persisted object
        if account_type in self.user.accounts:
            self.balance = self.user.accounts[account_type]['balance']
            self.account_number = self.user.accounts[account_type]['account_num']
            self.account_type = account_type
            self.transaction_log = self.user.accounts[account_type]['transaction_log']
        # create a new account if it does not already exist
        else:
            self.balance = float(balance)
            self.account_number = ''.join(choice('0123456789') for i in range(4))
            self.account_type = account_type.lower().replace(' ', '_')
            self.user.accounts[self.account_type] = {
                'account_num': self.account_number,
                'balance': self.balance,
                'transaction_log': '\n[Transacton log for {} {} #{}]\n'.format(self.user.user_name, account_type,
                                                                               self.account_number)
            }

            self.transaction_log = TransactionLog(self.account_type, balance)

            self.user.accounts[account_type][
                'transaction_log'] += '-------------------------------------------------------------------------------\n'
            self.user.accounts[account_type]['transaction_log'] += self.transaction_log.transactions[
                0].get_transaction_str()
            self.user.accounts[account_type][
                'transaction_log'] += '\n-------------------------------------------------------------------------------\n'

            self.user.update_user_data()

    # Updates the persisted object of the account
    def update_acc_data(self):
        self.user.accounts[self.account_type]['balance'] = self.balance
        self.user.accounts[self.account_type]['transaction_log'] = self.transaction_log
        self.user.update_user_data()

    def delete_account(self):
        del self.user.accounts[self.account_type]
        self.user.update_user_data()
        return True

    def get_info(self):
        return {
            "account_holder": self.user.user_name,
            "account_number": self.account_number,
            "account_type": self.account_type,
            "balance": "$" + str(self.balance)
        }

    def deposit(self, amount):
        self.balance += float(amount)
        TransactionLog.add_transaction(self, DEPOSIT, amount)
        self.update_acc_data()

    def withdraw(self, amount):
        if self.balance < float(amount):
            return False
        else:
            self.balance -= amount
            TransactionLog.add_transaction(self, WITHDRAW, -1 * amount)
            self.update_acc_data()
            return True
