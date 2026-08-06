Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #int to other
>>> a = 10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> #float to other
>>> b = 12.3
>>> int(b)
12
>>> complex(b)
(12.3+0j)
>>> str(b)
'12.3'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> bool(b)
True
>>> #complex to other
>>> c = 10+2j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(10+2j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> #string to other
>>> s1 = 'nikhil'
>>> s2 = '123'
>>> int(s1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(s1)
ValueError: invalid literal for int() with base 10: 'nikhil'
>>> int(s2)
123
>>> float(s1)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(s1)
ValueError: could not convert string to float: 'nikhil'
>>> float(s2)
123.0
>>> complex(s1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(s1)
ValueError: complex() arg is a malformed string
>>> complex(s2)
(123+0j)
>>> list(s1)
['n', 'i', 'k', 'h', 'i', 'l']
>>> list(s2)
['1', '2', '3']
>>> tuple(s1)
('n', 'i', 'k', 'h', 'i', 'l')
>>> tuple(s2)
('1', '2', '3')
>>> set(s1)
{'l', 'i', 'h', 'n', 'k'}
>>> set(s2)
{'1', '3', '2'}
>>> dict(s1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict(s1)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict(s2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dict(s2)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> #list to other
>>> l = [1,2,3,4]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(l)
'[1, 2, 3, 4]'
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> #tuple to other
>>> t = (1,2,3,4)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> str(t)
'(1, 2, 3, 4)'
>>> list(t)
[1, 2, 3, 4]
>>> set(t)
{1, 2, 3, 4}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> #set to other
>>> s = {2,3,4,5,6}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a number, not 'set'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(s)
'{2, 3, 4, 5, 6}'
>>> list(s)
[2, 3, 4, 5, 6]
>>> tuple()s
SyntaxError: invalid syntax
>>> tuple(s)
(2, 3, 4, 5, 6)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> #dict to other
>>> d = {1:1, 2:2, 3:3}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a number, not 'dict'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(d)
'{1: 1, 2: 2, 3: 3}'
>>> list(d)
[1, 2, 3]
>>> tuple(d)
(1, 2, 3)
>>> set(d)
{1, 2, 3}
>>> bool(d)
True
>>> #bool to other
>>> a = True
>>> int(a)
1
>>> float(a)
1.0
>>> complex(a)
(1+0j)
>>> str(a)
'True'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> 