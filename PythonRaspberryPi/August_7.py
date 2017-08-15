Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> number = 67
>>> type (number)
<class 'int'>
>>> number = 'Python-2'
>>> type (number)
<class 'str'>
>>> number = 3.14
>>> type (number)
<class 'float'>
>>> number = [1,2,3,4]     # Number to be a list
>>> type (number)
<class 'list'>
>>> for x in range (1,10):
	print (x, '\t', x*5)

	
1 	 5
2 	 10
3 	 15
4 	 20
5 	 25
6 	 30
7 	 35
8 	 40
9 	 45
>>> for x in range (1,10):
	print (x, x*5)

	
1 5
2 10
3 15
4 20
5 25
6 30
7 35
8 40
9 45
>>> for x in range (1,10):
	print (x, '/t', '*', '\t', x*5)

	
1 /t * 	 5
2 /t * 	 10
3 /t * 	 15
4 /t * 	 20
5 /t * 	 25
6 /t * 	 30
7 /t * 	 35
8 /t * 	 40
9 /t * 	 45
>>> for x in range (1,10):
	print (x, '\t', '*', '\t', x*5)

	
1 	 * 	 5
2 	 * 	 10
3 	 * 	 15
4 	 * 	 20
5 	 * 	 25
6 	 * 	 30
7 	 * 	 35
8 	 * 	 40
9 	 * 	 45
>>> #  \t is an excape character for tab.
>>> print ('There are tons of new stuff', '\n', 'we will be learning in Python 2')
There are tons of new stuff 
 we will be learning in Python 2
>>> #  '\n' is the escape character for new line
>>> print ('There are tons of new stuff\nwe will be learning in Python 2')
There are tons of new stuff
we will be learning in Python 2
>>> # ASCII code American Standard Code for Information Interchange
>>> print (chr(30))

>>> print (chr(65))
A
>>> print (chr(65))  #  print the character which is ASCII code 65d
A
>>> print ('Today is Monday')
Today is Monday
>>> print (chr(84))  # Character represented by ASCII value of 84
T
>>> print (ord('Today is Monday'))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print (ord('Today is Monday'))
TypeError: ord() expected a character, but string of length 15 found
>>> print (ord('T'))
84
>>> print (ord('T'))  # ord is used to convert from Character to ASCII
84
>>> x = 'Tomorrow will be Tuesday'
>>> for char in x:
	print (char)

	
T
o
m
o
r
r
o
w
 
w
i
l
l
 
b
e
 
T
u
e
s
d
a
y
>>> weather = 'The sun is out'
>>> for char in weather:
	print (ord(char))

	
84
104
101
32
115
117
110
32
105
115
32
111
117
116
>>> len(weather)
14
>>> len(weather)  #  Give number of characters in the string
14
>>> print (chr(66))  # print uppercase B
B
>>> for x in range (65, 91):
	print (x, chr(x))

	
65 A
66 B
67 C
68 D
69 E
70 F
71 G
72 H
73 I
74 J
75 K
76 L
77 M
78 N
79 O
80 P
81 Q
82 R
83 S
84 T
85 U
86 V
87 W
88 X
89 Y
90 Z
>>> for x in range (65, 91):
	print (x, '\t', chr(x))

	
65 	 A
66 	 B
67 	 C
68 	 D
69 	 E
70 	 F
71 	 G
72 	 H
73 	 I
74 	 J
75 	 K
76 	 L
77 	 M
78 	 N
79 	 O
80 	 P
81 	 Q
82 	 R
83 	 S
84 	 T
85 	 U
86 	 V
87 	 W
88 	 X
89 	 Y
90 	 Z
>>> for x in range (48,58):
	print (x, '\t', chr(x))

	
48 	 0
49 	 1
50 	 2
51 	 3
52 	 4
53 	 5
54 	 6
55 	 7
56 	 8
57 	 9
>>> x = '0123456789'
>>> for number in x:
	print (ord(x))

	
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print (ord(x))
TypeError: ord() expected a character, but string of length 10 found
>>> for number in x:
	print (ord(number))

	
48
49
50
51
52
53
54
55
56
57
>>> for number in x:
	print (number, ord(number))

	
0 48
1 49
2 50
3 51
4 52
5 53
6 54
7 55
8 56
9 57
>>> for number in x:
	print (number, '\t', ord(number))

	
0 	 48
1 	 49
2 	 50
3 	 51
4 	 52
5 	 53
6 	 54
7 	 55
8 	 56
9 	 57
>>> #  chr is used to translate from ASCII to human readable character
>>> # ord is used to translate from human readable to ASCII
