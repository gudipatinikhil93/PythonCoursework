'''
import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print('start')
sys.exit()
print('end')


import platform

print(platform.system())
print(platform.release())
print(platform.platform())


import math

print(math.pi)
print(math.e)

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(2,6))
print(math.sqrt(36))
print(math.pow(4,6))


import math

print(math.ceil(5.1))
print(math.ceil(5.9))
print(math.ceil(5.0))

print(math.floor(5.9))
print(math.floor(5.1))
print(math.floor(5.0))

print(round(5.7))
print(round(5.4))
print(round(5.5))



import random

random.seed(9) #with the use of seed, we can get the same random number again and again
print(random.random()) #float 0.0 to 1.0
print(random.randint(1,6)) #int 1 to 6
print(random.uniform(1,6)) #float 1 to 6

l=['heads','tails']
print(random.choice(l)) #randomly choose from list

lang = ['python','java','c++','c#']
random.shuffle(lang)
print(lang)



from collections import Counter,defaultdict

s = 'python programing'
res = Counter(s)
print(res)

d={}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)


res=defaultdict(list)
prod = ['suger','salt','milk']
for i in prod:
    res[i].append(['des','rev','com'])

print(res)
'''

from collections import deque

l = deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)

print(l)