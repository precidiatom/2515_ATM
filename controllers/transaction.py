class Transaction:

    def __init__(self, transaction_type, transaction_amount, transaction_date):
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date

    def get_transaction_str(self):
        return '{:30}{:20} @ {}'.format(self.transaction_type, self.transaction_amount, self.transaction_date)
