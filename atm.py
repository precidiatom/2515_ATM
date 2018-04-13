from tkinter import *

from controllers.login_controller import LoginController
from models.user import User

if __name__ == "__main__":
    root = Tk()
    account_db = user = User(user_name='Meow', pin=1234, user_type='teller')
    # atm_controller = MainController(root, account_db)
    # atm_controller.set_main_window()
    login_controller = LoginController(root)
    login_controller.set_main_window()
    mainloop()
