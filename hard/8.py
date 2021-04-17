"""A perfect number is a natural number equal to the sum of its positive divisors
other than itself.

Write a function, f, which takes a positive integer as an argument and
returns True if it's perfect, or False otherwise.

>>> f(1)
False
>>> f(5)
False
>>> f(6)
True
>>> f(28)
True
>>> f(27)
False
>>> f(496)
True
>>> f(8128)
True
"""

def f(x):
    return x ==sum([y for y in range(1,x) if x%y==0 ])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    