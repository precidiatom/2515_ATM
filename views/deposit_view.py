import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10


class ViewDeposit():
    def __init__(self, master):
        self.master = master

        self.overall_frame = tk.Frame(self.master)
        self.overall_frame.grid(row=0, column=0)

        self.welcome = tk.Label(self.overall_frame, text='Deposit Into Which Account?', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.current_balance = tk.Label(self.overall_frame)

        self.chequing_but = tk.Button(self.overall_frame, text="Chequing", font=COMICSMALL)
        self.chequing_value = tk.Label(self.overall_frame)

        self.savings_but = tk.Button(self.overall_frame, text="Savings", font=COMICSMALL)
        self.savings_value = tk.Label(self.overall_frame)

        self.main_menu_btn = tk.Button(self.overall_frame, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=9, column=0)

    def show_chequing(self):
        self.chequing_but.grid(row=2, column=0)
        self.chequing_value.grid(row=3, column=0)

    def show_saving(self):
        self.savings_but.grid(row=4, column=0)
        self.savings_value.grid(row=5, column=0)

    def show_current_balance(self, account_type, balance):
        self.current_balance.grid(row=1, column=0)
        self.current_balance.config(text='{} balance: {}'.format(account_type, balance))

    def remove_main_frame(self):
        self.destroy()
        self.chequing_but.grid_remove()
        self.savings_but.grid_remove()
        self.welcome.grid_remove()
        self.main_menu_btn.grid_remove()
