"""
map() adds 10 to each element in the list.
Lambda takes one value and returns modified value.
"""
nums = [5, 10, 15]
tn = list(map(lambda x: x + 10, nums))
print(tn)


"""
map() converts each string to uppercase.
Lambda applies string method .upper() to every element.
"""
words = ["apple", "orange", "banana"]
upp = list(map(lambda y: y.upper(), words))
print(upp)


"""
map() calculates square of each number in the list.
Lambda returns x squared.
"""
n = [2,5,88]
sqr = list(map(lambda x: x**2, n))
print(sqr)


"""
map() can work with two lists.
Lambda takes two arguments and adds corresponding elements.
"""
list1 = [2, 4, 5]
list2 = [1, 3, 6]
add = list(map(lambda a, b: a + b, list1, list2))
print(add)


"""
map() converts integers to strings.
Lambda transforms each number into a string type.
"""
kk = [8,5,2]
srt = list(map(lambda i: str(i), kk))
print(srt)