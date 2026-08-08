Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #output formatting
>>> a = 17
>>> b = 8.2
>>> c = 'codegnan'
>>> print(a,b,c)
17 8.2 codegnan
>>> print('a=',a,'b=',b,'c=',c)
a= 17 b= 8.2 c= codegnan
>>> print('a=',a,'b=',b,'c=',c, sep='')
a=17b=8.2c=codegnan
>>> print('a=',a,'b=',b,'c=',c, sep=' ')
a= 17 b= 8.2 c= codegnan
>>> print('a=',a,'b=',b,'c=',c, sep='', end='\n')
a=17b=8.2c=codegnan
>>> print('a=',a,'b=',b,'c=',c, sep='\n')
a=
17
b=
8.2
c=
codegnan
>>> print('a=',a,'b=',b,'c=',c,end='\n\n')
a= 17 b= 8.2 c= codegnan

>>> print('a=',a,'b=',b,'c=',c, end='@')
a= 17 b= 8.2 c= codegnan@
>>> print(f'nikhil')
nikhil
>>> print(f'nikhil is in {c}')
nikhil is in codegnan
>>> 