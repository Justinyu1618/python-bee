''' Q9: Given a string x, return the ratio of spaces to non-space characters without using count(). 
        There will be at least one non-space character.
>>> f(' a')
1
>>> f('abcd')
0
>>> f('a bcd')
0.25
>>> f('{}[ -=')
0.2
'''

def f(x):
    return len([i for i in x if i==" "])/len([i for i in x if i!=" "]) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()