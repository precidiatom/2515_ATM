"""
    Author: Emile Zhang
"""

class Transaction:

    def __init__(self, transaction_type, transaction_amount, transaction_date):
        """
           The single transaction class. Each transaction object is a line of transaction in
           the transaction log.

        Args:
            transaction_type: which type of transaction
            transaction_amount: amount of transaction
            transaction_date: the date of the transaction
        """
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date

    def get_transaction_str(self):
        return '{:30}{:20} @ {}\n'.format(self.transaction_type, self.transaction_amount, self.transaction_date)
