from os import path
from shelve import open

BEGIN_TRANSACTION = "Transaction Log for "
NEW_ACCOUNT = "Initial balance "
POST_CHEQUE = "Posted cheque "
BOUNCED_CHEQUE = "Bounced cheque "
DEPOSIT = "Deposited "
WITHDRAW = "Withdrew "
PAY_INTEREST = "Interest "
CHARGE_OVERDRAFT = "Overdraft fee ",
CHARGE_MIN_BALANCE = "Below minimum balance fee "
NAME_CHANGE = "Changed name to "

data_abs_path = path.abspath(path.dirname(__file__) + '\\..\\data')
app_data = open(data_abs_path + '\\appdata.db')