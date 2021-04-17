''' # Q5: Given a list of integers x, return a list with 1 added to each element of x.
>>> f([1,2,3,4,5]) 
[2,3,4,5,6]
>>> f([-1,0,1])
[0,1,2]
>>> f([])
[]
>>> f([2,3,1,-1])
[3,4,2,0]
'''

def f(x):
    return map(lambda y: y+1, x)

if __name__ == '__main__':
    import doctest
    doctest.testmod()