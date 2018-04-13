import tkinter as tk

COMICFONT = "Comic Sans MS", 15
COMICSMALL = "Comic Sans MS", 10


class ViewBalance():
    def __init__(self, master):
        # super().__init__(master)
        self.master = master

        self.overall_frame = tk.Frame(self.master)
        self.overall_frame.grid(row=0, column=0)

        self.welcome = tk.Label(self.overall_frame, text='Viewing your account balance', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.acc_balance = tk.Label(self.overall_frame, text="Account Balance: ", font=COMICSMALL)
        self.acc_balance.grid(row=1, column=0)

        self.chq_acc_amt = tk.Label(self.overall_frame)
        self.chq_acc_amt.grid(row=2, column=0)

        self.sav_acc_amt = tk.Label(self.overall_frame)
        self.sav_acc_amt.grid(row=2, column=0)

        self.main_menu_btn = tk.Button(self.overall_frame, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=8, column=0)

    def remove_main_frame(self):
        self.destroy()
        self.acc_balance.grid_remove()
        self.chq_acc_amt.grid_remove()
        self.sav_acc_amt.grid_remove()
        self.welcome.grid_remove()
        self.main_menu_btn.grid_remove()

    def show_balance(self, balance, account_type):
        print(balance, account_type)
        if account_type == 'chequing_account':
            print('meow moew moew')
            self.chq_acc_amt.config(text='Chequing Account: $' + str(balance))
        elif account_type == 'saving_account':
            self.sav_acc_amt.config(text='Saving Account: $' + str(balance))
