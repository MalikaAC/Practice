def multiply(a, b):
    return a * b
answer = multiply(6, 7)
print(answer)
"""
takes two arguments and returns their multiplication result
"""


def greet(name):
    return "Hello " + name
print(greet("PP2"))
"""
takes one argument and returns a greeting string
"""


def get_numbers():
    return [1, 2, 3, 4]
numbers = get_numbers()
print(numbers)
print(numbers[2])
"""
returns a list of numbers
stores returned list in variable numbers
"""

def get_message():
    return "Welcome to Python"
msg = get_message()
print(msg)
"""
returns a string message
"""


def get_average(a, b):
    return (a + b) / 2
print(get_average(10, 20))
"""
takes two numbers and returns their average
"""