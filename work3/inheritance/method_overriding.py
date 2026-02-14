class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
s = Shape()
s.draw()
c = Circle()
c.draw()




class Worker:
    def work(self):
        print("Working...")

class Programmer(Worker):
    def work(self):
        print("Writing code...")
w = Worker()
w.work()
p = Programmer()
p.work()



class Animal:
    def sound(self):
        print("Some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")
a = Animal()
a.sound()
c = Cat()
c.sound()




class Food:
    def eat(self):
        print("Eating food")

class Pizza(Food):
    def eat(self):
        print("Eating pizza")
f = Food()
f.eat()
p = Pizza()
p.eat()





class Day:
    def type(self):
        print("Regular day")

class Weekend(Day):
    def type(self):
        print("Weekend day")
d = Day()
d.type()
w = Weekend()
w.type()

"""
This code demonstrates method overriding in inheritance.

In each example, a parent class defines a method,
and the child class defines a method with the same name.

The child class method overrides the parent class method,
so when we call the method on a child object,
Python executes the child version instead of the parent version.

This shows how method overriding allows changing behavior in subclasses.
"""