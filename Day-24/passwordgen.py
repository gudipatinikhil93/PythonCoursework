import random

name = input('Enter your name: ').title()
dob = input('Enter your Date of Birth (DD-MM-YYYY): ')

special = ['@','!','#','$','%','&','*',',','.']

password = name + random.choice(special) + dob[-4:]

print('Generated Password: ',password)