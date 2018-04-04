import os
import shelve


class Teller:

    def __init__(self, teller_id, password):
        self.teller_id = teller_id
        self.password = password

        self.teller_obj = Teller.get_persist_teller_obj(teller_id)
        self.teller_obj['teller_id'] = self.teller_id
        self.teller_obj['password'] = self.password

    @classmethod
    def get_persist_teller_obj(cls, teller_id):
        return shelve.open('..\\data\\' + str(teller_id) + '.db', os.path.dirname(__file__))

    @staticmethod
    def login(teller_id, password):
        return str(Teller.get_persist_teller_obj(teller_id)['password']) == str(password)
