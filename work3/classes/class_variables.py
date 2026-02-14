"""
The Student class has class variables city and total_students.
The __init__ method saves the student's name and increases total_students each time a new object is created.
As a result, all students share the same city, and total_students shows how many objects were created.
"""
class Student:
    city = "Aktau"
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

s1 = Student("Karina")
s2 = Student("Malika")
print(Student.city)
print(Student.total_students)




"""
The OnlineCourse class has a class variable max_students.
The __init__ method saves the course name.
As a result, max_students is shared by all course objects.
"""
class OnlineCourse:
    max_students = 3

    def __init__(self, name):
        self.name = name

print(OnlineCourse.max_students)



"""
The Cinema class has a class variable ticket_price.
The __init__ method stores the movie name.
As a result, all cinema objects use the same ticket price.
"""
class Cinema:
    ticket_price = 2500
    def __init__(self, movie):
        self.movie = movie
c1 = Cinema("Avatar")
print(Cinema.ticket_price)




"""
The Player class has a class variable game_level.
The __init__ method saves the player's name.
The info() method shows the current game level, which changes for all players when the class variable is updated.
"""
class Player:
    game_level = 1

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"{self.name} is on level {Player.game_level}")

p1 = Player("Karina")
p1.info()

Player.game_level = 2
p1.info()




"""
The Country class has a class variable continent.
The __init__ method saves the country name.
As a result, all country objects share the same continent value.
"""
class Country:
    continent = "Asia"

    def __init__(self, name):
        self.name = name

c1 = Country("Kazakhstan")
print(c1.name, "is in", c1.continent)