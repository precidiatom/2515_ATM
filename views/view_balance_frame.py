from views.ATM_view import MainWindow
import tkinter as tk

COMICFONT = "Comic Sans MS", 15
COMICSMALL = "Comic Sans MS", 10

class ViewBalance(tk.Frame):
    def __init__(self, parent, MainWindow):
        self.MainWindow = MainWindow
        tk.Frame.__init__(self, parent)

        self.welcome = tk.Label(parent, text='Viewing your account balance', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.acc_balance = tk.Label(parent, text="Account Balance: ", font=COMICSMALL)
        self.acc_balance.grid(row=1, column=0)

        self.mainmenu = tk.Button(parent, text="Return to Main Menu", command=self.go_mainmenu)
        self.mainmenu.grid(row=7, column=0)

    def go_mainmenu(self):
        del self.MainWindow.current_frame
        self.welcome.destroy()
        self.acc_balance.grid_remove()
        self.mainmenu.grid_remove()
        self.MainWindow.current_frame = tk.Frame(self.MainWindow.mainframe.grid(row=1, padx=150, pady=55))

if __name__ == "__main__":
    root = tk.Tk()
    ViewBalance(root, MainWindow)
    tk.mainloop()
