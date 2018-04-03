from controllers.account import Account
from models.transaction_types import *


class SavingAccount(Account):
    __INTEREST = 0.02
    __MINIMUM_BALANCE_FEE = 10.00
    __MINIMUM_BALANCE = 1000

    def __init__(self, holder, balance=0.0):
        super().__init__(holder, balance, SavingAccount.__MINIMUM_BALANCE_FEE, SavingAccount.__INTEREST)

    def pay_interest(self):
        if self.balance >= SavingAccount.__MINIMUM_BALANCE:
            super().pay_interest()

    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < SavingAccount.__MINIMUM_BALANCE:
            super().charge_fee(CHARGE_MIN_BALANCE, SavingAccount.__MINIMUM_BALANCE_FEE)
