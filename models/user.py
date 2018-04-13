from os import path, makedirs
from random import choice
from shelve import open
from shutil import rmtree

from models.constants import data_abs_path


class User:
    def __init__(self, userid='', user_name='', pin='', user_type=''):

        if not User.check_existing_user(userid):
            self.user_id = '{}{}{}'.format(user_name[0], user_name[-1],
                                           ''.join(choice('0123456789') for i in range(4)))
            self.user_name = user_name
            self.pin = pin
            self.user_type = user_type
            self.accounts = {}

            self.user_obj = User.get_persist_user_obj(self.user_id)
            self.update_user_data()
        else:
            self.user_obj = User.get_persist_user_obj(userid)
            self.user_id = self.user_obj['user_id']
            self.user_name = self.user_obj['user_name']
            self.pin = self.user_obj['pin']
            self.user_type = self.user_obj['user_type']
            self.accounts = self.user_obj['accounts']
            # self.accounts = literal_eval(self.user_obj['accounts'])

    def update_user_data(self):
        self.user_obj['user_id'] = self.user_id
        self.user_obj['user_name'] = self.user_name
        self.user_obj['pin'] = self.pin
        self.user_obj['user_type'] = self.user_type
        self.user_obj['accounts'] = self.accounts
        User.get_persist_user_obj(self.user_id).update(self.user_obj)

    def get_user_info(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_type': self.user_type
        }

    @staticmethod
    def delete_user(userid):
        if User.check_existing_user(userid):
            rmtree('{}\\{}\\'.format(data_abs_path, str(userid)))
            return True
        else:
            return False

    @staticmethod
    def get_persist_user_obj(userid):
        if not path.exists('{}\\{}\\'.format(data_abs_path, str(userid))):
            makedirs('{}\\{}\\'.format(data_abs_path, str(userid)))
        return open('{}\\{}\\{}.db'.format(data_abs_path, str(userid), str(userid))
                    )

    @staticmethod
    def login(userid, pin, user_type=''):
        if User.check_existing_user(userid) and str(User.get_persist_user_obj(userid)['pin']) == str(pin):
            if user_type == 'teller':
                return User.teller_access(userid)
            else:
                return True
        else:
            return False

    @staticmethod
    def teller_access(userid):
        return User.get_persist_user_obj(userid)['user_type'] == 'teller'

    @staticmethod
    def check_existing_user(userid):
        return len(str(userid)) > 0 and path.exists('{}\\{}\\'.format(data_abs_path, str(userid)))
