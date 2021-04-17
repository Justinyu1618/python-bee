''' Q8: Given a list of numbers x, return the mean of all positive numbers  
        There will be at least one positive number.
>>> f([1,2,3,4,5])
3
>>> f([-1,-2,-3,-4,-5,1])
1
>>> f([0,2.5,3.5,6])
4
>>> f([-2,2,3])
2.5
'''

def f(x):
    return sum([y for y in  x if y>0])/len([y for y in x if y>0])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(f([1,2,3,4]))