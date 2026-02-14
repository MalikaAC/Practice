class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

    def total_salary(self):
        return self.base


class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

    def total_salary(self):
        return self.base * (1 + self.bonus / 100)


class Developer(Employee):
    def __init__(self, name, base, projects):
        super().__init__(name, base)
        self.projects = projects

    def total_salary(self):
        return self.base + self.projects * 500


data = input().split()

if data[0] == "Manager":
    emp = Manager(data[1], int(data[2]), int(data[3]))
elif data[0] == "Developer":
    emp = Developer(data[1], int(data[2]), int(data[3]))
else:
    emp = Employee(data[1], int(data[2]))

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")