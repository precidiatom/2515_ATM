from tkinter import *

from controllers.main_controller import MainController
from controllers.login_controller import LoginController
from models.account import Account

if __name__ == "__main__":
    root = Tk()
    account_db = Account('a0101')
    # atm_controller = MainController(root, account_db)
    # atm_controller.set_main_window()
    login_controller = LoginController(root, account_db)
    login_controller.set_main_window()
    mainloop()
