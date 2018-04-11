class ChildController:

    def __init__(self, parent_controller):
        self.parent_controller = parent_controller
        self.current_window = None

    def set_current_window(self, window):
        self.current_window = window
        self.current_window.grid(row=1, padx=150, pady=55)
        self.current_window.main_menu_btn.config(command=self._return_to_main_menu)

    def _return_to_main_menu(self):
        self.current_window.destroy()
        self.parent_controller.set_main_window()
        self.parent_controller.set_current_frame(self.parent_controller.atm_window)
        self.current_window.main_menu_btn.grid_remove()
        self.current_window.remove_main_frame()
