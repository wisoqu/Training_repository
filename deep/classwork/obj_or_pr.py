# OOP
# class Person:
#     def __init__(self,name,age):
#         #Атрибуты класса
#         self.name = name
#         self.age = age
#         print(f"Account with name {self.name} created!")
#
#
#         #Метод класса
#     def walk(self):
#         print("I'm go for a walk")
#
#     def display_info(self):
#         print(f'Name: {self.name} Age: {self.age}')
#         #Деструктор класса
#     def __del__(self):
#         print(f"Account with name: {self.name} deleted!")
#
#
#
# def created_person():
#     tom = Person("Tom",43)
#
#
#
# created_person()
# print("Program ended")
#
#
#
#
# class Auto:
#     def __init__(self, color, mark, num, year, v):
#         self.color = color
#         self.mark = mark
#         self.num = num
#         self.year = year
#         self.v = v
#         self.is_broken = False
#         self.is_engaged = False
#         print(f"The car {self.mark} created!")
#
#
#     def break_a_car(self):
#         print("That`s over")
#         self.is_broken = True
#         self.stop()
#
#
#     def drive(self):
#         print("Current state is Ok")
#
#     def stop(self):
#         print("stopped")
#         self.is_engaged = False
#
#     def crush(self):
#         print("crushed")
#
#     def trying_drive(self):
#         if self.is_broken:
#             print("The car is broken")
#             quit()
#         else:
#             print("Sure, engine engaged!")
#             self.is_engaged = True
#
#     def __del__(self):
#         print("The car deleted!")


# Методы класса это дополнительные возможности конкрентого объекта, реализуемые через функции внутри описания класса

#car_1 =  Auto("black", "Skoda", "123", 2012, 3)

#
#
#
# def create_person():
#     car  = Auto("Black", "BMW", 123, 2012, 1.5)
#
# create_person()
# print("Program ended!")

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def summ(self):
#         return self.a + self.b
#
#     def minus(self):
#         return self.a - self.b
#
#     def multipy(self):
#         return self.a * self.b
#
#     def __del__(self):
#         print("Session stopped!")

#
# class Student:
#     def __init__(self):
#         """Nice way to ask data here, but don`t think it is better than default params. (with default u can validate data)"""
#         self.name = input("Введите имя студента: ")
#         # Запрашиваем оценки через пробел и превращаем их в список чисел
#         input_scores = input("Введите оценки через пробел: ")
#         self.scores = [int(x) for x in input_scores.split()]
#
#     def average_score(self):
#         # if not self.scores: # Проверка, чтобы не делить на ноль
#         #     return 0
#         try:
#             return sum(self.scores) / len(self.scores)
#         except ZeroDivisionError:
#             print("Impossible!")
#             quit()
#
# # Использование:
# student = Student()
# print("Средний балл студента {student.name}: {student.average_score()}")



# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores
#         print("Created successfully!")
#
#     def calc_mid(self):
#         return sum(self.scores) / len(self.scores)
#
#     def __del__(self):
#         print("Bye!")
#
# def create_stud(name, score):
#     stud = Student("bob", [5, 4, 5, 4, 3, 2, 4, 5])
