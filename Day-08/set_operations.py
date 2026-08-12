Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #set
>>> #set is mutable, unordered, unique, dynamic, heterogenous
>>> #set is heterogenous but can only include immutable datatypes
>>> s = {}
>>> s = set()
>>> type(s)
<class 'set'>
>>> s = {345,12345,6547,23,567,342,65487,234,323}
>>> s = {1,1,1,1,1,1,1}
>>> s
{1}
>>> s = {345,12345,6547,23,567,342,65487,234,323}
>>> s
{323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s
{323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s
{323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s
{323, 567, 234, 65487, 6547, 342, 23, 345, 12345}
>>> s.add(1)
>>> s.add(12.4)
>>> s.add(23+3j)
>>> s.add('str')
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add((3,45,6))
>>> s.add({435,546,234})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add({435,546,234})
TypeError: unhashable type: 'set'
>>> s.add({1:1,2:1})
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add({1:1,2:1})
TypeError: unhashable type: 'dict'
>>> s.add(False)
>>> #list, set, dict are not allowed inside set
>>> #set operations
>>> a = {324,123,443,1234,521,231,35}
>>> b = {342,1234,543,234,521,231,35}
>>> a
{1234, 35, 324, 231, 123, 521, 443}
>>> b
{1234, 35, 342, 231, 521, 234, 543}
>>> {234,21,4325} + {342,342,234}
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    {234,21,4325} + {342,342,234}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> {234,1234,5} * 2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    {234,1234,5} * 2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> a
{1234, 35, 324, 231, 123, 521, 443}
>>> b
{1234, 35, 342, 231, 521, 234, 543}
>>> 34 in a
False
>>> 34 not in a
True
>>> a & b
{521, 1234, 35, 231}
>>> #union
>>> a & b
{521, 1234, 35, 231}
>>> #union is |
>>> a | b
{35, 324, 231, 521, 234, 1234, 443, 342, 123, 543}
>>> #intersection is &
>>> a & b
{521, 1234, 35, 231}
>>> a - b
{123, 324, 443}
>>> a
{1234, 35, 324, 231, 123, 521, 443}
>>> b
{1234, 35, 342, 231, 521, 234, 543}
>>> a - b
{123, 324, 443}
>>> a - b # b values are removed from a
{123, 324, 443}
>>> b - a # a values are removed from b
{234, 342, 543}
>>> #subsets
>>> {1,2,3,4,5,6}
{1, 2, 3, 4, 5, 6}
>>> # {1}{1,2}{1,2,3},{1,2,3,4},{1,2,3,4,5,6}{2,3}
>>> a <= b
False
>>> #<= is used to check subset
>>> a >= b
False
>>> #>= is used to check superset
>>> a.isdisjoint(b)
False
>>> #indexing and slicing is not there in set
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
>>> s.index(3)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.index(3)
AttributeError: 'set' object has no attribute 'index'
>>> all(s)
False
>>> any(s)
True
>>> sum(s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sum(s)
TypeError: unsupported operand type(s) for +: 'complex' and 'str'
>>> sum(a)
2911
>>> max(a)
1234
>>> min(a)
35
>>> len(a)
7
>>> sorted(a)
[35, 123, 231, 324, 443, 521, 1234]
>>> a.count(2)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.count(2)
AttributeError: 'set' object has no attribute 'count'
>>> c = a.copy()
>>> c
{1234, 35, 324, 231, 123, 521, 443}
>>> a.add(2)
>>> a
{1234, 35, 324, 2, 231, 123, 521, 443}
>>> b
{1234, 35, 342, 231, 521, 234, 543}
>>> a = d
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a = d
NameError: name 'd' is not defined
>>> d = a
>>> a.add(45)
>>> a
{2, 324, 521, 1234, 35, 231, 45, 443, 123}
>>> d
{2, 324, 521, 1234, 35, 231, 45, 443, 123}
>>> #set methods
>>> a.add(3467)
>>> a
{2, 324, 521, 3467, 1234, 35, 231, 45, 443, 123}
>>> a.update({3425,2134,6534,231}) #to add multiple elements
>>> a
{2, 324, 6534, 521, 3467, 1234, 2134, 3425, 35, 231, 45, 443, 123}
>>> a.pop()
2
>>> a.remove(3435)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.remove(3435)
KeyError: 3435
>>> a.remove(3425)
>>> a.discard(23415)
>>> #discard wont throw error if value does not exist
>>> b.clear()
>>> b
set()
>>> #frozenset means its immutable set
>>> 