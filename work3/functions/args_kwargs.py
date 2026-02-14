def print_words(*words):
    print("Total words:", len(words))
    print("Second word:", words[1])
    print("All words:", words)
print_words("apple", "banana", "cherry")
"""
collects all positional arguments into a tuple
thanks to * the function can take any number of values
"""


def mult_func(*num):
    total = 1
    for n in num:
        total *= n
    return total
print(mult_func(4,2,3))
print(mult_func(10, 1, 8))
"""
collects all numbers into a tuple called num
the loop multiplies each value and returns the final result
"""


def data(**info):
    print("Type:", type(info))
    print("Username:", info["username"])
    print("Country:", info["country"])
    print("All data:", info)
data(username="mlkv", country="Japan", age=17)
"""
collects keyword arguments into a dictionary
dictionary keys are used to access specific values
"""


def example(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
example(1, 2, 3, name="Rada", age=17)
"""
args stores positional arguments in a tuple
kwargs stores keyword arguments in a dictionary
prints both positional and keyword data separately
"""


def print_info(**kwargs):
    print("Type:", type(kwargs))
    print("Data:", kwargs)
print_info(name="Asan", age=17)
"""
collects all named arguments into a dictionary
print() displays the dictionary type and all key-value pairs
"""