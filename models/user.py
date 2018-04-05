from random import choice
from shelve import open

from models.constants import app_data
from models.constants import data_abs_path


class User:
    def __init__(self, user_name, pin, user_type):
        self.user_id = app_data['NEXT_USER_ID']
        self.user_name = user_name
        self.pin = pin
        self.user_type = user_type

        self.user_obj = User.get_persist_user_obj(self.user_id)
        self.user_obj['user_id'] = self.user_id
        self.user_obj['user_name'] = self.user_name
        self.user_obj['pin'] = self.pin
        self.user_obj['user_type'] = self.user_type

        app_data['NEXT_USER_ID'] = ''.join(choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(4))

    @classmethod
    def get_persist_user_obj(cls, userid):
        return open(data_abs_path + '\\' + str(userid) + '.db')

    @staticmethod
    def login(userid, pin):
        return str(User.get_persist_user_obj(userid)['pin']) == str(pin)

    @staticmethod
    def teller_access(userid):
        return User.get_persist_user_obj(userid)['user_type'] == 'teller'
