from models.transaction_log import TransactionLog
from models.transaction_types import *

from observer import Observable


class Account(Observable):
    __NEXT_ACCT_NUM = 9000

    def __init__(self, holder, balance=0.0, fee=0.0, interest=0.0):
        super().__init__()

        self.balance = float(balance)
        self.holder = holder
        self.account_number = Account.__NEXT_ACCT_NUM
        self.fee = float(fee)
        self.interest = float(interest)
        self.transaction_log = TransactionLog(self, balance)

        Account.__NEXT_ACCT_NUM += 1

    def get_info(self):
        return {
            "name": self.holder,
            "account_number": self.account_number,
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
        transaction_log = ['[Transacton log for ' + self.holder + ' #' + str(self.account_number) + ']',
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
        self.holder = new_name
