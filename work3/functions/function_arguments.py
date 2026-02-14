def square(number):
    print("Square =", number * number)
square(5)
"""
takes one argument and prints its square
"""


def fav_sub(subject="Math"):
    print("My favorite subject is", subject)
fav_sub("Physics")
fav_sub()
fav_sub("Biology")
fav_sub("English")
"""
takes one argument with a default value "Math"
if no argument is passed, the default value is used
"""

def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)
my_list = ["apple", "banana", "cherry"]
print_fruits(my_list)
"""
takes a list as argument
loop iterates through each element and prints it
"""


def introduce(person, city, age):
    print(person, "is", age, "years old and lives in", city)
introduce("Karina", city="Almaty", age=18)
"""
takes positional and keyword arguments
prints formatted sentence using given values
"""


def display_book(book):
    print("Title:", book["title"])
    print("Author:", book["author"])
book_info = {"title": "Heaven Official's Blessing", "author": "Mo Xiang Tong Xiu"}
display_book(book_info)
"""
takes a dictionary as argument
accesses values using dictionary keys
"""