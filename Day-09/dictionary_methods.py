Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary
>>> #dict is mutable ordered heterogenous dynamic size
>>> #list, set, dict cannot be keys
>>> #all datatypes can be values
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = {1:2,3:4,5:6,7:8}
>>> d
{1: 2, 3: 4, 5: 6, 7: 8}
>>> d[1] = 2
>>> d
{1: 2, 3: 4, 5: 6, 7: 8}
>>> d[12.3] = 3
>>> d
{1: 2, 3: 4, 5: 6, 7: 8, 12.3: 3}
>>> del d
>>> d = {}
>>> d[1] = 1
>>> d
{1: 1}
>>> d[12.3] = 2
>>> d[23+5j] = 3
>>> d['nikhil'] = 'placed'
>>> d[True] = False
>>> d[[1,2,3]] = 4
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[[1,2,3]] = 4
TypeError: unhashable type: 'list'
>>> d[(2,3,4)] = 7
>>> d[{1,2,3}] = 7
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d[{1,2,3}] = 7
TypeError: unhashable type: 'set'
>>> d[{1:2}] = 2
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d[{1:2}] = 2
TypeError: unhashable type: 'dict'
>>> #list set dict cannot be keys
>>> del d
>>> d = {}
>>> d[1] = 1
>>> d[2] = 12.3
>>> d[3] = 12+6j
>>> d[4] = True
>>> d[5] = 'str'
>>> d[6] = [1,2,3]
>>> d[7] = (1,2,3)
>>> d[8] = {12,3}
>>> d[9] = {1:2}
>>> d[10] = frozenset(1,2,3)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d[10] = frozenset(1,2,3)
TypeError: frozenset expected at most 1 argument, got 3
>>> d[10] = frozenset({1,2,3})
>>> d
{1: 1, 2: 12.3, 3: (12+6j), 4: True, 5: 'str', 6: [1, 2, 3], 7: (1, 2, 3), 8: {3, 12}, 9: {1: 2}, 10: frozenset({1, 2, 3})}
>>> #all datatypes can be values
>>> #dict operations
>>> #membership only works on keys, not values
>>> del d
>>> d = {'name' : 'nikhil', 'course' : 'PFS' , 'batch' : 65}
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65}
>>> d['names']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d['names']
KeyError: 'names'
>>> d['name']
'nikhil'
>>> d.get('name')
'nikhil'
>>> d.get('age')
>>> #difference between accessing value through d[key] and d.get(key) is d.get() does not throw error
>>> d.get('age','key is not there')
'key is not there'
>>> d['course']
'PFS'
>>> d['batch']
65
>>> #membership
>>> 'name' in d
True
>>> 'age' in d
False
>>> 'batch' in d
True
>>> 'nikhil' in d
False
>>> #methods
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65}
>>> d['name'] = 'prasad'
>>> d
{'name': 'prasad', 'course': 'PFS', 'batch': 65}
>>> d.popitem()
('batch', 65)
>>> d.pop('course')
'PFS'
>>> d['phno'] = 987987345
>>> d
{'name': 'prasad', 'phno': 987987345}
>>> d.update({'email' : 'nikhil@codegnan.com','age':20})
>>> d
{'name': 'prasad', 'phno': 987987345, 'email': 'nikhil@codegnan.com', 'age': 20}
>>> d.clear()
>>> d = {'name' : 'nikhil', 'course' : 'PFS' , 'batch' : 65}
>>> #we cant modify key in dictionary
>>> id(d)
2269771087552
>>> d.keys()
dict_keys(['name', 'course', 'batch'])
>>> d.values()
dict_values(['nikhil', 'PFS', 65])
>>> sorted(d)
['batch', 'course', 'name']
>>> max(d)
'name'
>>> min(d)
'batch'
>>> len(d)
3
>>> d.items()
dict_items([('name', 'nikhil'), ('course', 'PFS'), ('batch', 65)])
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65}
>>> d.setdefault('name':'prasad')
SyntaxError: invalid syntax
>>> d.setdefault('name','prasad')
'nikhil'
>>> d.setdefault('age',20)
20
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20}
>>> #setdefault = get the key value, if the key value dont exist, create it with default value
>>> b = d
>>> b['placed' : True]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    b['placed' : True]
TypeError: unhashable type: 'slice'
>>> b['placed'] = True
>>> b
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> del b
>>> a = d.copy()
>>> a
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> a['placed'] = True
>>> a
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> b
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> a
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> a['exam'] = 'attempted'
>>> a
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True, 'exam': 'attempted'}
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> d.get('name')
'nikhil'
>>> d.get('company','tcs')
'tcs'
>>> d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65, 'age': 20, 'placed': True}
>>> #fromkeys() = initialise multiple key with given value
>>> dict.fromkeys(['python','mysql','flask'],0)
{'python': 0, 'mysql': 0, 'flask': 0}
>>> 