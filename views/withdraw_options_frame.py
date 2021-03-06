import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10

class ViewWithdrawOptions:
    def __init__(self, master):
        """
        Displays the screen with all the withdraw options as well as customized amounts

        Arg:
            master: the Withdraw controller

        Authors:
            Precidia Tom
            Emilie Zhang
        """
        self.master = master
        self.overall_frame = tk.Frame(self.master, bg="palegreen")
        self.overall_frame.grid(row=0, column=0, padx=150, pady=85)

        self.top_frame = tk.Frame(self.overall_frame, bg="white")
        self.top_frame.grid(row=0, column=0, padx=25, pady=15)
        self.welcome = tk.Label(self.top_frame, text='Withdrawing from', font=COMICFONT, padx=10, pady=10)
        self.welcome.grid(row=0, column=0)
        self.welcome_account = tk.Label(self.top_frame, font=COMICFONT)
        self.welcome_account.grid(row=0, column=1, sticky="W")

        self.mid_frame = tk.Frame(self.overall_frame, bg="white")
        self.mid_frame.grid(row=1, column=0, padx=85, pady=25)

        self.display_balance = tk.Label(self.mid_frame, text="Your current balance is: ", font=COMICSMALL)
        self.display_balance = tk.Label(self.mid_frame, font=COMICSMALL)
        self.display_balance.grid(row=1, column=0, padx=10, pady=25)

        self.current_balance = tk.Label(self.mid_frame, font=COMICSMALL)
        self.current_balance.grid(row=1, column=1, padx=10, pady=25)

        self.minus_20 = tk.Button(self.mid_frame, text="$20", font=COMICSMALL)
        self.minus_20.grid(row=2, column=0)

        self.minus_40 = tk.Button(self.mid_frame, text="$40", font=COMICSMALL)
        self.minus_40.grid(row=3, column=0)

        self.minus_60 = tk.Button(self.mid_frame, text="$60", font=COMICSMALL)
        self.minus_60.grid(row=4, column=0)

        self.minus_80 = tk.Button(self.mid_frame, text="$80", font=COMICSMALL)
        self.minus_80.grid(row=2, column=2)

        self.minus_100 = tk.Button(self.mid_frame, text="$100", font=COMICSMALL)
        self.minus_100.grid(row=3, column=2)

        self.minus_other = tk.Button(self.mid_frame, text="Custom amount (click here): ", font=COMICSMALL)
        self.minus_other_input = tk.Entry(self.mid_frame, width=8)
        self.minus_other.grid(row=4, column=1, sticky="E")
        self.minus_other_input.grid(row=4, column=2, sticky="W")

        self.mainmenu = tk.Button(self.overall_frame, text="Return to Menu",
                                  font=COMICSMALL)
        self.mainmenu.grid(row=10, column=0, pady=10)

    def get_other_amount(self):
        """
        Retrieves custom user input

        Returns:
            the manual user input in the Custom amount box
        """
        return self.minus_other_input.get()


if __name__ == "__main__":
    root = tk.Tk()
    ViewWithdrawOptions(root)
    tk.mainloop()