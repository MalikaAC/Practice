#1. Create a generator that generates the squares of numbers up to some number N.
def sqqq(n):
    for i in range(1, n+1):
        yield i*i
ans = sqqq(int(input()))
for num in ans:
    print(num)

#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def evv(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i
ans2 = evv(int(input()))
for num in ans2:
    print(num)

#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def devv(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
ans3 = devv(int(input()))
for num in ans3:
    print(num)

#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def btw(a,b):
    for i in range(a,b+1):
        yield i*i
ans4 = btw(int(input()), int(input()))
for num in ans4:
    print(num)

#5. Implement a generator that returns all numbers from (n) down to 0.
def revv(n):
    for i in range(n, -1, -1):
        yield i
ans5 = revv(int(input()))
for num in ans5:
    print(num)