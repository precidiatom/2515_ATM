from views.ATM_view import MainWindow
import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10

class ViewWithdrawOptions(tk.Frame):
    def __init__(self, parent, MainWindow):
        self.MainWindow = MainWindow
        tk.Frame.__init__(self, parent)

        self.welcome = tk.Label(parent, text='Withdraw', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.minus_20 = tk.Button(parent, text="$20", font = COMICSMALL)
        self.minus_20.grid(row=1, column=0)

        self.minus_40 = tk.Button(parent, text="$40", font = COMICSMALL)
        self.minus_40.grid(row=2, column=0)

        self.minus_60 = tk.Button(parent, text="$60", font = COMICSMALL)
        self.minus_60.grid(row=3, column=0)

        self.minus_80 = tk.Button(parent, text="$80", font = COMICSMALL)
        self.minus_80.grid(row=1, column=2)

        self.minus_100 = tk.Button(parent, text="$100", font = COMICSMALL)
        self.minus_100.grid(row=2, column=2)

        self.minus_other_label = tk.Label(parent, text="Other amount: ", font = COMICSMALL)
        self.minus_other_input = tk.Entry(parent, width=8)
        self.minus_other_label.grid(row=3, column=1)
        self.minus_other_input.grid(row=3, column=2)

        self.mainmenu = tk.Button(parent, text="Cancel, return to Main Menu", font=COMICSMALL)
        self.mainmenu.grid(row=10, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    ViewWithdrawOptions(root, MainWindow)
    tk.mainloop()
