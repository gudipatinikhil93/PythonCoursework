l = [i for i in range(1,11)]
print(l)


m = [i for i in range(2,11,2)]
print(m)


n = 16
f = [i for i in range(1,n+1) if n%i==0]

print(f)

x=[1,2,3,4,5,6,7,8,9,10]
y=[i if i%2==0 else 0 for i in x]

print(y)


l = [[i for i in range(1,4)] for j in range(3)]
print(l)


s = {i:i*i for i in range(1,11)}
print(s)
