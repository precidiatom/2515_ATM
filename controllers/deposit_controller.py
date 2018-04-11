from controllers.child_controller import ChildController
from views.deposit_view import ViewDeposit
from views.deposit_entry_frame import ViewDepositInput


class DepositController(ChildController):

    def __init__(self, parent_controller):
        super().__init__(parent_controller)

    def set_deposit_window(self):
        super().set_current_window(
            ViewDeposit(self.parent_controller.atm_window.mid_frame))

    def _click_chequing(self):
        print('meow')
        # super().set_current_window(
        #     ViewDepositInput(self.parent_controller.atm_window.mid_frame))