from views.ATM_view import MainWindow
import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10

class ViewWithdraw(tk.Frame):
    def __init__(self, parent, MainWindow):
        self.MainWindow = MainWindow
        tk.Frame.__init__(self, parent)

        self.welcome = tk.Label(parent, text='Withdraw From Which Account?', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.chequing_but = tk.Button(parent, text="Chequing", font = COMICSMALL)
        self.chequing_but.grid(row=1, column=0)
        self.chequing_value = tk.Label(parent)
        self.chequing_value.grid(row=2, column=0)

        self.savings_but = tk.Button(parent, text="Savings", font=COMICSMALL)
        self.savings_but.grid(row=3, column=0)
        self.savings_value = tk.Label(parent)
        self.savings_value.grid(row=4, column=0)

        self.mainmenu = tk.Button(parent, text="Return to Main Menu", font=COMICSMALL)
        self.mainmenu.grid(row=7, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    ViewWithdraw(root, MainWindow)
    tk.mainloop()