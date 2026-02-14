def my_func():
    print("Hello, practice-3!")
my_func()
"""
Prints a greeting message to the console.
"""


def my2_func(x):
    return (x + 11)*5
print(my2_func(7))
"""
Takes one argument x and returns (x + 11) multiplied by 5.
"""


def student(name, age):
    print(name, "is", age, "years old")
student("Malika", 17)
"""
Takes two arguments name and age and prints student information.
"""


def student_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
student_info("Karina", 17, "Almaty")
"""
Takes three arguments name, age, and city and prints detailed student information.
"""


def check_even(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
check_even(7)
"""
Takes one argument number and prints whether it is even or odd using a loop and if-else statement.
"""