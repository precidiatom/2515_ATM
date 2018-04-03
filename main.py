from tkinter import *

from controllers import ATM_controller

if __name__ == "__main__":
    root = Tk()
    ATM_controller.MainWindow(root)
    mainloop()
