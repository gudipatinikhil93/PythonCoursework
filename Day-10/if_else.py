
username = input('Enter Username: ')
password = input('Enter your Password: ')

if username == 'admin' and password == 'admin123':
    print('Login Successfull')
else:
    print('Invalid Credentials')


products = ['bag','laptop','pen','charger','books']
search = input('Enter Product name: ')
if search in products:
    print(f'{search} found')
else:
    print(f'{search} not found')



bill = int(input('Enter Bill Amount: '))
if bill>99:
    print(f'Total bill is {bill}')
else:
    print(f'Total bill is {bill+30}')