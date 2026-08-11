Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string method continuation
>>> #trimming methods
>>> s = '                nikhil     gudipati            '
>>> s.strip()
'nikhil     gudipati'
>>> s.lstrip()
'nikhil     gudipati            '
>>> s.rstrip()
'                nikhil     gudipati'
>>> s.replace(' ','')
'nikhilgudipati'
>>> #splitting
>>> c = 'python-mysql-flask-html-react-css-javascript-genai'
>>> c.split('-')
['python', 'mysql', 'flask', 'html', 'react', 'css', 'javascript', 'genai']
>>> c.rsplit('-')
['python', 'mysql', 'flask', 'html', 'react', 'css', 'javascript', 'genai']
>>> c.rsplit('-',3)
['python-mysql-flask-html-react', 'css', 'javascript', 'genai']
>>> c.lsplit('-',3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c.lsplit('-',3)
AttributeError: 'str' object has no attribute 'lsplit'
>>> c.split('-',2)
['python', 'mysql', 'flask-html-react-css-javascript-genai']
>>> sub = '''cloud
network
crypto
'''
>>> sub
'cloud\nnetwork\ncrypto\n'
>>> sub.splitlines()
['cloud', 'network', 'crypto']
>>> a = 'python.java.c.rust.php'
>>> '.'.join(a)
'p.y.t.h.o.n...j.a.v.a...c...r.u.s.t...p.h.p'
>>> del a
>>> a = ['python','java','c','rust','php']
>>> ''.join(a)
'pythonjavacrustphp'
>>> '-'.join(a)
'python-java-c-rust-php'
>>> #partitions
>>> #partition will always divide string to 3 parts
>>> s = 'java-python-c-rust'
>>> s.partition('-')
('java', '-', 'python-c-rust')
>>> s.rpartition('-')
('java-python-c', '-', 'rust')
>>> s
'java-python-c-rust'
>>> #testing methods
>>> n = 'nikhil is pro'
>>> n.startswith('nik')
True
>>> n.startswith('pro')
False
>>> n.endswith('pro')
True
>>> n.endswith('nik')
False
>>> 'NIKHIL'.islower()
False
>>> 'nikhil'.islower()
True
>>> 'NiKhil'.islower()
False
>>> 'NIKHIL'.isupper()
True
>>> 'nikhil'.isalpha()
True
>>> 'hohiu234'.isalpha()
False
>>> 'dsafhoh3248094'.isalphanum()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    'dsafhoh3248094'.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'
>>> 'sdfhos13894'.isalnum()
True
>>> 'nikhil'.isalnum()
True
>>> '3243425'.isalnum()
True
>>> '           '.isspace()
True
>>> '        asdfadsf'.isspace()
False
>>> 'Nikhil G'.istitle()
True
>>> 'Nikhil nikhil'.istitle()
False
>>> 'dajfoashdiof'.isupper().islower()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    'dajfoashdiof'.isupper().islower()
AttributeError: 'bool' object has no attribute 'islower'
>>> 'Nikhil nikhil'.iscapitalise()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    'Nikhil nikhil'.iscapitalise()
AttributeError: 'str' object has no attribute 'iscapitalise'
>>> 'nikhil3456472345&^*%^)&^)(*'.islower()
True
>>> 'N89032485327&(^%*%&*'.isupper()
True
>>> 'my_var'.isidentifier()
True
>>> '12_num'.isidentifier()
False
>>> '_'.isidentifier()
True
>>> '_____'.isidentifier()
True
>>> '32452345'.isdigit()
True
>>> 'dsfgd234536'.isdigit()
False
>>> '4238057893'.isnumeric()
True
>>> '435.2345'.isdecimal()
False
>>> '432532'.isdecimal()
True
>>> 