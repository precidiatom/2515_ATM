from models.account import Account
from models.constants import *


class ChequingAccount(Account):
    __OVERDRAFT_AMOUNT = 500
    __INTEREST = float(-1 * 0.03)
    __OVEDRAFT_FEE = float(10.00)

    def __init__(self, user, balance=0.0):
        super().__init__(user, 'Chequing Account', balance, ChequingAccount.__OVEDRAFT_FEE, ChequingAccount.__INTEREST)

    def post_cheque(self, amount):
        if self.balance - amount < ChequingAccount.__OVERDRAFT_AMOUNT:
            super().charge_fee(BOUNCED_CHEQUE, ChequingAccount.__OVEDRAFT_FEE)
        else:
            self.balance -= amount
            self.transaction_log.add_transaction(POST_CHEQUE, -1 * amount)

    def pay_interest(self):
        if self.balance < ChequingAccount.__OVERDRAFT_AMOUNT:
            super().pay_interest()

    def withdraw(self, amount):
        if (self.balance - amount) < -1 * ChequingAccount.__OVERDRAFT_AMOUNT:
            print("Insufficient funds. Remaining balance:", self.balance)
        else:
            super().withdraw(amount)
            self.pay_interest()
