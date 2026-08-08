Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python operators
>>> #arithmetic operators
>>> a = 10
>>> b = 12
>>> a+b
22
>>> a-b
-2
>>> a*b
120
>>> a**b
1000000000000
>>> a/b
0.8333333333333334
>>> a//b
0
>>> a%b
10
>>> 12/2
6.0
>>> 12//2
6
>>> #comparison operators
>>> a>b
False
>>> a<b
True
>>> a>=b
False
>>> a<=b
True
>>> a==b
False
>>> a!=b
True
>>> #assignment  operators
>>> a = 10
>>> a += 10
>>> a
20
>>> a -= 5
>>> a
15
>>> a **= 2
>>> a
225
>>> a %= 2
>>> a
1
>>> a /= 2
>>> a
0.5
>>> a += 23
>>> a
23.5
>>> a //= 12
>>> a
1.0
>>> 10//2
5
>>> 23.5//12
1.0
>>> a*= 2
>>> a
2.0
>>> a
2.0
>>> a=2
>>> a
2
>>> #relational operators
>>> email = True
>>> password = False
>>> email and password
False
>>> login = False
>>> display_prod = True
>>> login and display_prod
False
>>> 3%2==0 and 4%2==0
False
>>> 's' in 'aeiou'
False
>>> 's' not in 'aeiou'
True
>>> not 3%2==0
True
>>> 3%2==0
False
>>> login or display_prod
True
>>> True or False
True
>>> True and True
True
>>> True and False
False
>>> not True
False
>>> not False
True
>>> 'n' in 'nikhil
SyntaxError: EOL while scanning string literal
>>> 'n' in 'nikhil'
True
>>> True and True and False
False
>>> True and True or False
True
>>> False or False and True
False
>>> True and True and True or False
True
>>> #membership operations
>>> #only string list tuple set dict
>>> #string
>>> name = 'nikhil'
>>> 'n' in name
True
>>> 'n' not in name
False
>>> #list
>>> l = [1,2,3,4]
>>> 4 in l
True
>>> 4 not in l
False
>>> #tuple
>>> t = (1,2,34,4)
>>> 5 in t
False
>>> 5 not in t
True
>>> #set
>>> s = {1,2,3,4}
>>> 3 in s
True
>>> 3 not in s
False
>>> #dict
>>> #in only works for keys not for values
>>> d = {'name' : 'nikhil', 'batch' : 65, 'placed' : 'yes'}
>>> 'nikhil' in d
False
>>> 'name' in d
True
>>> 'placed' in d
True
>>> 'yes' in d
False
>>> #identity operator
>>> a = [1,2,3,4]
>>> b = [1,2,3,4]
>>> a == b
True
>>> id(a)
2506983528384
>>> id(b)
2506983651328
>>> a in b
False
>>> b ina
SyntaxError: invalid syntax
>>> b in a
False
>>> c = a
>>> id(a)
2506983528384
>>> id(c)
2506983528384
>>> c in a
False
>>> a in c
False
>>> #bitwise operators
>>> # & | ^ ~ >> <<
>>> 2 & 3
2
>>> 2 | 3
3
>>> 2 ^ 3
1
>>> ~2
-3
>>> ~4
-5
>>> 2 << 4
32
>>> 2 >> 4
0
>>> 