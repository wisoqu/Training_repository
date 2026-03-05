# # Полиморфизм
#
# Классический полиморфизм
# class Animal:
#     def create_sound(self):
#         pass
#
# class Cat(Animal):
#     def create_sound(self):
#         return "Meow"
#
# class Dog(Animal):
#     def create_sound(self):
#         return "Bark"
#
# class Parrot(Animal):
#     def create_sound(self):
#         return "Hello there"
#
# def make_animal_sound(animal: Animal):
#     print(animal.create_sound())
#
# animal = [Dog(), Cat(), Parrot()]
# for x in animal:
#     make_animal_sound(x)
#
# class Figure:
#     def create_v(self):
#         pass
#
# class Sphere(Figure):
#     def create_v(self):
#         return '(4/3) * 3.14159 * radius**3'
#
# class Cube(Figure):
#     def create_v(self):
#         return 'side**3'
#
# class Piramid(Figure):
#     def create_v(self):
#         return '(1/3) * base_area * height'
#
#
# def show_info_v(figure: Figure):
#     print(figure.create_v())
#
#
#
# figures = [Sphere(), Cube(), Piramid()]
#
# for _ in figures:
#     show_info_v(_)



# Параметрический полиморфизм
#
# from typing import TypeVar, List
#
# T = TypeVar("T")
#
#
# def reverse_list(items: List[T]) -> List[T]:
#     """Fucntion is returning the list with same data-type it got"""
#     return items[::-1]
#
# nums = reverse_list([1, 2, 3])
# lst_str = reverse_list(['a', 'b', 'c'])
#
# print(nums)
# print(lst_str)

# from typing import Generic, TypeVar, List
#
# T = TypeVar("T")
#
# class Storage(Generic[T]):
#     def __init__(self):
#         self.__items: List[T] = []
#
#     def put(self, item: T):
#         self.__items.append(item)
#         print(f"Добавлено: {item}")
#
#     @property
#     def get_all(self) -> List[T]:
#         return self.__items
#
# # Сейф для чисел
# int_storage = Storage[int]()
# int_storage.put(10)
# int_storage.put(20)
# print(int_storage.get_all)
#
#
# # Сейф для букв
#
# str_storage = Storage[str]()
# str_storage.put("hello")
# str_storage.put("bye")
#
# print(f"first storage: {int_storage.get_all}")
# print(f"second storage: {str_storage.get_all}")


# Magic methods
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(1, 3)
# v2 = Vector(2, 3)
# print(v1.__add__(v2))
# 3.6