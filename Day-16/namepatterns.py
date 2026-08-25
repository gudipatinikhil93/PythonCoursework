#D
n = int(input('Enter the size: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#B
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#C
n = int(input('Enter the size: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#E
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()


n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#F
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#C
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#G
n = int(input('Enter the size: '))
m = n//2

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (i==m and j>=m) or (j==n-1 and i>=m):
            print('*',end='')
        else:
            print(' ',end='')
    print()


#H
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()


#I
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()


#J
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or (i==n-1 and j<=m):
            print('*',end='')
        else:
            print(' ',end='')
    print()

#L
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()


#Z
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j == n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#X
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j == n-1 or i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print()


#Y
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j == n-1 or (i==j and i<=m):
            print('*',end='')
        else:
            print(' ',end='')
    print()


#K
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i==j and i>=m) or (i+j == n-1 and i<=m):
            print('*',end='')
        else:
            print(' ',end='')
    print()

#M
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end='')
        else:
            print(' ',end='')
    print()



#W
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):
            print('*',end='')
        else:
            print(' ',end='')
    print()



#P
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or (j==n-1 and i<=m) or i==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()



#v
n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i+j==m+n-1 and i>=m) or i-j==m:
            print('*',end='')
        else:
            print(' ',end='')
    print()


n = int(input('Enter the size: '))
m = n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i>=m) or (j==n-1 and i>=m) or i+j==m-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
