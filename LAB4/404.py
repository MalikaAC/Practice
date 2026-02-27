a_b=input().split()
a=int(a_b[0])
b=int(a_b[1])
def my_func(a_b):
    for i in range(a,b+1):
        yield i*i

for i in my_func(a_b):
    print(i)