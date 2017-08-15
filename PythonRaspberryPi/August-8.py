Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Today is Tuesday

Tomorrow is Wednesday

Day after tomorrow is Thursday

>>> f = open ('days.txt', 'r')
>>> string1 = f.read(5)
>>> print (string1)
Today
>>> print (f.tell())   # position of the pointer
5
>>> string1 = f.read(5)
>>> print (string1)
 is T
>>> print (f.tell())   # position of the pointer
10
>>> f.close()
>>> f= open ('days.txt', 'r')
>>> print (f.tell())
0
>>> f.seek(9)
9
>>> f.read(5)
'Tuesd'
>>> f.tell()
14
>>> f.read(10)
'ay\nTomorro'
>>> f.seek(0)
0
>>> f.read(5)
'Today'
>>> 
