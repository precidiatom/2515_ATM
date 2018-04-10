from views.BalanceView import ViewBalance


class ViewBalanceController:

    def __init__(self, parent_controller):
        self.main_window_controller = parent_controller
        self.atm_balance_window = None

    def set_balance_window(self):
        self.atm_balance_window = ViewBalance(self.main_window_controller.atm_window.mid_frame, self)
        self.atm_balance_window.grid(row=1, padx=150, pady=55)
        self.atm_balance_window.main_menu_btn.config(command=self._return_to_main_menu)

    def _return_to_main_menu(self):
        # del self.main_window_controller.atm_window.current_frame
        self.main_window_controller.set_main_window()
        self.main_window_controller.atm_window.welcome.destroy()
        self.main_window_controller.set_current_frame(self.main_window_controller.atm_window)
        # self.atm_balance_window.mainframe.grid_remove()
        self.atm_balance_window.acc_balance.grid_remove()
        self.atm_balance_window.main_menu_btn.grid_remove()
        self.atm_balance_window.destroy()
