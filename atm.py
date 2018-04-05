from tkinter import *

from controllers.ATM_controller import ATMController
from models.account import Account

if __name__ == "__main__":
    root = Tk()
    account_db = Account('a0101')
    ATMController(root, account_db)
    mainloop()
