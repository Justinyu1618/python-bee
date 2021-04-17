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
    pass
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    