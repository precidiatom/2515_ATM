import tkinter as tk
from tkinter import messagebox

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10


class ViewWithdraw:
    def __init__(self, master):
        """
         Displays the screen of the Withdraw page, displays account balance(s).

        Arg:
            master: the Withdraw controller

        Authors:
            Precidia Tom
            Emilie Zhang
        """
        self.master = master
        self.overall_frame = tk.Frame(self.master, bg="palegreen")
        self.overall_frame.grid(row=0, column=0, padx=150, pady=75)

        self.top_frame = tk.Frame(self.overall_frame, bg="white")
        self.top_frame.grid(row=0, column=0, pady=10, padx=10)
        self.welcome = tk.Label(self.top_frame, text='Withdraw From Which Account?', font=COMICFONT)
        self.welcome.grid(row=0, column=0, padx=20, pady=20)

        self.chq_balance = tk.Label(self.top_frame)
        self.sav_balance = tk.Label(self.top_frame)

        self.chequing_but = tk.Button(self.overall_frame, text="Chequing", font=COMICSMALL)
        self.savings_but = tk.Button(self.overall_frame, text="Savings", font=COMICSMALL)

        self.main_menu_btn = tk.Button(self.overall_frame, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=7, column=0)

    def show_chequing(self):
        """
        Places the chequing button on page if user has chequing account
        """
        self.chequing_but.grid(row=2, column=0, padx=2, pady=2)

    def show_saving(self):
        """
        Places the saving button on page if user has saving account
        """
        self.savings_but.grid(row=5, column=0, padx=2, pady=2)

    def show_sav_balance(self, balance):
        """
        Places the savings button on page if user has a savings account

        Arg:
            balance: the saving account balance
        """
        self.sav_balance.grid(row=4, column=0)
        self.sav_balance.config(text='Saving balance: {}'.format(balance))

    def show_chq_balance(self, balance):
        """
        Places the chequing button on page if user has chequing account

        Arg:
            balance: the chequing account balance
        """
        self.chq_balance.grid(row=1, column=0)
        self.chq_balance.config(text='Chequing balance: {}'.format(balance))

    def show_msg_box(self, title, msg):
        """
        Places an error pop message box on the screen.

        Arg:
            title: the title of the message box
            msg: the message inside the message box
        """
        messagebox.showerror(title, msg)
