#Use map() and filter() on lists
num = [1, 2, 3, 4, 5]
double = list(map(lambda x: x*2, num))
print(double)

even = list(filter(lambda x: x%2==0, num))
print(even)

#Aggregate with reduce() (from functools)
from functools import reduce
total = reduce(lambda x, y: x + y, num)

print(total)
