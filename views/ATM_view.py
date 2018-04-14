import tkinter as tk

# from views.view_balance_frame import ViewBalance

COMICFONT = "Comic Sans MS", 15


class MainWindow:
    def __init__(self, root):
        """
        The view for the main menu - displaying the three main ATM actions.

        Arg:
            root: the main menu controller

        Author:
            Precidia Tom
        """
        self.root = root
        self.root.title("Meow ATM")

        self.overall_frame = tk.Frame(self.root, bg="maroon")
        self.top_frame = tk.Frame(self.overall_frame)
        self.mid_frame = tk.Frame(self.overall_frame, bg="lightgrey")
        self.right_frame = tk.Frame(self.overall_frame)
        self.bot_frame = tk.Frame(self.overall_frame)

        self.overall_frame.grid(row=0, column=0)
        self.top_frame.grid(row=0, column=0, padx=100, pady=25)
        self.mid_frame.grid(row=1, column=0, padx=150, pady=50)
        self.bot_frame.grid(row=4, column=0, padx=150, pady=30)

        # Header
        self.welcome = tk.Label(self.top_frame, text='Welcome to Meowmeow Bank, ', font=COMICFONT)
        self.welcome_value = tk.Label(self.top_frame, text='<meow>', font=COMICFONT)
        self.welcome.grid(row=0, column=0, sticky="W")
        self.welcome_value.grid(row=0, column=1, sticky="W")

        # Main screen frame
        self.balance_button = tk.Button(self.mid_frame, text='View my Balance', width=50)

        self.deposit_button = tk.Button(self.mid_frame, text='Deposit', width=50)

        self.withdraw_button = tk.Button(self.mid_frame, text='Withdraw', width=50)

        self.balance_button.grid(row=2, column=0, padx=25, pady=10, sticky="W")
        self.deposit_button.grid(row=3, column=0, padx=25, pady=10, sticky="W")
        self.withdraw_button.grid(row=4, column=0, padx=25, pady=10, sticky="W")

        # Footer
        self.logout_button = tk.Button(self.bot_frame, text="Log Out", width=15)
        self.logout_button.grid(row=6, column=1)

        self.exit_button = tk.Button(self.bot_frame, text='Exit', width=15,
                                     command=lambda: root.destroy())
        self.exit_button.grid(row=6, column=0)

        self.current_frame = self.mid_frame

    def set_main_frame(self):
        self.mid_frame.grid(row=1, padx=150, pady=55)

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    tk.mainloop()
