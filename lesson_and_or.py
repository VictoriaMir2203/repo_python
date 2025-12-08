#  and
user_login = 'qwer'
user_pass = '123'

login = input('Login: ')
password = input('Password: ')

if login == user_login and password == user_pass:
    print('Secret is open')
else:
    print('Locked')

# or
crit1 = 'red'
crit2 ='lock'

color = input('Color: ')
feature = input('Feature: ')

if color == crit1 or feature == crit2:
    print("Buy it!")
else:
    print("Don't buy it!")
