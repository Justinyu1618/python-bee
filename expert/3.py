''' Q10: Given two integers a and b, return their least common multiple.
>>> f(12, 34)
204
>>> f(3, 15)
15
>>> f(15, 123)
615
'''

def f(a,b):
    return [x for x in range(a*b+1) if ][0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    