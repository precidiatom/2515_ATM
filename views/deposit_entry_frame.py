import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10

class ViewDepositInput:
    def __init__(self, master):
        """
        The view for the deposit input amount.

        Arg:
            master: the Deposit controller

        Author:
            Precidia Tom
        """
        self.overall_frame = master
        self.overall_frame = tk.Frame(self.overall_frame, bg="yellow")
        self.overall_frame.grid(row=0, column=0, padx=150, pady=75)

        self.top_frame = tk.Frame(self.overall_frame, bg="white")
        self.top_frame.grid(row=0, column=0, pady=15, padx=25)
        self.welcome = tk.Label(self.top_frame, text='Depositing into', font=COMICFONT)
        self.welcome.grid(row=0, column=0)
        self.welcome_account = tk.Label(self.top_frame, font=COMICFONT)
        self.welcome_account.grid(row=0, column=1)

        self.mid_frame = tk.Frame(self.overall_frame, bg="white")
        self.mid_frame.grid(row=2, column=0, padx=75, pady=25)
        self.display_balance = tk.Label(self.mid_frame, text="Your current balance is: ", font=COMICSMALL)
        self.display_balance.grid(row=2, column=0, padx=10, pady=25)
        self.current_balance = tk.Label(self.mid_frame, font=COMICSMALL)
        self.current_balance.grid(row=2, column=1, padx=10, pady=25)

        # Deposit input area
        self.deposit_label = tk.Label(self.mid_frame, text="Amount to Deposit:", font=COMICSMALL)
        self.deposit_label.grid(row=3, column=1)
        self.deposit_amt = tk.Entry(self.mid_frame, width=15)
        self.deposit_amt.grid(row=4, column=1)

        self.deposit_but = tk.Button(self.mid_frame, text="Deposit", font=COMICSMALL)
        self.deposit_but.grid(row=5, column=1, padx=5, pady=5)

        self.mainmenu = tk.Button(self.overall_frame, text="Return to Main Menu",
                                  font=COMICSMALL)
        self.mainmenu.grid(row=9, column=0, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    ViewDepositInput(root)
    tk.mainloop()
