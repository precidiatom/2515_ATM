from controllers.ChildController import ChildController
from views.DepositView import ViewDeposit


class DepositController(ChildController):

    def __init__(self, parent_controller):
        super().__init__(parent_controller)

    def set_deposit_window(self):
        super().set_current_window(
            ViewDeposit(self.parent_controller.atm_window.mid_frame))
