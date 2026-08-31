def display(n):
    if n==11:
        return

    display(n+1)
    print(n)

display(1)


def display(s, ind):
    if ind == len(s):
        return

    display(s, ind + 1)
    print(s[ind],end='')

display("codegnan", 0)



def display(s,ind,w):
    if len(s)-w+1 == ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)

s = input('Enter the string: ')
w = int(input('Enter the width: '))
display(s,0,w)


l1 = list(map(int,input('Enter number: ').split()))
w = int(input('Enter the width: '))
def display(l1,ind,w):
    if len(l1)-w+1 == ind:
        return
    print(l1[ind:ind+w])
    display(l1,ind+1,w)

display(l1,0,w)


#sum of digits
def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l,ind+1)

l = [34,23,56,87,56,22,99]
print(display(l,0))


#sum of digits
n = 432

def sumofdig(n):
    if n==0:
        return 0
    return n%10 + sumofdig(n//10)

print(sumofdig(n))


#factorial
def fact(n):
    if n==1:
        return 1    
    return n * fact(n-1)
    
n=5
print(fact(n))


#normal fibonacci program
n = int(input('Enter the number: '))
if n == 1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b)
    for i in range(n-1):
        a,b = b,a+b
        print(b,end=' ')


def fibo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

for i in range(20):
    print(fibo(i))



