import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10


class ViewWithdrawOptions():
    def __init__(self):
        self.window = tk.Toplevel()

        self.overall_frame = tk.Frame(self.window)
        self.overall_frame.grid(row=0, column=0)

        self.welcome = tk.Label(self.overall_frame, text='Withdrawing from', font=COMICFONT)
        self.welcome.grid(row=0, column=0)
        self.welcome_account = tk.Label(self.overall_frame, font=COMICFONT)
        self.welcome_account.grid(row=0, column=1)

        self.display_balance = tk.Label(self.overall_frame, text="Your current balance is: ", font=COMICSMALL)
        self.display_balance.grid(row=1, column=0)
        self.current_balance = tk.Label(self.overall_frame, font=COMICSMALL)
        self.current_balance.grid(row=1, column=1)


        self.minus_20 = tk.Button(self.overall_frame, text="$20", font=COMICSMALL)
        self.minus_20.grid(row=2, column=0)

        self.minus_40 = tk.Button(self.overall_frame, text="$40", font=COMICSMALL)
        self.minus_40.grid(row=3, column=0)

        self.minus_60 = tk.Button(self.overall_frame, text="$60", font=COMICSMALL)
        self.minus_60.grid(row=4, column=0)

        self.minus_80 = tk.Button(self.overall_frame, text="$80", font=COMICSMALL)
        self.minus_80.grid(row=2, column=2)

        self.minus_100 = tk.Button(self.overall_frame, text="$100", font=COMICSMALL)
        self.minus_100.grid(row=3, column=2)

        self.minus_other_label = tk.Label(self.overall_frame, text="Other amount: ", font=COMICSMALL)
        self.minus_other_input = tk.Entry(self.overall_frame, width=8)
        self.minus_other_label.grid(row=4, column=1)
        self.minus_other_input.grid(row=4, column=2)
        self.minus_other_but = tk.Button(self.overall_frame, text="Wi")

        self.mainmenu = tk.Button(self.overall_frame, text="Cancel Transaction. \n Return to Main Menu",
                                  font=COMICSMALL)
        self.mainmenu.grid(row=10, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    ViewWithdrawOptions()
    tk.mainloop()
