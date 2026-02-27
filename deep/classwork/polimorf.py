# # Полиморфизм
#
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

class Figure:
    def create_v(self):
        pass

class Sphere(Figure):
    def create_v(self):
        return '(4/3) * 3.14159 * radius**3'

class Cube(Figure):
    def create_v(self):
        return 'side**3'

class Piramid(Figure):
    def create_v(self):
        return '(1/3) * base_area * height'


def show_info_v(figure: Figure):
    print(figure.create_v())



figures = [Sphere(), Cube(), Piramid()]

for _ in figures:
    show_info_v(_)