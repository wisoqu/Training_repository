# Encapsulation
# Impossible to change data outside the class by using __ before varible
#
# class Human:
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self, age: int):
#         if 0 < age < 110:
#             self.__age = age
#             print(f"Age set: {age}")
#         else:
#             print(f"Incorrect age: {age}")
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#
#
#     def print_info(self):
#         print(f"Name: {self.__name}\n"
#               f"Age: {self.__age}")
#
#
# jeffry = Human("Jeffry", 45)
# jeffry.print_info()
# jeffry.set_age(-1234567)
# jeffry.set_age(12)
# jeffry.print_info()
#
#
# class Auto:
#     def __init__(self, mark, engine):
#         self.__mark = mark
#         self.__engine = engine
#
#     def set_engine(self, engine):
#         if 1.1 <= engine <= 3.5: self.__engine = engine
#         else: print(f"Impossible: {engine} cannot exist!")
#
#     def get_mark(self):
#         return self.__mark
#
#     def get_engine(self):
#         return self.__engine
#
#     def print_info(self):
#         print(f"Mark: {self.__mark}\n"
#               f"Engine: {self.__engine}")
#
# mark = Auto("bmw m4 competition", 2.3)
# mark.set_engine(12345)
# mark.set_engine(1.5)
# mark.get_mark()
# mark.get_engine()
# mark.print_info()


# Annotations of features

#
#
#
# class Human:
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#
#
#
#
#     def set_age(self, age: int):
#         if 0 < age < 110:
#             self.__age = age
#             print(f"Age set: {age}")
#         else:
#             print(f"Incorrect age: {age}")
#
#     # getter
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 110:
#             self.__age = age
#         else: print("Incorrect age")
#
#
#     def get_age(self):
#         return self.__age
#
#
#
#     def get_name(self):
#         return self.__name
#
#
#
#     def print_info(self):
#         print(f"Name: {self.__name}\n"
#               f"Age: {self.__age}")

# setter and getter have the same name (necessary)
# setter si going after getter
# need to use @setter_name.setter