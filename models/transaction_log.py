import datetime

from models.constants import *
from models.transaction import Transaction


class TransactionLog:

    def __init__(self, account, init_balance):
        self.account = account
        self.transactions = [
            Transaction(NEW_ACCOUNT, '$' + str(init_balance), datetime.datetime.now())]

    @staticmethod
    def add_transaction(account, transaction_type, amount):
        new_transaction = Transaction(transaction_type, '$%.2f' % amount, datetime.datetime.now())
        account.transaction_log += new_transaction.get_transaction_str()
