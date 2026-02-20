#Наследование
# Супер класс - базовый класс в котором есть
# реализация методов и атибутов и от которого они наследуются другими подклассами
# Подкласс(дочерний класс)-наследует от супер класса все публичные атрибуты и методы

class Human:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_inf(self):
        print(f"Name: {self.__name}")


class Employer(Human):
    def __init__(self, name, salary = 27000):
        Human.__init__(self, name)
        self.__salary = salary

    def go_to_work(self):
        print(f"{self.name} go to work")

    def show_salary(self):
        return self.__salary

    def change_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Cannot be negative!")


class Student(Human):
    def __init__(self, name, stip = 15000):
        Human.__init__(self, name)
        self.__stip = stip

    def go_to_lecture(self):
        print(f"{self.name} go to lecture")

    def show_stip(self):
        return self.__stip

    def change_stip(self, stip):
        if stip > 0:
            self.__stip = stip
        else:
            print("Cannot be negative!")


class WorkingStudent(Employer, Student):
    def __init__(self, name, salary, stip):
        Employer.__init__(self, name, salary)
        Student.__init__(self, name, stip)

    def show_money(self):
        # Вызываем методы, чтобы получить значения
        print(f"Scholarship: {self.show_stip()}, Salary: {self.show_salary()}, Name: {self.name}")


bob = Employer('Bob', 50000)
bob.go_to_work()
bob.display_inf()
print(f"Bob's salary: {bob.show_salary()}")


john = Student('John', 2000)
john.go_to_lecture()
john.display_inf()
print(f"John's scholarship: {john.show_stip()}")


ann = WorkingStudent("Ann", 30000, 1500)
ann.go_to_work()
ann.go_to_lecture()
ann.display_inf()
# Вызываем новый метод, чтобы увидеть все доходы
ann.show_money()
