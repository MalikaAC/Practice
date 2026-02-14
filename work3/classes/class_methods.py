"""
The Volunteer class creates volunteer objects.
The __init__ method saves name and profession when the object is created.
The work() method prints a message using the object's data.
"""
class Volunteer:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def work(self):
        print("Hello! My name is " + self.name + " and I am an " + self.profession + ".")

w1 = Volunteer("Malika", "Engineer")
w1.work()



"""
The Calculator class creates a simple calculator object.
It has methods minus() and devide() that perform subtraction and division.
The object is used to calculate and print the results.
"""
class Calculator:
    def minus(self, a, b):
        return a - b
    def devide(self, a, b):
        return a/b
math = Calculator()
print(math.minus(8,3))
print(math.devide(15,5))



"""
The Student class creates student objects.
The __init__ method stores name and grade.
The get_info() method returns formatted information about the student.
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return f"{self.name} has grade {self.grade}"
s1 = Student("Karina", "A")
print(s1.get_info())



"""
The Car class creates car objects.
The __init__ method saves brand and speed.
The accelerate() method increases speed and prints the updated value.
"""
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print(f"The {self.brand} is now moving at {self.speed} km/h")

car1 = Car("BMW", 60)
car1.accelerate(20)
car1.accelerate(15)



"""
The Student class creates student objects with name and major.
The __init__ method initializes these attributes.
The __str__() method defines how the object is displayed when printed.
"""
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        return f"{self.name} studies {self.major}"

s1 = Student("Malika", "Automation and Control")
print(s1)