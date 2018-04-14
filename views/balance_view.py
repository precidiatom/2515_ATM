import tkinter as tk

COMICFONT = "Comic Sans MS", 15
COMICSMALL = "Comic Sans MS", 10


class ViewBalance():
    def __init__(self, master):
        # super().__init__(master)
        self.master = master

        self.overall_frame = tk.Frame(self.master, bg="pink")
        self.overall_frame.grid(row=0, column=0, padx=100, pady=125)

        self.top_frame = tk.Frame(self.overall_frame)
        self.top_frame.grid(row=0, column=0, padx=5, pady=5)
        self.welcome = tk.Label(self.top_frame, text='Viewing your account balance', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.mid_frame = tk.Frame(self.overall_frame, bg="white")
        self.mid_frame.grid(row=1, column=0, padx=10, pady=10)
        self.acc_balance = tk.Label(self.mid_frame, text="Account Balance: $", font=COMICSMALL)
        self.acc_balance.grid(row=1, column=0, padx=100, pady=10)

        self.chq_acc_amt = tk.Label(self.mid_frame)
        self.chq_acc_amt.grid(row=2, column=0)

        self.sav_acc_amt = tk.Label(self.mid_frame)
        self.sav_acc_amt.grid(row=3, column=0)

        self.main_menu_btn = tk.Button(self.overall_frame, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=8, column=0)

    def show_balance(self, balance, account_type):
        if account_type == 'chequing_account':
            self.chq_acc_amt.config(text='Chequing Account: $' + str(balance))
        elif account_type == 'saving_account':
            self.sav_acc_amt.config(text='Saving Account: $' + str(balance))
