from tkinter import *

from controllers.MainController import MainController
from models.account import Account

if __name__ == "__main__":
    root = Tk()
    account_db = Account('a0101')
    atm_controller = MainController(root, account_db)
    atm_controller.set_main_window()
    mainloop()
