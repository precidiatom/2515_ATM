import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10


class ViewDepositInput():
    def __init__(self):
        self.window = tk.Toplevel()

        self.overall_frame = tk.Frame(self.window)
        self.overall_frame.grid(row=0, column=0)
        self.welcome = tk.Label(self.overall_frame, text='Depositing into', font=COMICFONT)
        self.welcome.grid(row=0, column=0)
        self.welcome_account = tk.Label(self.overall_frame, font=COMICFONT)
        self.welcome_account.grid(row=0,column=1)

        self.display_balance = tk.Label(self.overall_frame, text="Your current balance is: ", font=COMICSMALL)
        self.display_balance.grid(row=1, column=0)
        self.current_balance = tk.Label(self.overall_frame, font=COMICSMALL)
        self.current_balance.grid(row=1, column=1)

        self.deposit_label = tk.Label(self.overall_frame, text="Amount to Deposit:", font=COMICSMALL)
        self.deposit_label.grid(row=2, column=1)
        self.deposit_amt = tk.Entry(self.overall_frame, width=15)
        self.deposit_amt.grid(row=3, column=1)

        self.deposit_but = tk.Button(self.overall_frame, text="Deposit", font=COMICSMALL)
        self.deposit_but.grid(row=4, column=1)

        self.mainmenu = tk.Button(self.overall_frame, text="Cancel Transaction. \n Return to Main Menu",
                                  font=COMICSMALL)
        self.mainmenu.grid(row=9, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    ViewDepositInput()
    tk.mainloop()
