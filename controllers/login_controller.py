from controllers.main_controller import MainController
from models.user import User
from views.login_view import LoginWindow


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
            self.atm_window.remove_main_frame()
            self.atm_window = MainController(self.master, user_id, self)
            self.atm_window.set_main_window()

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
