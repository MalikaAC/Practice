"""
sorted() sorts by the first element (name).
Lambda x: x[0] selects the name from each tuple.
"""
students = [("Karina", 17), ("Asan", 17), ("Akyltai", 18)]
sorted_names = sorted(students, key = lambda x: x[0])
print(sorted_names)


"""
Original sorted() numbers in increasing order
reverse=True changes order to decreasing.
"""
num = [2, 5, 9, 4, 5]
sort_decr = sorted(num, key = lambda x: x, reverse = True)
print(sort_decr)


"""
sorted() sorts words by length.
Lambda returns len(word), so sorting is based on word length.
"""
words = ["Calculus", "Discrete Structure", "English"]
leng = sorted(words, key = lambda i: len(i))
print(leng)


"""
Sort numbers by their absolute value.
"""
numbers = [-10, 5, -3, 8, -1]
s_a = sorted(numbers, key = lambda w: abs(w))
print(s_a)


"""
Lambda returns x % 3, so sorting depends on remainder.
"""
numbers = [10, 7, 14, 3, 9]
sorted_mod = sorted(numbers, key=lambda x: x % 3)
print(sorted_mod)