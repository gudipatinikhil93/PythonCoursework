'''
def function_name(arg):
    statements
    return (optional)

function_name(parameter)


def gst(price):
    print('Original Price: ',price)
    print('Final price :',price+price*0.18)

gst(1000)
gst(20000)
gst(800)
gst(5467)
gst(437526)
gst(1000000)


#tables
def table(n):
    print(f'{n} table')
    print('-------------------')
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


for i in range(1,21):
    table(i)


#checking leap year
def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return 'Leap year'
    else:
        return "Not a leap year"

print(isleap(2012))
print(isleap(2026))
print(isleap(2005))
print(isleap(2069))


#checking prime number
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 'Not a prime number'
    return 'Prime number'

print(isprime(7))
print(isprime(69))
print(isprime(12))
print(isprime(56))
print(isprime(13))


#positional arguments
def details(name,email,pwd):
    print('Name: ',name)
    print('Email: ',email)
    print('Password: ',pwd)
    print('-------------------')

details('nikhil','nikhil@gmail.com','nikhil@123')
details('nikhil@gmail.com','nikhil','nikhil@123')
details('nikhil@123','nikhil','nikhil@gmail.com')


#keyword arguments
def details(name,email,pwd):
    print('Name: ',name)
    print('Email: ',email)
    print('Password: ',pwd)
    print('-------------------')

details(name='nikhil',email='nikhil@gmail.com',pwd='nikhil@123')
details(email='nikhil@gmail.com',name='nikhil',pwd='nikhil@123')
details(pwd='nikhil@123',name='nikhil',email='nikhil@gmail.com')


#Default arguments(should be at the end)
def details(name,email,pwd=None):
    print('Name: ',name)
    print('Email: ',email)
    print('Password: ',pwd)
    print('-------------------')

details('nikhil','nikhil@gmail.com')
details('nikhil','nikhil@gmail.com','nikhil@123')


#variable length arguments
def display(*name): #it is tuple
    print(name)

display('nikhil')
display('nikhil','prasad')
display('nikhil','prasad','tarun')
display('nikhil','prasad','tarun','bunny')
display('nikhil','prasad','tarun','bunny','sai kiran')


def display(**name): #it is dictionary
    print(name)

display(name1='nikhil')
display(name2='nikhil',name3='prasad')
'''





