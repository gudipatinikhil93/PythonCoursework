#local variable are defined inside the function and can only be accessed inside the function.
#global variables are defined outside the function and can be accessed anywhere in the program.

def display():
    n=10 #local variable
    print('Inside Function:', n)

n=12 #global variable
display()
print('Outside Function:', n)


def display():
    global n
    n=10
    print('Inside Function:', n)

display()
print('Outside Function:', n)

#global variable cannot be passed as an argument to a function. It can be accessed directly inside the function.


def display(n):
    global n
    n=10 
    print('Inside Function:', n)

'''
n=12 
display(n)
print('Outside Function:', n)
SyntaxError: name 'n' is parameter and global
'''


def display():
    global n
    n+=10
    print('Inside Function:', n)

n=10
display()
print('Outside Function:', n)


def coursedetails():
    course = 'PFS'
    def update():
        course = 'JFS'
        print('Inside Function: ',course)
    update()
    print('Outer Function: ',course)

coursedetails()


def coursedetails():
    course = 'PFS'
    def update():
        nonlocal course #nonlocal variable is used to work with variables inside nested functions, not outside functions. only accessible in nested functions
        course = 'JFS'
        print('Inside Function: ',course)
    update()
    print('Outer Function: ',course)

coursedetails()

'''
l = [1, 2, 3, 4, 5]
print(sum(l))

sum = 20
print(sum(l)) #TypeError: 'int' object is not callable
'''

#this will give error because sum is now a variable and not a function. so we cannot use it as a function.
#the moment the built-in function name is used as a variable name, it will override the built-in function and we cannot use it as a function anymore.




