class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("My name is", self.name)
"""
Person is the parent class.
It has a name attribute and an introduce() method.
Other classes inherit from this class.
"""



class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def info(self):
        print(self.name, "has grade", self.grade)
s1 = Student("Karina", "A")
s1.introduce()
s1.info()
"""
Student is a child class of Person.
It uses super() to call the parent __init__ and keep the name.
It adds a new attribute grade and has its own info() method.
"""




class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        print(self.name, "teaches", self.subject)
t1 = Teacher("Akyltai", "PP2")
t1.introduce()
t1.info()
"""
Teacher is a child class of Person.
It calls super() to inherit the name attribute.
It adds subject and defines its own info() method.
"""



class Doctor(Person):
    def __init__(self, name, hospital):
        super().__init__(name)
        self.hospital = hospital
    def info(self):
        print(self.name, "works at", self.hospital)
d1 = Doctor("Bykov", "City Hospital")
d1.introduce()
d1.info()
"""
Doctor is a child class of Person.
It keeps the name using super().
It adds hospital and has an info() method.
"""





class Hobby(Person):
    def __init__(self, name, sport):
        super().__init__(name)
        self.sport = sport
    def info(self):
        print(self.name, "plays", self.sport)
a1 = Hobby("Malika", "Videogames")
a1.introduce()
a1.info()
"""
Hobby is a child class of Person.
It inherits the name attribute with super().
It adds sport and defines its own info() method.
"""



class Engineer(Person):
    def __init__(self, name):
        super().__init__(name)
e1 = Engineer("JJJ")
e1.introduce()
"""
Engineer is a child class of Person.
It only calls super() to inherit the name.
It uses the introduce() method from the parent class.
"""