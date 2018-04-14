"""
    Author: Emile Zhang
"""

import datetime

from models.constants import *
from models.transaction import Transaction


class TransactionLog:

    def __init__(self, account, init_balance=0):
        """
           The class for transaction logs. A transaction log object is a full transaction log for an account

        Args:
            account: the account the transaction log is for
            init_balance: when creating a new transaction log, the initial balance of the account
        """
        self.account = account
        self.transactions = [
            Transaction(NEW_ACCOUNT, '$' + str(init_balance), datetime.datetime.now())]

    @staticmethod
    def add_transaction(account, transaction_type, amount):
        """
        Add a transaction to the transaction log
        Args:
            account: the account the transaction is for
            transaction_type:  the type of transaction
            amount: the amount of the transaction

        Returns:

        """
        new_transaction = Transaction(transaction_type, '$%.2f' % amount, datetime.datetime.now())
        account.transaction_log += new_transaction.get_transaction_str()
