Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('hello world')
hello world
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 3+4
7
>>> 12*5
60
>>> 2**10
1024
>>> 10/2
5.0
>>> 11/3
3.6666666666666665
>>> 1/2
0.5
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type('abacate')
<class 'str'>
>>> dir('abacate')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help('abacate'.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

>>> 'abacate'.upper()
'ABACATE'
>>> a = 42
>>> b = 'abacate'
>>> print(a*3)
126
>>> a = 'banana'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> resposta = 42
>>> print (f'tudo tem [resposta] como solução')
tudo tem [resposta] como solução
>>> print (f'tudo tem {resposta} como solução')
tudo tem 42 como solução
>>> preco = 9.6666
>>> print (f'Preço é R$ {preco:.2f')
SyntaxError: f-string: expecting '}'
>>> print (f'Preço é R$ {preco:.2f'})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print (f'Preço é R$ {preco:.2f}')
Preço é R$ 9.67
>>> 
>>> 
>>> 
>>> a = 42
>>> b = 13
>>> a>b
True
>>> a <b
False
>>> a == 42
True
>>> b != a
True
>>> a == 42 and b == 42
False
>>> a == 42 or b == 42
True
>>> str(42) + 'abacate'
'42abacate'
>>> a = 3
>>> b = 'abacate'
>>> a, b = b, a
>>> a
'abacate'
>>> b
3
>>> a,b,c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> d,m,a = '16/12/1997'.split('/')
>>> d
'16'
>>> m
'12'
>>> a
'1997'
>>> divida = 0
>>> compra = 10
>>> divida = divida + compra
>>> compra = 50
>>> divida = divida + compra
>>> compra = 4.5
>>> divida = divida + compra
>>> divida
64.5
>>> nome = input('digite o nome:')
digite o nome:ana luiza
>>> nome
'ana luiza'
>>> n1 = input('n1')
n11
>>> 
