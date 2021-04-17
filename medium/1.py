'''Q1: Given a list of integers x, return the second smallest element (no repeats, length of list is at least 2).
>>> f([1,2,3,4,5])
2
>>> f([5,4,3,2,1])
2
>>> f([-1,0,1])
0
>>> f([-5,-4,-3,-2,-1])
-4
>>> f([2,4,3,1])
2
>>> f([1,2])
2
'''

def f(x):
    return(sorted(x)[1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()