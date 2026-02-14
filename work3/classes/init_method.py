"""
The Student class creates student objects.
The __init__ method saves name and grade when the object is created.
As a result, each student object stores its own name and grade.
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Karina", "A")
print(s1.name)
print(s1.grade)


"""
The Car class creates car objects.
The __init__ method assigns brand and year (with a default value).
As a result, each car object contains its own brand and year.
"""
class Car:
    def __init__(self, brand, year=2024):
        self.brand = brand
        self.year = year
c1 = Car("Toyota")        
c2 = Car("BMW", 2020)
print(c1.brand, c1.year)
print(c2.brand, c2.year)


"""
The Movie class creates movie objects.
The __init__ method initializes title, year, genre, and rating.
As a result, the object stores all movie information.
"""
class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
m1 = Movie("The Maze Runner", 2014, "Adventure", "Infinity")
print(m1.title)
print(m1.year)
print(m1.genre)
print(m1.rating)



"""
The Team class creates team objects.
The __init__ method assigns the team name and members list.
As a result, each team object keeps its own data.
"""
class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
team1 = Team("Developers", ["Asan", "Akyltai", "Karina"])
print(team1.name)
print(team1.members)



"""
The Animals class creates animal objects.
The __init__ method initializes name, class, and type.
As a result, the animal object stores its information.
"""
class Animals:
    def __init__(self,name,classes,type):
        self.name = name
        self.classes = classes
        self.type = type
A1 = Animals("Cat","mammal","domestic")
print(f"{A1.name} - {A1.classes} - {A1.type}")