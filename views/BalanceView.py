import tkinter as tk

COMICFONT = "Comic Sans MS", 15
COMICSMALL = "Comic Sans MS", 10


class ViewBalance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.welcome = tk.Label(parent, text='Viewing your account balance', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.acc_balance = tk.Label(parent, text="Account Balance: ", font=COMICSMALL)
        self.acc_balance.grid(row=1, column=0)

        self.acc_amt = tk.Label(parent)
        self.acc_amt.grid(row=2, column=0)

        self.main_menu_btn = tk.Button(parent, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=8, column=0)

    def remove_main_frame(self):
        self.destroy()
        self.acc_balance.grid_remove()
        self.welcome.grid_remove()
        self.main_menu_btn.grid_remove()
