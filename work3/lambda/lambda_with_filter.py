"""
filter() keeps only even numbers.
Lambda returns True when number is divisible by 2.
"""
n = [2,4,5,6,7]
even = list(filter(lambda x: x % 2== 0, n))
print(even)


"""
filter() keeps numbers greater than 10.
Lambda checks condition x > 10.
Only True results remain in the new list.
"""
values = [5, 12, 7, 18, 3, 20]
grt_10 = list(filter(lambda x: x > 10, values))
print(grt_10)


"""
filter() works with strings too.
Lambda keeps only words longer than 5 characters.
"""
words = ["apple", "banana", "kiwi", "cherry"]
lg_wr = list(filter(lambda w: len(w) > 5, words))
print(lg_wr)


"""
filter() can remove empty strings.
Lambda keeps elements that are not empty.
"""
texts = ["Hello", "", "Python", "", "2"]
non_empty = list(filter(lambda t: t != "", texts))
print(non_empty)


"""
filter() keeps only positive numbers.
Lambda returns True if number is greater than 0.
"""
numbers = [-5, 3, -1, 7, 0, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)