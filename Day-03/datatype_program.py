Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #int.
>>> a = 10
>>> type(a)
<class 'int'>
>>> #float
>>> b = 12.4
>>> type(b)
<class 'float'>
>>> #complex
>>> c = 3+4j
>>> type(c)
<class 'complex'>
>>> #string
>>> name = 'nikhil'
>>> name
'nikhil'
>>> type(name)
<class 'str'>
>>> #list
>>> l1 = [1,2,3,4]
>>> id(l1)
2855049739712
>>> l1.append(5)
>>> id(l1)
2855049739712
>>> type(l1)
<class 'list'>
>>> #typle
>>> t1 = (1,2,3,4)
>>> t1
(1, 2, 3, 4)
>>> type(t1)
<class 'tuple'>
>>> #set
>>> s1 = {1,2,3,3,3,4,5}
>>> s1
{1, 2, 3, 4, 5}
>>> s1
{1, 2, 3, 4, 5}
>>> s1.append(7)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1.append(7)
AttributeError: 'set' object has no attribute 'append'
>>> s1.add(8)
>>> s1
{1, 2, 3, 4, 5, 8}
>>> s1
{1, 2, 3, 4, 5, 8}
>>> type(s1)
<class 'set'>
>>> #dict
>>> d1 = {'name' : 'nikhil', 'age' : 21}
>>> d1
{'name': 'nikhil', 'age': 21}
>>> type(d1)
<class 'dict'>
>>> #boolean
>>> a = True
>>> b = False
>>> #none
>>> a = None
>>> type(a)
<class 'NoneType'>
>>> 
