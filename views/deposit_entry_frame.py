from views.ATM_view import MainWindow
import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10

class ViewDepositInput(tk.Frame):
    def __init__(self, parent, MainWindow):
        self.MainWindow = MainWindow
        tk.Frame.__init__(self, parent)

        self.welcome = tk.Label(parent, text='Depositing into', font=COMICFONT)
        self.welcome.grid(row=0, column=0)
        self.welcome_account = tk.Label(parent, text='<placeholder pls use magic>')
        self.welcome_account.grid(row=0,column=1)

        self.deposit_label = tk.Label(parent, text="Amount to Deposit:", font = COMICSMALL)
        self.deposit_label.grid(row=1, column=1)
        self.deposit_amt = tk.Entry(parent, width=15)
        self.deposit_amt.grid(row=2, column=1)

        self.mainmenu = tk.Button(parent, text="Return to Main Menu", font=COMICSMALL)
        self.mainmenu.grid(row=9, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    ViewDepositInput(root, MainWindow)
    tk.mainloop()
