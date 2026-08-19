#nested if means, using if inside another if block

follow = eval(input('Follows Account :'))

if follow:
    cf = eval(input('Close friend:'))
    if cf:
        print('story visible')
    else:
        print('not in close friends list')
else:
    print('Follow this account first')



register = eval(input('registered:'))

if register:
    fee = eval(input('Fee paid:'))
    if fee:
        print('tournament entry confirmed')
    else:
        print('Entry fee pending')
else:
    print('Registration required')


link = eval(input("Tell whether the Link is active or not"))

if link:
 permission = eval(input("tell permission is granted or not"))
 if permission:
    print("File Opened Successfully")
 else:
    print("permission not granted")
else:
    print("link is not active")

data={
    'tharun':{'status':True,'python':49,'mysql':49,'flask':49},
    'prasad':{'status':True,'python':90,'mysql':80,'flask':80},
    'sai':{'status':False,'python':None,'mysql':None,'flask':None},
    'nikhil':{'status':True,'python':90,'mysql':50,'flask':70},
    'bunny':{'status':True,'python':70,'mysql':60,'flask':40}
}


name = input('enter the name:')
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f'hello {name}')
        print(f'your average scoe is {avg}')
        if avg>=90:
            print('outstanding performance')
        if avg>=80:
            print('very good')
        if avg>=70:
            print('good, work hard')
        if avg>=35:
            print('better luck next time')
        else:
            print('you failed the exam')
    else:
        print(f'{name}did not attend to the exam')

else:
    print(f'{name} not found')