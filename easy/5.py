''' Q5: Given a list x and two positive integers i and n  as input, return a list with an element i inserted into the nth position of list x (n <len(x))
>>> f([1,2,3,4,5], 6, 2)
[1,2,6,3,4,5]
>>> f([],1,0)
[1]
>>> f(['a','b'], 2, 2)
['a','b',2]
>>> f([[1,2],[2,3]], 2, 1)
[[1,2],1,[2,3]]
>>>f([‘hello’, ‘world’]) 
[‘world’, ‘hello’]
'''
def f(x,i,n):
    # Your Code Here!
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()