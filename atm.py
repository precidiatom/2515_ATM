from tkinter import *

from controllers.ATM_controller import ATMController
from models.account import Account

if __name__ == "__main__":
    root = Tk()
    account_db = Account('a0101')
    atm_controller = ATMController(root, account_db)
    atm_controller.set_main_window()
    mainloop()
