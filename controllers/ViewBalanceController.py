from controllers.ChildController import ChildController
from views.BalanceView import ViewBalance


class ViewBalanceController(ChildController):

    def __init__(self, parent_controller):
        super().__init__(parent_controller)

    def set_balance_window(self):
        super().set_current_window(ViewBalance(self.parent_controller.atm_window.mid_frame, self))
