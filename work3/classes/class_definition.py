"""
Create a class named MKT.
The class has one class attribute x with value 5.
"""
class MKT:
    x = 9


"""
Create an object p1 from MKT.
Access attribute x using the object.
"""
p1 = MKT()
print(p1.x)


"""
Create multiple objects from the same class.
All objects share the class attribute x.
"""
p1 = MKT()
p2 = MKT()
p3 = MKT()

print(p1.x)   
print(p2.x)   
print(p3.x)  


"""
Delete object p1 using del.
After deletion, accessing p1 will cause an error.
"""
del p1



"""
Changing attribute for one object.
This creates instance attribute only for p2.
"""
p2.x = 10

print(p2.x)       
print(MKT.x)  