for i in range(5):
    for j in range(5):
        print('*',end='')
    print()


for i in range(5):
    for j in range(5):
        print(j%2,end='')
    print()

for i in range(5):
    for j in range(5):
        print(i%2,end='')
    print()
 

for i in range(5):
    for j in range(5):
        print((i+j)%2,end='')
    print()       


for i in range(5):
    for j in range(5):
        print(i+j,end='')
    print()

n=1
for i in range(5):
    for j in range(5):
        print(n,end='')
        n+=1
    print()


for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()


for i in range(5):
    for j in range(5-i):
        print('*',end='')
    print()


for i in range(5):
    for space in range(5-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(5):
    for space in range(i):
        print(' ',end='')
    for j in range(5-i):
        print('*',end='')
    print()


n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    if i <= m:
        for j in range(i+1):
            print('*',end='')
    else:
        for j in range(n-i):
            print('*',end='')
    print()


n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    if i <= m:
            print('* '*(i+1),end='')
    else:
            print('* '*(n-i),end='')
    print()


n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    if i <= m:
            print(' '*(m-i),'*'*(i+1),end='',sep='')
    else:
            print(' '*(i-m),'*'*(n-i),end='',sep='')
    print()

