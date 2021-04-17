''' Q10: Given an input list, flatten it.
Note the items in the input list may vary in their level of nesting.

You may not use the itertools module.

>>> f([[[]]])
[]
>>> f([[[1]]])
[1]
>>> f([['a'], ['b', 'c']])
['a', 'b', 'c']
>>> f([[1, 2], 3, [4, [5, 6]]])
[1, 2, 3, 4, 5, 6]
>>> f(['already', 'f[la]t'])
['already', 'f[la]t']
>>> f([1, [2], 3])
[1, 2, 3]
'''

def f(x):
    # flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    # return list(flatten(x))
    # # return x if type(x)!=type([]) else [f(a) for a in x]
    return [(a if type(a)!=type([]) else (f(b) for b in a)) for a in x] 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    