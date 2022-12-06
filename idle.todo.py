Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
square=[]
for num i in range(10):
    
SyntaxError: invalid syntax
for num in range(10):
    square.append(num**2)

    
print("square :",square)
square : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
sum([x**2 for x in range(10)]))
SyntaxError: unmatched ')'
sum([x**2 for x in range(10)])
285
even_coop=[x for x in range(10) if x %2 == 0]
even_coop
[0, 2, 4, 6, 8]
cube_square=[x**2 for x%2==0 else x**3 for x in range(10)]
SyntaxError: invalid syntax
cube_square=[x**2 if x % 2==0 else x**3 for x in range(10)]
cube_square
[0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
l=list(range(1,100,4))
l
[1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97]
for key,value in enumerate(1):
    print(key,"::",value)

    
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for key,value in enumerate(1):
TypeError: 'int' object is not iterable
for key,value in enumerate(1):
    print(key," :: ",value)

    
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for key,value in enumerate(1):
TypeError: 'int' object is not iterable
for key,value in enumerate(1):
    print(key, :: ,value)
    
SyntaxError: invalid syntax
for key,value in enumerate(l):
    for key,value in enumerate(1):
        print(key," :: ",value)
        i
        a

        
Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    for key,value in enumerate(1):
TypeError: 'int' object is not iterable
for key,value in enumerate(l):
    print(key," :: ",value)

    
0  ::  1
1  ::  5
2  ::  9
3  ::  13
4  ::  17
5  ::  21
6  ::  25
7  ::  29
8  ::  33
9  ::  37
10  ::  41
11  ::  45
12  ::  49
13  ::  53
14  ::  57
15  ::  61
16  ::  65
17  ::  69
18  ::  73
19  ::  77
20  ::  81
21  ::  85
22  ::  89
23  ::  93
24  ::  97
>>> i=(str(i) for i in range(10))
>>> print(list(i))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print([str(i) for i in range (10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print([for i in range(10)])
SyntaxError: invalid syntax
>>> print([str (i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> ([for i in range(10)])
SyntaxError: invalid syntax
>>> list(i)
[]
>>> print([i for i in range(10)])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
