from models.user import User
from views.login_view import LoginWindow


class LoginController:
    def __init__(self, frame_controller):
        self.frame_controller = frame_controller
        self.view = None
        self.interface = LoginWindow(self.frame_controller.master)
        self.interface.credentials_butt.config(command=self._check_credentials)
        self.interface.user_id.bind("<KeyPress-Return>", lambda ev: self._check_credentials())
        self.interface.user_pin.bind("<KeyPress-Return>", lambda ev: self._check_credentials())

    def set_current_frame(self, frame):
        self.interface.current_frame = frame

    def _confirm_pin(self, user_id, pin):
        if User.login(user_id, pin):
            self.frame_controller.user_id = user_id
            self.frame_controller.change_controller('main_menu', user_id)
        else:
            self.interface.fail_login()

    def _check_credentials(self):
        user_account = self.interface.user_id.get()
        pin_inp = self.interface.user_pin.get()
        self._confirm_pin(user_account, pin_inp)
