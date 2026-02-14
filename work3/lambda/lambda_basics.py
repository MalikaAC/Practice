multiply = lambda x: x * 3
print(multiply(4))
"""
Lambda creates a short anonymous function.
Takes one argument x and returns x multiplied by 3.
"""


add = lambda a, b: a + b
print(add(8, 4))
"""
Lambda takes two arguments and returns their sum.
"""


average = lambda a, b, c: (a + b + c)/3
print(average(6,9,12))
"""
Lambda takes three arguments and returns their average.
"""


def myfunc(n):
    return lambda a: a * n
my = myfunc(3)
print(my(10))
"""
Returns a lambda function that multiplies a by n.
"""

def pow(n):
    return lambda a: a**n
sqr = pow(2)
cube = pow(3)
print(sqr(4))
print(cube(4))
"""
Returns a lambda function that raises a to the power of n.
"""
