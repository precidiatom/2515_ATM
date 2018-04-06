import tkinter as tk

COMICFONT = "Comic Sans MS", 15
COMICSMALL = "Comic Sans MS", 10
class MainWindow:
    def __init__(self, root):

        self.root = root

        self.root.title("Meow ATM")
        self.root.config()

        self.overall_frame = tk.Frame(self.root, bg="cyan")
        self.top_frame = tk.Frame(self.overall_frame)
        self.mid_frame = tk.Frame(self.overall_frame, bg="yellow")
        self.right_frame = tk.Frame(self.overall_frame)
        self.bot_frame = tk.Frame(self.overall_frame)

        self.overall_frame.pack()
        self.top_frame.grid(row=0, padx=100, pady=25)
        self.mid_frame.grid(row=1, padx=150, pady=50)
        self.bot_frame.grid(row=4, padx=150, pady=30)

# Header
        self.welcome = tk.Label(self.top_frame, text='Welcome to Meowmeow Bank, ', font=COMICFONT)
        self.welcome_value = tk.Label(self.top_frame, text='<placeholderformeow>', font=COMICFONT)
        self.welcome.grid(row=0, column=0)
        self.welcome_value.grid(row=0, column=1)

# Main screen frame
        self.mainframe = tk.Frame(self.mid_frame)
        self.mainframe.grid(row=1, padx=150, pady=55)
        self.balance_button = tk.Button(self.mainframe, text='View my Balance', width=50, command=self.display_newframe)

        self.deposit_button = tk.Button(self.mainframe, text='Deposit', width=50)

        self.withdraw_button = tk.Button(self.mainframe, text='Withdraw', width=50)

        self.balance_button.grid(row=3, column=1, padx=25, pady=10)
        self.deposit_button.grid(row=4, column=1, padx=25, pady=10)
        self.withdraw_button.grid(row=5, column=1, padx=25, pady=10)

        self.exit_button = tk.Button(self.bot_frame, text='Exit', width=20,
                                     command=lambda: root.destroy())
        self.exit_button.grid(row=8, column=5)

        self.current_frame = self.mainframe

    def display_newframe(self):
        self.mainframe.grid_remove()
        self.current_frame = ViewBalance(self.mid_frame, self).grid(row=1, padx=150, pady=55)

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
    MainWindow(root)
    tk.mainloop()
