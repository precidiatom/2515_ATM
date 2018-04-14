import tkinter as tk
from tkinter import messagebox

COMICFONT = "Comic Sans MS", 14
COMICSMALLER = "Comic Sans MS", 8


class LoginWindow:
    def __init__(self, root):
        self.root = root

        self.root.title("Meow ATM")
        self.root.config()

        self.overall_frame = tk.Frame(self.root, bg="maroon")
        self.top_frame = tk.Frame(self.overall_frame)
        self.mid_frame = tk.Frame(self.overall_frame, bg="lightgrey", padx=10, pady=10)
        self.bot_frame = tk.Frame(self.overall_frame)

        self.overall_frame.grid(row=0, column=0)
        self.top_frame.grid(row=0, padx=100, pady=25)
        self.mid_frame.grid(row=1, padx=150, pady=50)
        self.bot_frame.grid(row=4, padx=150, pady=30)

        self.welcome = tk.Label(self.top_frame, text='Welcome to Meowmeow Bank', font=COMICFONT)
        self.welcome.grid(row=0, column=0)

        self.user_id_label = tk.Label(self.mid_frame, text="User ID:", font=COMICFONT)
        self.user_id_label.grid(row=1, column=0, sticky="W")
        self.user_id = tk.Entry(self.mid_frame, width=30)

        self.user_pin_label = tk.Label(self.mid_frame, text="PIN:", font=COMICFONT)
        self.user_pin_label.grid(row=3, column=0, sticky="NW")
        self.user_pin = tk.Entry(self.mid_frame, show="*", width=10)
        self.user_pin.config(show="*")

        self.credentials_butt = tk.Button(self.mid_frame, text="Submit", font=COMICSMALLER, bg="yellow")
        self.credentials_butt.grid(row=6, column=0)

        self.user_id.grid(row=2, column=0, padx=88, pady=10)
        self.user_pin.grid(row=4, column=0, padx=88, pady=10)

        self.exit_button = tk.Button(self.bot_frame, text='Exit', width=20, font=COMICSMALLER,
                                     command=lambda: root.destroy())
        self.exit_button.grid(row=8, column=5)

    def set_main_frame(self):
        self.mainframe.grid(row=1, padx=150, pady=55)

    def fail_login(self):
        tk.messagebox.showerror("Incorrect account", "You have entered invalid user id or pin")

    def remove_main_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    tk.mainloop()
