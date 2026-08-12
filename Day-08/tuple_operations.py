Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple
>>> t = (1) #this is just integer, not tuple
>>> t
1
>>> type(t)
<class 'int'>
>>> t = (1,) #we need to use comma, if we want tuple to have single element
>>> type(t)
<class 'tuple'>
>>> t = (1,2,2,3,4,5)
>>> t = (1,23.4,34+5j,'str',[1,2,3],{3,4,5},{1:1,2:3})
>>> t
(1, 23.4, (34+5j), 'str', [1, 2, 3], {3, 4, 5}, {1: 1, 2: 3})
>>> t = (1,1,1,1,1,1,1,1)
>>> t
(1, 1, 1, 1, 1, 1, 1, 1)
>>> #tuple operations
>>> t = (1,23.4,34+5j,'str',[1,2,3],{3,4,5},{1:1,2:3})
>>> max(t)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'complex' and 'float'
>>> t = (1,2,34,56,78,9,0,8,7)
>>> max(t)
78
>>> min(t)
0
>>> len(t)
9
>>> t+2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t+2
TypeError: can only concatenate tuple (not "int") to tuple
>>> t*2
(1, 2, 34, 56, 78, 9, 0, 8, 7, 1, 2, 34, 56, 78, 9, 0, 8, 7)
>>> (1,2,3) + (6,5,4)
(1, 2, 3, 6, 5, 4)
>>> (1,2,3) - (6,5,4)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    (1,2,3) - (6,5,4)
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
>>> t[2]
34
>>> t[1]
2
>>> t
(1, 2, 34, 56, 78, 9, 0, 8, 7)
>>> t[:2]
(1, 2)
>>> t[::-1]
(7, 8, 0, 9, 78, 56, 34, 2, 1)
>>> t[3:7]
(56, 78, 9, 0)
>>> t[-1:-3:-1]
(7, 8)
>>> 34 in t
True
>>> 23 in t
False
>>> 56 not in t
False
>>> 23 not in t
True
>>> sorted(t)
[0, 1, 2, 7, 8, 9, 34, 56, 78]
>>> #tuple methods
>>> t
(1, 2, 34, 56, 78, 9, 0, 8, 7)
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> t.index(56)
3
>>> t.index(0)
6
>>> t = (1,2,3,4,[4,5,6])
>>> t[4].append(8)
>>> t
(1, 2, 3, 4, [4, 5, 6, 8])
>>> #if tuple contains mutable datatype, we can modify the value of that datatype
>>> t = tuple()
>>> type(t)
<class 'tuple'>
>>> t
()
>>> any(t)
False
>>> t = (1,2,3,4,[4,5,6])
>>> any(t)
True
>>> all(t)
True
>>> sum(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sum(t)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> del t[4]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    del t[4]
TypeError: 'tuple' object doesn't support item deletion
>>> all(t)
True
>>> 