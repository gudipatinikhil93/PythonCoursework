Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list
>>> l = []
>>> a = list()
>>> type(a)
<class 'list'>
>>> type(l)
<class 'list'>
>>> a = [12,34.23,34+4j,'nikhil',[1,2,3],(4,5,6),{1:1,2:2},{5,6,7}]
>>> a
[12, 34.23, (34+4j), 'nikhil', [1, 2, 3], (4, 5, 6), {1: 1, 2: 2}, {5, 6, 7}]
>>> b = [g,g,g,g,g,g]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b = [g,g,g,g,g,g]
NameError: name 'g' is not defined
>>> b = [2,2,2,2,2,2,2,2,2,2]
>>> b
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
>>> #list operations
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a-b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> a*2
[1, 2, 3, 1, 2, 3]
>>> a*b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
>>> a**2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a**2
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> a*4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a/2
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> #indexing
>>> a
[1, 2, 3]
>>> a = [345,213,56,235,78,12,78]
>>> a[1]
213
>>> a[-1]
78
>>> a[0]
345
>>> #slicing
>>> a[::-1]
[78, 12, 78, 235, 56, 213, 345]
>>> a[0:4]
[345, 213, 56, 235]
>>> a[-1:-4,-1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a[-1:-4,-1]
TypeError: list indices must be integers or slices, not tuple
>>> a[-1:-4:-1]
[78, 12, 78]
>>> a[:2:2]
[345]
>>> #membership
>>> 13 in a
False
>>> 343 in a
False
>>> 345 in a
True
>>> 345 not in a
False
>>> 45 not in a
True
>>> 45 in a
False
>>> #list methods
>>> a = [12,67,45,78,21,75,57,6,32]
>>> max(a)
78
>>> min(a)
6
>>> len(a)
9
>>> sorted(a)
[6, 12, 21, 32, 45, 57, 67, 75, 78]
>>> id(a)
2537466838656
>>> a.append(2)
>>> a
[12, 67, 45, 78, 21, 75, 57, 6, 32, 2]
>>> a.append(2,3)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.append(2,3)
TypeError: list.append() takes exactly one argument (2 given)
>>> #append is used to add only 1 value
>>> a
[12, 67, 45, 78, 21, 75, 57, 6, 32, 2]
>>> a.insert(2,69)
>>> a
[12, 67, 69, 45, 78, 21, 75, 57, 6, 32, 2]
>>> a.extend([2,3,4,6])
>>> a
[12, 67, 69, 45, 78, 21, 75, 57, 6, 32, 2, 2, 3, 4, 6]
>>> a.pop()
6
>>> a.pop()
4
>>> a.pop(2)
69
>>> a.push(2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.push(2)
AttributeError: 'list' object has no attribute 'push'
>>> a.remove(67)
>>> #pop() is used to delete value based on index
>>> #remove() is used to delete value based on value
>>> #updating
>>> a[2] = 34
>>> a
[12, 45, 34, 21, 75, 57, 6, 32, 2, 2, 3]
>>> #to delete multiple values we use del
>>> del a[1:2]
>>> a
[12, 34, 21, 75, 57, 6, 32, 2, 2, 3]
>>> a
[12, 34, 21, 75, 57, 6, 32, 2, 2, 3]
>>> b = a.copy()
>>> b
[12, 34, 21, 75, 57, 6, 32, 2, 2, 3]
>>> id(a)
2537466838656
>>> id(b)
2537466838848
>>> b = a
>>> id(a)
2537466838656
>>> id(b)
2537466838656
>>> #copy means, values get copied but changes will not appear in copied variable
>>> #if a=b is done then, changes will also get appear on assigned value, id of both a and b will be same
>>> a.clear()
>>> a
[]
>>> #sorted will not effect the list
>>> #sort will effect the list
>>> a = [12,34,45]
>>> sorted(a)
[12, 34, 45]
>>> a.sort()
>>> a
[12, 34, 45]
>>> 