"""
    Author: Emile Zhang
"""

from os import path

BEGIN_TRANSACTION = "Transaction Log for "
NEW_ACCOUNT = "Initial balance "
DEPOSIT = "Deposited "
WITHDRAW = "Withdrew "

data_abs_path = path.abspath(path.dirname(__file__) + '\\..\\data')
