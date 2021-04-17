""" Given lists a and b, combine two lists by taking alternate
elements from them, starting with a. If the lists are different lengths, throw away
the extra elements.

>>> f([1,2], [3, 4])
[1, 3, 2, 4]
>>> f([], [])
[]
>>> f([1, 2, 3], [4])
[1, 4]
>>> f([1], [2, 3])
[1, 2]
>>> f([1, 2, 3], [])
[]
>>> f([1.0, 'mixed'], [{1: 2}, (3,)])
[1.0, {1: 2}, 'mixed', (3,)]
>>> f([1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'])
[1, 'one', 2, 'two', 3, 'three', 4, 'four', 5, 'five']
"""

def f(a, b):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()