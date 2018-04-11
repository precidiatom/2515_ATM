from os import path, makedirs
from random import choice
from shelve import open
from shutil import rmtree

from models.constants import data_abs_path


class User:
    def __init__(self, user_name, pin, user_type):
        self.user_id = '{}{}{}'.format(user_name[0], user_name[-1],
                                       ''.join(choice('0123456789') for i in range(4)))
        self.user_name = user_name
        self.pin = pin
        self.user_type = user_type

        self.user_obj = User.get_persist_user_obj(self.user_id)
        self.user_obj['user_id'] = self.user_id
        self.user_obj['user_name'] = self.user_name
        self.user_obj['pin'] = self.pin
        self.user_obj['user_type'] = self.user_type

    def get_user_info(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_type': self.user_type
        }

    @staticmethod
    def delete_user(userid):
        rmtree('{}\\{}\\'.format(data_abs_path, str(userid)))

    @staticmethod
    def get_persist_user_obj(userid):
        if not path.exists('{}\\{}\\'.format(data_abs_path, str(userid))):
            makedirs('{}\\{}\\'.format(data_abs_path, str(userid)))
        return open('{}\\{}\\{}.db'.format(data_abs_path, str(userid), str(userid))
                    )

    @staticmethod
    def login(userid, pin, user_type):
        valid_user = User._check_valid_user(userid)
        valid_pin = str(User.get_persist_user_obj(userid)['pin']) == str(pin)
        teller_access = User.teller_access(userid) if user_type == 'teller' else True

        return valid_user and valid_pin and teller_access

    @staticmethod
    def teller_access(userid):
        return User.get_persist_user_obj(userid)['user_type'] == 'teller'

    @staticmethod
    def _check_valid_user(userid):
        return path.exists('{}\\{}\\'.format(data_abs_path, str(userid)))
