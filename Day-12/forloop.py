#string, list, tuple, set, dict, range

#string iteration
s = 'python programming'
for i in s:
    print(i)

#list iteration
l = [1,2,3,4,5]
for num in l:
    print(num)

#set iterations
prices = (4353,12345,21345,653,1235)
for price in prices:
    print(price)

#dictionary iteration
d = {1:'one',2:'two',3:'three'}
for i in d:
    print(i,d[i])

#range iteration, range(start,end+1,step)
for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(50,0,-1):
    print(i)
    
for i in range(19,0,-2):
    print(i)

#printing index
s = 'python programming language'
for i in range(len(s)):
    print(i,s[i])

#using enumerate
name = 'nikhil gudipati'
for i in enumerate(name):
    print(i)

d = {'nikhil':'one','prasad':'two','tharun':'three'}
for i in enumerate(d):
    print(i,i[1],d[i[1]])

#jumping statements

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

#for with else
#if for contains break, then else block will execute, if break is not there, then else block will execute
l = [342,1234,54,324,523,12]
for i in l:
    if i==1234:
        print(i,'found')
        break
else:
    print(i,'not found')

for i in range(1,14):
    if i==3:    
        print(i)
else:
    print('end of loop')

pin = 1234
for i in range(5):
    epin = int(input('Enter your pin: '))
    if epin == pin:
        print('Phone Unlocked')
        break
    else:
        print('invalid pin')
else:
    print('Try after 30 seconds')


n = 2
for i in range(2,n//2+1):
    if n%i==0:
        print('not a prime number')
        break
else:
    print('prime number')