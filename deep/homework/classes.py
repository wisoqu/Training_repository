from dataclasses import dataclass
import math


@dataclass()
class Rectangle:
    a: int
    b: int

    def area(self):
        """Вычисляет площадь прямоугольника."""
        return self.a * self.b

    def perimeter(self):
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.a + self.b)


@dataclass()
class Circle:
    r: int

    def area(self):
        """Вычисляет площадь круга."""
        return math.pi * (self.r ** 2)

    def circumference(self):
        """Вычисляет длину окружности."""
        return 2 * math.pi * self.r


@dataclass()
class Triangle:
    a: int
    b: int
    c: int

    def area(self):
        """Вычисляет площадь треугольника по формуле Герона."""
        # Полупериметр
        p = (self.a + self.b + self.c) / 2
        # Формула Герона
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        """Вычисляет периметр треугольника."""
        return self.a + self.b + self.c
