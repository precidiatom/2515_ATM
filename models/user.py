from random import choice
from shelve import open

from models.constants import app_data
from models.constants import data_abs_path


class User:
    __NEXT_USER_ID = app_data['NEXT_USER_ID']

    def __init__(self, user_name, password, user_type):
        self.user_id = User.__NEXT_USER_ID
        self.user_name = user_name
        self.password = password
        self.user_type = user_type

        self.user_obj = User.get_persist_user_obj(self.user_id)
        self.user_obj['user_id'] = self.user_id
        self.user_obj['user_name'] = self.user_name
        self.user_obj['password'] = self.password
        self.user_obj['user_type'] = self.user_type

        User.__NEXT_USER_ID = ''.join(choice('0123456789ABCDEF') for i in range(4))

    @classmethod
    def get_persist_user_obj(cls, userid):
        return open(data_abs_path + '\\' + str(userid) + '.db')

    @staticmethod
    def login(userid, password):
        return str(User.get_persist_user_obj(userid)['password']) == str(password)

    @staticmethod
    def teller_access(userid):
        return User.get_persist_user_obj(userid)['user_type'] == 'teller'
