from random import choice

from models.constants import *
from models.transaction_log import TransactionLog
from models.user import User


class Account:
    def __init__(self, userid, account_type='Default', balance=0.0):
        self.balance = float(balance)
        self.account_type = account_type

        self.user = dict(User.get_persist_user_obj(userid))
        self.account_number = app_data['NEXT_ACC_NUM']

        account_type = account_type.lower().replace(' ', '_')
        self.user[account_type] = {
            'account_num': self.account_number,
            'balance': self.balance,
            'transaction_log': '\n[Transacton log for {} {} #{}]\n'.format(self.user['user_name'], self.account_type,
                                                                           self.account_number)
        }

        self.transaction_log = TransactionLog(self.user[account_type], balance)

        self.user[account_type][
            'transaction_log'] += '-------------------------------------------------------------------------------\n'
        self.user[account_type]['transaction_log'] += self.transaction_log.transactions[0].get_transaction_str()
        self.user[account_type][
            'transaction_log'] += '\n-------------------------------------------------------------------------------\n'

        app_data['NEXT_ACC_NUM'] = ''.join(choice('0123456789') for i in range(4))

        User.get_persist_user_obj(userid).update(self.user)

    @staticmethod
    def delete_account(userid, acc_type):
        if User.check_valid_user(userid) and acc_type in User.get_persist_user_obj(userid).keys():
            del User.get_persist_user_obj(userid)[acc_type]
            return True
        else:
            return False

    @staticmethod
    def get_account_info_for_user(userid):
        results = {}
        for k in User.get_persist_user_obj(userid).keys():
            if 'account' in k:
                results[k] = User.get_persist_user_obj(userid)[k]
        return results

    def get_info(self):
        return {
            "account_holder": self.user['user_name'],
            "account_number": self.account_number,
            "account_type": self.account_type,
            "balance": "$" + str(self.balance)
        }

    def deposit(self, amount):
        if amount <= 0:
            print("inappropriate data")
        else:
            self.balance += amount
            self.transaction_log.add_transaction(DEPOSIT, amount)

    @staticmethod
    def get_balance(userid, acc):
        return User.get_persist_user_obj(userid)[acc]['balance']

    def show_transaction_log(self):
        transaction_log = ['[Transacton log for ' + self.user['user_name'] + ' #' + str(self.account_number) + ']',
                           '-------------------------------------------------------------------------------']
        transaction_log.extend([transaction.get_transaction_str() for transaction in self.transaction_log.transactions])
        transaction_log.append('\n')
        return transaction_log

    def withdraw(self, amount):
        if amount <= 0:
            print("inappropriate data")
        else:
            self.balance -= amount
            self.transaction_log.add_transaction(WITHDRAW, -1 * amount)

    def change_name(self, new_name):
        self.user = new_name
