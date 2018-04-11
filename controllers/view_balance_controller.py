from controllers.child_controller import ChildController
from views.balance_view import ViewBalance


class ViewBalanceController(ChildController):

    def __init__(self, parent_controller):
        super().__init__(parent_controller)
        self.view = None

    def set_balance_window(self):
        self.view = ViewBalance(self.parent_controller.atm_window.mid_frame)
        super().set_current_window(self.view)
        self.view.show_balance(self.parent_controller.account_db['balance'])
