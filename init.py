from models.constants import app_data
from models.user import User

app_data['NEXT_ACC_NUM'] = '9000'
app_data['NEXT_USER_ID'] = 'a0101'

user = User(user_name='Meow', pin=1234, user_type='teller')
