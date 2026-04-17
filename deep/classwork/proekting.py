# Пораждающие
# Одиночка (Singletone) - гарантирует, что у класса есть только один экземпляр.
from g4f.debug import logs
from sympy.codegen.ast import none


class DatBase:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Database connection")
            cls._instance = super().__new__(cls)
            # cls - class, __new__ - делает новый пустой объект
            # суть - если класс есть то просто выдаем его если нет то создаем новый
        return cls._instance

db1 = DatBase()
db2 = DatBase()

print(db1 is db2)

class Logger:
    logs = []
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Working on...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        return " ".join(self.logs)

    def new_message(self, message):
        print("Message sent")
        self.logs.append("Message")

    def new_file(self, file):
        print("file uploaded")
        self.logs.append("File loaded")

# фабрика - нужен когда заранее не знаем какие допонлительные у нас будут классы
class Transport:
    def delivery(self):
        pass

class Car(Transport):
        def delivery(self):
            return "delivery by car"

class Scooter(Transport):
    def delivery(self):
        return "delivery by scooter"
class Drone(Transport):
    def delivery(self):
        return "delivery by drone"


class DeliverySerive:
    def get_transport(self, type):
        if type == "fast":
            return Scooter()
        if type == "heavy":
            return Car()
class DivideByWeight:
    def get_transport(self, weight):
        try:
            if weight >= 10 and weight > 0 and weight < 100:
                return Car()
            if weight < 10 and weight > 0 and weight < 100:
                return Scooter()
            if weight >= 100 and weight > 0:
                return Drone()
        except:
            print("Incorrect!")

service = DeliverySerive()

my_delivery = service.get_transport("fast")
my_delivery1 = service.get_transport("heavy")
print(my_delivery1.delivery())


# Структурные




# Поведенческие паттерны