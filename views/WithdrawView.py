import tkinter as tk

COMICFONT = "Comic Sans MS", 16
COMICSMALL = "Comic Sans MS", 10


class ViewWithdraw(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.welcome = tk.Label(parent, text='Withdraw From Which Account?', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.chequing_but = tk.Button(parent, text="Chequing", font=COMICSMALL)
        self.chequing_but.grid(row=1, column=0)
        self.chequing_value = tk.Label(parent)
        self.chequing_value.grid(row=2, column=0)

        self.savings_but = tk.Button(parent, text="Savings", font=COMICSMALL)
        self.savings_but.grid(row=3, column=0)
        self.savings_value = tk.Label(parent)
        self.savings_value.grid(row=4, column=0)

        self.main_menu_btn = tk.Button(parent, text="Return to Main Menu", font=COMICSMALL)
        self.main_menu_btn.grid(row=7, column=0)

    def remove_main_frame(self):
        self.destroy()
        self.chequing_but.grid_remove()
        self.savings_but.grid_remove()
        self.welcome.grid_remove()
