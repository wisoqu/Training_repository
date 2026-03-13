# Static methods and attributes
# class Person:
#     type = "Person"
#     description = "Person description"
#
# print(Person.type)
# print(Person.description)
#
# Person.type = "Class Person"
# print(Person.type)


# class Person:
#     type = "Person"
#     def __init__(self, name):
#         self.name = name
#
# tom = Person("Tom")
# bob = Person("Bob")
#
# print(tom.type)
# print(bob.type)
#
# Person.type = "Class Person"
#
# print(tom.type)
# print(bob.type)



# Static methods
#
# class Person:
#     __type = "Person"
#     description = "Person description"
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def type_info():
#         print(Person.__type)
#
# #Person.type_info()
#
# tom = Person("Tom")
# bob = Person("Bob")
#
#
# tom.type_info()
# bob.type_info()



# Redefining __str__()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(self)
#         # print(f"Name: {self.name}\n"
#         #       f"Age: {self.age}")
#
#     def __str__(self):
#         return (f'Name: {self.name}\n'
#                 f'Age: {self.age}')
#
# tom = Person("Tom", 22)
# print(tom)
# tom.display_info()

#
# import abc
# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self):
#         pass
#
# shape = Shape()
# print(shape)
#
# class Rectangle(Shape):
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth = heigth
#
#     def area(self):
#         return self.width * self.heigth
#
#
#
# rect = Rectangle(11, 22)
# print(f"Rectangle area: {rect.area()}")
#
#
# class Triangle(Shape):
#     def __init__(self, a, h):
#         self.a = a
#         self.h = h
#
#     def area(self):
#         return 0.5 * self.a * self.h
#
#
#
#
#
#
# from dataclasses import dataclass
#
# class BPLA(abc.ABC):
#
#     @abc.abstractmethod
#     def distance(self):
#         pass
#
# @dataclass
# class New_bpla(BPLA):
#     km: int
#
#     def distance(self):
#         return  f"Only {self.km} distance!"

import abc


class Employee(abc.ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    @abc.abstractmethod
    def calculateSalary(self):
        pass

    def display_info(self):
        print(self)

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"ID: {self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthlysalary):
        super().__init__(name, id)
        self.monthlysalary = monthlysalary

    def calculateSalary(self):
        return self.monthlysalary * 12

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.calculateSalary()}")


class ContractEmployee(Employee):
    def __init__(self, name, id, hourlyrate, hoursworked):
        super().__init__(name, id)
        self.hourlyrate = hourlyrate
        self.hoursworked = hoursworked

    def calculateSalary(self):
        return self.hourlyrate * self.hoursworked

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.calculateSalary()}")


# Example usage
workers = [
    FullTimeEmployee("John Doe", 1, 5000),
    ContractEmployee("Jane Smith", 2, 50, 160)
]

for worker in workers:
    worker.display_info()
    print("-" * 20)
