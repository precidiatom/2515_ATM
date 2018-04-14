import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10

class ViewDeposit():
    def __init__(self, master):
        self.master = master

        self.overall_frame = tk.Frame(self.master, bg="yellow")
        self.overall_frame.grid(row=0, column=0, padx=150, pady=75)

        self.top_frame = tk.Frame(self.overall_frame, bg="white")
        self.top_frame.grid(row=0, column=0, pady=10, padx=10)
        self.welcome = tk.Label(self.top_frame, text='Deposit Into Which Account?', font=COMICFONT)
        self.welcome.grid(row=0, column=0, padx=20, pady=20)

        self.chq_balance = tk.Label(self.top_frame)
        self.sav_balance = tk.Label(self.top_frame)

        self.chequing_but = tk.Button(self.overall_frame, text="Chequing", font=COMICSMALL)
        self.chq_balance = tk.Label(self.overall_frame)

        self.savings_but = tk.Button(self.overall_frame, text="Savings", font=COMICSMALL)
        self.sav_balance = tk.Label(self.overall_frame)

        self.main_menu_btn = tk.Button(self.overall_frame, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=9, column=0, padx=50, pady=10)

    def show_chequing(self):
        self.chequing_but.grid(row=2, column=0)
        self.chq_balance.grid(row=3, column=0, padx=2, pady=2)

    def show_chq_balance(self, balance):
        self.chq_balance.grid(row=1, column=0)
        self.chq_balance.config(text='chequing balance: {}'.format(balance))

    def show_saving(self):
        self.savings_but.grid(row=5, column=0)
        self.sav_balance.grid(row=6, column=0, padx=2, pady=2)

    def show_sav_balance(self, balance):
        self.sav_balance.grid(row=4, column=0)
        self.sav_balance.config(text='saving balance: {}'.format(balance))
