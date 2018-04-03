from tkinter import *

from controllers.ATM_controller import ATMController
from models.account import Account

if __name__ == "__main__":
    root = Tk()
    account_db = Account('Merp', 1000)
    ATMController(root, account_db)
    mainloop()
