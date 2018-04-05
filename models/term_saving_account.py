import datetime

from models.saving_account import SavingAccount


class TermSavingAccount(SavingAccount):

    def __init__(self, userid, balance=0.0):
        super().__init__(userid, balance)
        self.acc_file['account_type'] = 'Term Saving Account'
        self.last_deposit_date = datetime.datetime.now()

    def withdraw(self, amount):
        if (datetime.datetime.now() - self.last_deposit_date).days >= 60:
            super().withdraw(amount)
        else:
            print("Less than 60 days since last deposit. Cannot withdraw")

    def deposit(self, amount):
        super().deposit(amount)
        self.last_deposit_date = datetime.datetime.now()
