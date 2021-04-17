''' Q5: Given a number x, 
return
- ‘fizz’ if it’s a multiple of 3
- ‘buzz’ if it’s a multiple of 5
- ‘fizzbuzz’ if it’s a multiple of both
- the input number otherwise.

>>> f(125)
'buzz'
>>> f(17)
17
>>> f(5859375)
'fizzbuzz'
>>> f(9)
'fizz'
'''

def f(x):
    return ("fizzbuzz" if x%5==0 else "fizz") if x%3==0 else ("buzz" if x%5==0 else x)

if __name__ == '__main__':
    import doctest
    doctest.testmod()