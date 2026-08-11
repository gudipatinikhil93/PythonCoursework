Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string
>>> s = 'nikhil'
>>> del s
>>> fname = 'nikhil'
>>> lname = 'gudipati'
>>> #concatination
>>> fname + lname
'nikhilgudipati'
>>> #repeatation
>>> fname * 10
'nikhilnikhilnikhilnikhilnikhilnikhilnikhilnikhilnikhilnikhil'
>>> '-nikhil' * 10
'-nikhil-nikhil-nikhil-nikhil-nikhil-nikhil-nikhil-nikhil-nikhil-nikhil'
>>> type(fname)
<class 'str'>
>>> name = fname.concat(lname)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name = fname.concat(lname)
AttributeError: 'str' object has no attribute 'concat'
>>> s.
SyntaxError: invalid syntax
>>> #indexing
>>> names = 'nikhil prasad bunny tharun sai'
>>> names[0]
'n'
>>> names[7]
'p'
>>> #slicing
>>> names[:7]
'nikhil '
>>> names[8:14]
'rasad '
>>> names[7:14]
'prasad '
>>> names[14:20]
'bunny '
>>> names[20:27]
'tharun '
>>> names[27:30]
'sai'
>>> #negative indexing
>>> names[-1:]
'i'
>>> names[:-1]
'nikhil prasad bunny tharun sa'
>>> names[::-1]
'ias nuraht ynnub dasarp lihkin'
>>> names[-1:-4]
''
>>> names[:-1]
'nikhil prasad bunny tharun sa'
>>> names[:-2]
'nikhil prasad bunny tharun s'
>>> names[-1:-4:-1]
'ias'
>>> names[-1:-4:]
''
>>> #membership
>>> 'sai' in names
True
>>> 'nikhil' not in names
False
>>> names[::-2]
'isnrh nu aaplhi'
>>> #ASCII value
>>> ord('a')
97
>>> chr(97)
'a'
>>> #len
>>> len(names)
30
>>> #sorted
>>> sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'b', 'd', 'h', 'h', 'i', 'i', 'i', 'k', 'l', 'n', 'n', 'n', 'n', 'p', 'r', 'r', 's', 's', 't', 'u', 'u', 'y']
>>> #max
>>> max(names)
'y'
>>> #min
>>> min(names)
' '
>>> chr(345)
'ř'
>>> chr(4325)
'ქ'
>>> chr(4235555)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    chr(4235555)
ValueError: chr() arg not in range(0x110000)
>>> chr(24523)
'忋'
>>> chr(12345)
'〹'
>>> chr(95675)
'𗖻'
>>> ord('tg')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ord('tg')
TypeError: ord() expected a character, but string of length 2 found
>>> ord('h')
104
>>> #case convertions
>>> #uppercase
>>> a = 'nxtwave vs codegnan'
>>> a.upper()
'NXTWAVE VS CODEGNAN'
>>> #lowercase
>>> a.lower()
'nxtwave vs codegnan'
>>> #title
>>> a.title()
'Nxtwave Vs Codegnan'
>>> #capitalize
>>> a.capitalize()
'Nxtwave vs codegnan'
>>> #swapcase
>>> a.swapcase()
'NXTWAVE VS CODEGNAN'
>>> #casefold
>>> a.casefold()
'nxtwave vs codegnan'
>>> #center
>>> s='codegnan is good'
>>> s.center(10,'-')
'codegnan is good'
>>> s.center(50,'-')
'-----------------codegnan is good-----------------'
>>> s.center(50,'#')
'#################codegnan is good#################'
>>> #zfill : if the value width is less then required width, it adds zeroes in the starting
>>> 67.zfill(4)
SyntaxError: invalid syntax
>>> '67'.zfill(4)
'0067'
>>> '546467'.zfill(3)
'546467'
>>> #searching and finding
>>> c = 'python full stack'
>>> s.find('p')
-1
>>> c.find('p')
0
>>> c.find('o')
4
>>> c.find('stack')
12
>>> c.index('p')
0
>>> c.rfind('l')
10
>>> c.
SyntaxError: invalid syntax
>>> c.rindex('l')
10
>>> c.index('z')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    c.index('z')
ValueError: substring not found
>>> #difference between find and index is exception handling, find will return -1 if nothing found
>>> #index will return error with nothing found
>>> #replace
>>> #-----------------
>>> c.replace('python','java')
'java full stack'
>>> #maketrans
>>> c.maketrans('aeiou','123456')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    c.maketrans('aeiou','123456')
ValueError: the first two maketrans arguments must have equal length
>>> c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> c.translate(c.maketrans('aeiou','12345'))
'pyth4n f5ll st1ck'
>>> text = 'hello nikhil'
>>> text.encode()
b'hello nikhil'
>>> text.decode()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> b'hello nikhil'.decode()
'hello nikhil'
>>> 