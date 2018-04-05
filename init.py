from models.constants import app_data
from models.user import User

app_data['NEXT_ACC_NUM'] = '9000'
app_data['NEXT_USER_ID'] = 'a0101'

user = User('Meow', 1234, 'teller')
