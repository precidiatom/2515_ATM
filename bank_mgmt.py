from controllers.BM_controller import BMController
from models.user import User

if __name__ == '__main__':
    user = User(userid='a0101', user_name='Meow', pin=1234, user_type='teller')
    controller = BMController()
