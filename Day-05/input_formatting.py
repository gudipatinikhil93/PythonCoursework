Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #input formatting
>>> #int float complex str
>>> a = input()
nikhil
>>> a
'nikhil'
>>> name = input('enter your name: ')
enter your name: nikhil
>>> age = int('enter your age: ')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    age = int('enter your age: ')
ValueError: invalid literal for int() with base 10: 'enter your age: '
>>> age = int(input('enter your age: '))
enter your age: 20
>>> marks = float(input('enter your marks: '))
enter your marks: 99.99
>>> marks = list(input('enter marks: '))
enter marks: 1
>>> marks = list(input('enter marks: '))
enter marks: 1 3 4 5 7 8
>>> marks
['1', ' ', '3', ' ', '4', ' ', '5', ' ', '7', ' ', '8']
>>> names kadsg'sadjglsadkdv;laskfgpoasgkiasrkgas[kwkjgqrw[0ig[ask
SyntaxError: invalid syntax
>>> names = input('enter names: ').split()
enter names: prasad sai nikhil tarun bunny
>>> names
['prasad', 'sai', 'nikhil', 'tarun', 'bunny']
>>> names = input('enter names: ').split()
enter names: 
>>> 
>>> 
>>> names = input('enter names: ').split()
enter names: tarun nikhil
>>> names = tuple(input('enter names: ').split())
enter names: codegnan nxtwave excelr
>>> names
('codegnan', 'nxtwave', 'excelr')
>>> names = set(input('enter names: ').split())
enter names: nikhil nikhil tarun 
>>> names
{'tarun', 'nikhil'}
>>> #map() used to change the datatype inside the list by iterating one by one, it has 2 parameters, map(datatype, what to convert)
>>> marks = input('enter your marks: ').split()
enter your marks: 23 24 26
>>> marks
['23', '24', '26']
>>> marks1 = map(int,marks)
>>> marks1
<map object at 0x000001CAE825ACA0>
>>> marks1 = list(map(int,marks))
>>> marks1
[23, 24, 26]
>>> ages = tuple(map(int,input('enter your ages: ').split()))
enter your ages: 14 14 15 56
>>> ages
(14, 14, 15, 56)
>>> ages = tuple(map(bool,input('enter your ages: ').split()))
enter your ages: 12 14 15
>>> ages
(True, True, True)
>>> s = {[1], [2]}
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s = {[1], [2]}
TypeError: unhashable type: 'list'
>>> names = input('enter your name: ').split(',')
enter your name: nikhil,prasad,bunny
>>> names
['nikhil', 'prasad', 'bunny']
>>> email,password = input('enter email and password: ').split()
enter email and password: nikhil@google.com 123456
>>> email
'nikhil@google.com'
>>> password
'123456'
>>> a,b,c = list(map(int,input('enter your marks: ').split()))
enter your marks: 23 45 78
>>> a
23
>>> b
45
>>> c
78
>>> #eval
>>> names = eval(input())
nikhil prasad sai 
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    names = eval(input())
  File "<string>", line 1
    nikhil prasad sai 
           ^
SyntaxError: invalid syntax
>>> names = eval(input())
'nikhil prasad sai'
SyntaxError: multiple statements found while compiling a single statement
>>> names = eval(input())
'nikhil prasad sai'
SyntaxError: multiple statements found while compiling a single statement
>>> marks = eval(input())
{1,2,3}
>>> marks
{1, 2, 3}
>>> marks = eval(input())
'nikhil'
SyntaxError: multiple statements found while compiling a single statement
>>> marks = eval(input())
{1:1, 2:2, 3:3}
SyntaxError: multiple statements found while compiling a single statement
>>> marks = eval(input())
{1:1}
SyntaxError: multiple statements found while compiling a single statement
>>> marks = eval(input())
1
SyntaxError: multiple statements found while compiling a single statement
>>> name = eval(input('enter your name: '))
enter your name: nikhil
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    name = eval(input('enter your name: '))
  File "<string>", line 1, in <module>
NameError: name 'nikhil' is not defined
>>> name = eval(input('enter your name: '))
enter your name: 'nikhil'
>>> name
'nikhil'
>>> d = eval(input())
{'name':'nikhil'}
>>> d
{'name': 'nikhil'}
>>> l = eval(input('enter number: '))
enter number: {1:2}
>>> l
{1: 2}
>>> l = eval(input('enter number: '))
enter number: {1:2, 4:5}
>>> l
{1: 2, 4: 5}
>>> 