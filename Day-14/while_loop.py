'''
i = 1
while i<=10:
    print(i)
    i+= 1

i = 10
while i>0:
    print(i)
    i-=1

i = 5
while i<=50:
    print(i)
    i+=5


s = 'nikhil gudipati'
i = 0
while i<len(s):
    print(s[i])
    i+= 1

s = 'nikhil gudipati'
i = len(s) - 1
while i>=0:
    print(s[i])
    i-=1


l = [2134,13245,53426,1212,623,3245,214]
i=0
while i<len(l):
    print(l[i])
    i+=1


n = 1234
sum = 0
while n>0:
    sum += n%10
    n//=10
print('sum of digits is :',sum)


n = 1234
prod=1
while n>0:
    prod *= n%10
    n=n//10
print(prod)


n = 2467
res=0
while n>0:
    rem = n%10
    res = res *10 + rem
    n//=10
   
print(res)

n = 23456478
sum = 0
while n>0:
    if (n%10)%2==0:
        sum += (n%10)
    n//=10
print('sum of digits is :',sum)


l = [3,5,2,5,0,0,0,2,5,0,77,32,12,0,0,0]

while 0 in l:
    l.remove(0)

print(l)


l = [2,3,676,12,4,1,5,61,4,5,2,23]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
'''


