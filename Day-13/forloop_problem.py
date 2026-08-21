#program to find factors of a number
n = int(input('Enter a number: '))
res = []
for i in range(1,n+1):
    if n%i==0:
        res.append(i)

print(f'Factors of {n} = {res}')


#frequency count in dictionary
s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)


d = 'aaaaadddddssqqqqsssaa'
count = 1
res = ''
#a4d5s2q4s3a2
for i in range(len(d)-1):
    if d[i] == d[i+1]:
        count = count + 1
    else:
        res += d[i]+str(count)
        count = 1
print(res+s[i]+str(count))
print(d[i])