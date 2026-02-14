class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def print_info(self):
        print(self.name, "is a", self.species)
a1 = Animal("Leo", "Lion")
a1.print_info()



"""
Animal is the parent class with name and species.
Tiger is a child class that inherits everything from Animal without changes.
"""



class Tiger(Animal):
    pass
a2 = Tiger("Gera", "tiger")
a2.print_info()

"""
Cat is a child class of Animal.
It calls the parent __init__ to keep name and species,
adds a new attribute age, and overrides print_info().
"""




class Cat(Animal):
    def __init__(self, name, species, age):
        Animal.__init__(self, name, species)  
        self.age = age

    def print_info(self):
        print(self.name, "is a", self.species, "and is", self.age, "years old")
a3 = Cat("Murka", "cat", 10)
a3.print_info()

"""
Person is a parent class with name and introduce() method.
Student is a child class that inherits from Person
and uses the parent's method without modification.
"""



class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)






class Student(Person):
    pass
s1 = Student("Maliko")
s1.introduce()
s2 = Person("Mali")
s2.introduce()