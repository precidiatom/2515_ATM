from glob import glob
from os import remove
from random import choice

from models.constants import *
from models.transaction_log import TransactionLog
from models.user import User
from observer import Observer


class Account(Observer):
    def __init__(self, userid, account_type='Default', balance=0.0, fee=0.0, interest=0.0):
        super().__init__()

        self.balance = float(balance)

        self.user = User.get_persist_user_obj(userid)
        self.account_number = app_data['NEXT_ACC_NUM']
        self.fee = float(fee)
        self.interest = float(interest)
        self.transaction_log = TransactionLog(self, balance)

        self.acc_file = Account.get_persist_account(userid, self.account_number)
        self.acc_file['holder_name'] = self.user['user_name']
        self.acc_file['account_num'] = self.account_number
        self.acc_file['account_type'] = account_type
        self.acc_file['balance'] = self.balance

        self.acc_file['transaction_log'] = '\n[Transacton log for ' + self.user['user_name'] + ' #' + str(
            self.account_number) + ']' + '\n'
        self.acc_file[
            'transaction_log'] += '-------------------------------------------------------------------------------\n'
        self.acc_file['transaction_log'] += self.transaction_log.transactions[0].get_transaction_str()

        app_data['NEXT_ACC_NUM'] = ''.join(choice('0123456789') for i in range(4))

    @staticmethod
    def get_persist_account(userid, acc_number):
        return open(data_abs_path + '\\' + str(userid) + str(acc_number) + '.db')

    @staticmethod
    def delete_account(userid, acc_number):
        for acc_file in glob(data_abs_path + '\\' + str(userid) + str(acc_number) + '.db.*'):
            remove(acc_file)

    @staticmethod
    def login(acc_num, pin):
        return Account.get_persist_account(acc_num)['pin'] == pin

    def get_info(self):
        return {
            "account_holder": self.user['user_name'],
            "account_number": self.account_number,
            "account_type": self.acc_file['account_type'],
            "balance": "$" + str(self.balance)
        }

    def deposit(self, amount):
        if amount <= 0:
            print("inappropriate data")
        else:
            self.balance += amount
            self.transaction_log.add_transaction(DEPOSIT, amount)

    def get_balance(self):
        return self.balance

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

    def charge_fee(self, fee_type, fee_amount):
        self.balance -= self.fee
        self.transaction_log.add_transaction(fee_type, -1 * fee_amount)

    def pay_interest(self):
        interest_fee = abs(self.balance) * self.interest
        self.balance += interest_fee
        self.transaction_log.add_transaction(PAY_INTEREST, interest_fee)

    def change_name(self, new_name):
        self.user = new_name
