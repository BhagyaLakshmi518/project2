Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a="bhagya lakshmi ogirala"
>>> print(a)
bhagya lakshmi ogirala
>>> a[7:15]
'lakshmi '
>>> a[15:19]
'ogir'
>>> a[-1]
'a'
>>> a[-1:-5]
''
>>> a[-1:-6]
''
>>> a[0:7] + "is a good girl"
'bhagya is a good girl'
>>> b=a[0:7]+"is a good girl"
>>> print(b)
bhagya is a good girl
>>> a+b
'bhagya lakshmi ogiralabhagya is a good girl'
>>> a[-5:-1]
'iral'
>>> a[0:-5]
'bhagya lakshmi og'
>>> a*3
'bhagya lakshmi ogiralabhagya lakshmi ogiralabhagya lakshmi ogirala'
>>> a[-1:-6]
''
>>> a[-6:-1]
'giral'
>>> c="APSSDC"
>>> A in c
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    A in c
NameError: name 'A' is not defined
>>> A in APSSDC
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    A in APSSDC
NameError: name 'A' is not defined
>>> C in 'c'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    C in 'c'
NameError: name 'C' is not defined
>>> 'C' in 'c'
False
>>> 'A' in 'c'
False
>>> "A"in "c"
False
>>> del(a)
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> a="apssdc"
>>> 'a' in 'a'
True
>>> 'w' in 'a'
False
>>> C="APPSSDC"
>>> 'A' in 'C'
False
>>> a="bhagya lakshmi"
>>> a[-6:]
'akshmi'
>>> 'A' in C
True
>>> 'a' in c
False
>>> 'a' in a
True
>>> a="vishnu institute of technology"
>>> a.capitalize()
'Vishnu institute of technology'
>>> a.title()
'Vishnu Institute Of Technology'
>>> a,upper()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a,upper()
NameError: name 'upper' is not defined
>>> a.upper()
'VISHNU INSTITUTE OF TECHNOLOGY'
>>> a.lower()
'vishnu institute of technology'
>>> s="andhra pradesh state skill development"
>>> s.split()
['andhra', 'pradesh', 'state', 'skill', 'development']
>>> s.join()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.join()
TypeError: join() takes exactly one argument (0 given)
>>> a="bhagya"
>>> b="lakshmi"
>>> a,join(b)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a,join(b)
NameError: name 'join' is not defined
>>> a.join(b)
'lbhagyaabhagyakbhagyasbhagyahbhagyambhagyai'
>>> a=" "
>>> b="bhagya"
>>> a.join(b)
'b h a g y a'
>>> "hello {} my roll no is {}".format("bhagya","12345")
'hello bhagya my roll no is 12345'
>>> a="bhagya lakshmi"
>>> a.count('a')
3
>>> "hello [] my num is []".format("bhagya","12345")
'hello [] my num is []'
>>> 
