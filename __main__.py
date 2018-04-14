from tkinter import *

from controllers.BM_controller import BMController
from controllers.frame_controller import FrameController
from models.user import User

if __name__ == "__main__":
    user = User(userid='a0101', user_name='Meow', pin=1234, user_type='teller')
    controller = BMController()

    root = Tk()
    new_frame_controller = FrameController(root)
    mainloop()
