#1
class Father:
    def skill1(self):
        print("Can fix cars")

class Mother:
    def skill2(self):
        print("Can cook")

class Child(Father, Mother):
    pass
c = Child()
c.skill1()
c.skill2()




#2
class Student:
    def study(self):
        print("Studying lessons")

class Worker:
    def work(self):
        print("Working part-time")

class WorkingStudent(Student, Worker):
    pass


ws = WorkingStudent()
ws.study()
ws.work()




#3
class Fly:
    def fly(self):
        print("Flying in the sky")

class Swim:
    def swim(self):
        print("Swimming in the water")

class Duck(Fly, Swim):
    pass


d = Duck()
d.fly()
d.swim()





#4
class Read:
    def read(self):
        print("Reading a book")

class Write:
    def write(self):
        print("Writing a story")

class Author(Read, Write):
    pass


a = Author()
a.read()
a.write()





#5
class Music:
    def sing(self):
        print("Singing a song")

class Dance:
    def dance(self):
        print("Dancing on stage")

class Performer(Music, Dance):
    pass


p = Performer()
p.sing()
p.dance()

"""
These examples demonstrate multiple inheritance in Python.

In each case, one child class inherits from two parent classes.
The child class does not define its own methods (uses pass),
but it can access and use methods from both parents.

This shows that multiple inheritance allows one class
to combine behaviors from multiple parent classes.
"""