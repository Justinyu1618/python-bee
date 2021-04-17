#!/usr/bin/env python
"""Write a function, f, which, given a list of items x, return a list
their mode (the value that appears most frequently).

You may not use the statistics module.

>>> f([1, 2, 3])
[1, 2, 3]
>>> f([1, 4, 1, 2, 4, 3])
[1, 4]
>>> f([2, 3, 2])
[2]
>>> f([1])
[1]
>>> f(['a', 'a', 'b'])
['a']
"""

def f(x):
    return list(set([i for i in x if x.count(i) == max([x.count(i) for i in x])]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()