import datetime

from controllers.transaction import Transaction
from models.transaction_types import *


class TransactionLog:

    def __init__(self, account, init_balance):
        self.account = account
        self.transactions = [
            Transaction(NEW_ACCOUNT, '$' + str(init_balance), datetime.datetime.now())]

    def add_transaction(self, transaction_type, amount):
        self.transactions.append(Transaction(transaction_type, '$%.2f' % amount, datetime.datetime.now()))
