from tkinter import *
from ATM_controller import ATMController

class MainWindow:
    def __init__(self, root):
        self.root = root

        self.root.title("Meow ATM")
        self.root.config(background="palegreen")

        self.top_frame = Frame(self.root)
        self.mid_frame = Frame(self.root)
        self.right_frame = Frame(self.root)
        self.bot_frame = Frame(self.root)

        self.top_frame.grid(row=0, padx=100, pady=15)
        self.mid_frame.grid(row=1, padx=150, pady=50)
        self.bot_frame.grid(row=4, padx=150, pady=30)

        self.welcome = Label(self.top_frame, text='Welcome to Meowmeow Bank, ')
        self.welcome_value = Label(self.top_frame, text='<placeholderformeow>')
        self.welcome.grid(row=0, column=0, sticky=E)
        self.welcome_value.grid(row=0, column=1, sticky=W)

        self.balance_button = Button(self.mid_frame, text='View my Balance', width=50)
        self.balance_button.bind()

        self.deposit_button = Button(self.mid_frame, text='Deposit', width=50)
        self.deposit_button.bind('<Button-1>', ATMController.deposit_fund(self))

        self.withdraw_button = Button(self.mid_frame, text='Withdraw', width=50)
        self.withdraw_button.bind('<Button-1>', ATMController.deposit_fund(self))

        self.balance_button.grid(row=3, column=1, sticky=E, padx=25, pady=10)
        self.deposit_button.grid(row=4, column=1, sticky=E, padx=25, pady=10)
        self.withdraw_button.grid(row=5, column=1, sticky=E, padx=25, pady=10)

        self.exit_button = Button(self.bot_frame, text='Exit', width=20,
                                  command=lambda:root.destroy())
        #self.exit_button.bind('<Button-1>', MainWindow._exit_program)
        self.exit_button.grid(row=8, column=5, sticky=E)

    # I dont know how to fix this T_T
    # def _exit_program(self):
    #     MainWindow.root.destroy()

if __name__ == "__main__":
    root = Tk()
    MainWindow(root)
    mainloop()