from tkinter import *

from controllers.frame_controller import FrameController
from models.account import Account
from models.user import User

if __name__ == "__main__":
    user = User(userid='b9090', user_name='Hello Kitty', pin=1234, user_type='customer')
    account = Account(userid=user.user_id, balance=1000.00, account_type='saving_account')
    account = Account(userid=user.user_id, balance=500.00, account_type='chequing_account')

    root = Tk()
    new_frame_controller = FrameController(root)
    mainloop()
