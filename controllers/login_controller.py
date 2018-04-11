from controllers.deposit_controller import DepositController
from controllers.view_balance_controller import ViewBalanceController
from controllers.withdraw_controller import WithdrawController
from models.account import Account
from views.ATM_view import MainWindow
from views.login_view import LoginWindow
from models.user import User

class LoginController:
    def __init__(self, master, account):
        self.master = master
        self.account_db = None
        self.atm_window = LoginWindow(self.master)
        self.atm_window.credentials_butt.config(command=self._check_credentials)

        self._refresh_window()

    def set_main_window(self):
        self.atm_window.set_main_frame()

    def set_current_frame(self, frame):
        self.atm_window.current_frame = frame

    def _confirm_pin(self, user_id, pin):
        if User.login(user_id, pin):
            self.user = User.get_persist_user_obj(user_id)
            #self.atm_window = MainWindow(self.master)
        else:
            self.atm_window.fail_login()

        print('yabai', User.login(user_id, pin))

    def _refresh_window(self):
        pass

    def _view_login(self):
        self.atm_window = LoginWindow(self.master)

    def _check_credentials(self):
        user_account = self.atm_window.user_id.get()
        pin_inp = self.atm_window.user_pin.get()
        self._confirm_pin(user_account, pin_inp)

    def _redirect(self):
        pass

