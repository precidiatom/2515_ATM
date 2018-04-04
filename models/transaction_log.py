import datetime

from models.transaction import Transaction
from models.transaction_types import *


class TransactionLog:

    def __init__(self, account, init_balance):
        self.account = account
        self.transactions = [
            Transaction(NEW_ACCOUNT, '$' + str(init_balance), datetime.datetime.now())]

    def add_transaction(self, transaction_type, amount):
        new_transaction = Transaction(transaction_type, '$%.2f' % amount, datetime.datetime.now())
        self.transactions.append(new_transaction)
        self.account.acc_file['transaction_log'] += new_transaction.get_transaction_str()
        self.account.acc_file['balance'] = self.account.balance
