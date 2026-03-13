#Use enumerate() and zip() for paired iteration
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

names = ["Aryn", "Nurdana", "Karina"]
for index, name in enumerate(names):
    print("Student", index, ":", name)


countries = ["Kazakhstan", "Japan", "Italy"]
capitals = ["Astana", "Tokyo", "Rome"]
for country, capital in zip(countries, capitals):
    print(country, "-", capital)


a = [1, 2, 3]
b = [4, 5, 6]
for x, y in zip(a, b):
    print(x + y)


#Demonstrate type checking and conversions
#Type checking
x = 10
print(type(x))

print(isinstance(x, str))

#Type conversion
a = "5"
b = 3
result = int(a) + b
print(result)


text = str(x)
print(text)
print(type(text))


x = 4.7
y = int(x)
print(y)