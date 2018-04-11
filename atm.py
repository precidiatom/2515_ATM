from tkinter import *

from controllers.login_controller import LoginController
from models.user import User

if __name__ == "__main__":
    root = Tk()
    account_db = User('Meow', 1234, 'teller')
    # atm_controller = MainController(root, account_db)
    # atm_controller.set_main_window()
    login_controller = LoginController(root, account_db)
    login_controller.set_main_window()
    mainloop()
