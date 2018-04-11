from controllers.child_controller import ChildController
from views.withdraw_view import ViewWithdraw


class WithdrawController(ChildController):

    def __init__(self, parent_controller):
        super().__init__(parent_controller)

    def set_withdraw_window(self):
        super().set_current_window(
            ViewWithdraw(self.parent_controller.atm_window.mid_frame))
