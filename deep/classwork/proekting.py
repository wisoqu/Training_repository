# Пораждающие
# Одиночка (Singletone) - гарантирует, что у класса есть только один экземпляр.


#
# class DatBase:
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             print("Database connection")
#             cls._instance = super().__new__(cls)
#             # cls - class, __new__ - делает новый пустой объект
#             # суть - если класс есть то просто выдаем его если нет то создаем новый
#         return cls._instance
#
# db1 = DatBase()
# db2 = DatBase()
#
# print(db1 is db2)
#
# class Logger:
#     logs = []
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             print("Working on...")
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __str__(self):
#         return " ".join(self.logs)
#
#     def new_message(self, message):
#         print("Message sent")
#         self.logs.append("Message")
#
#     def new_file(self, file):
#         print("file uploaded")
#         self.logs.append("File loaded")
#
# # фабрика - нужен когда заранее не знаем какие допонлительные у нас будут классы
# class Transport:
#     def delivery(self):
#         pass
#
# class Car(Transport):
#         def delivery(self):
#             return "delivery by car"
#
# class Scooter(Transport):
#     def delivery(self):
#         return "delivery by scooter"
# class Drone(Transport):
#     def delivery(self):
#         return "delivery by drone"
#
#
# class DeliverySerive:
#     def get_transport(self, type):
#         if type == "fast":
#             return Scooter()
#         if type == "heavy":
#             return Car()
# class DivideByWeight:
#     def get_transport(self, weight):
#         try:
#             if weight >= 10 and weight > 0 and weight < 100:
#                 return Car()
#             if weight < 10 and weight > 0 and weight < 100:
#                 return Scooter()
#             if weight >= 100 and weight > 0:
#                 return Drone()
#         except:
#             print("Incorrect!")
#
# service = DeliverySerive()
#
# my_delivery = service.get_transport("fast")
# my_delivery1 = service.get_transport("heavy")
# print(my_delivery1.delivery())
#
#
# # Абстрактная фабрика
# # Chairs family
# class Chair:
#     def sit_on(self):
#         pass
#
# class VictorianChair(Chair):
#     def sit_on(self):
#         return "Sitting on Victorian chair"
#
# class ModernChair(Chair):
#     def sit_on(self):
#         return "Sitting on Modern chair"
#
# # Sofas family
# class Sofa:
#     def lie_on(self): pass
#
# class VictSofa(Sofa):
#     def lie_on(self):
#         return "Lie on Vict sofa"
#
# class ModerSofa(Sofa):
#     def lie_on(self):
#         return "lie on modern sofa"
#
# class NetanyahuChair(Chair):
#     def sit_on(self):
#         return "Sitting on special Netanyahu chair, proud of it!"
#
# class NetanyahySofa(Sofa):
#     def lie_on(self):
#         return "liing on special Netanyahu chair, proud of it!"
#
#
# # Abstract fabric
#
# class FurnitureFactory:
#     def create_chair(self): pass
#     def create_sofa(self): pass
#
#
#
# class VictorianFactory(FurnitureFactory):
#     def create_chair(self):
#         return VictorianChair()
#
#     def create_sofa(self):
#         return VictSofa()
#
# class ModernFactory(FurnitureFactory):
#     def create_chair(self):
#         return ModernChair()
#
#     def create_sofa(self):
#         return ModerSofa()
#
# class NetanyahuFactory(FurnitureFactory):
#     def create_chair(self):
#         return NetanyahuChair()
#
#     def create_sofa(self):
#         return NetanyahySofa()
#
#
# # Using
#
# def setup_room(factory: FurnitureFactory):
#     chair = factory.create_chair()
#
#     sofa = factory.create_sofa()
#     print(chair.sit_on())
#     print(sofa.lie_on())
#
# setup_room(ModernFactory())
# setup_room(VictorianFactory())
# setup_room(NetanyahuFactory())

# Builder
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f"Pizza on {self.dough} dough, sauce: {self.sauce} suace, with: {' '.join(self.toppings) if self.toppings else 'empty'}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_cheese(self):
        self.pizza.toppings.append("cheese")
        return self

    def add_peperoni(self):
        self.pizza.toppings.append("peperoni")
        return self

    def add_mushrooms(self):
        self.pizza.toppings.append("mushrooms")
        return self
    def add_meat(self):
        self.pizza.toppings.append("meat")
        return self

    def build(self):
        return self.pizza

margaritta = (PizzaBuilder()
              .set_dough("thin")
              .set_sauce("tomato")
              .add_cheese()
              .build())
print(margaritta)

class Director:
    def __init__(self):
        self.builder = None

    def build_pepperoni(self):
        builder = (PizzaBuilder()
         .set_dough("thin")
         .set_sauce("tomato")
         .add_cheese()
         .build())
        return builder
    def build_meat(self):
        builder = (PizzaBuilder()
         .set_dough("heavy")
         .set_sauce("tomato")
         .add_cheese()
        .add_mushrooms()
        .add_meat()
         .build())
        return builder
    def build_mushrooms(self):
        builder = (PizzaBuilder()
         .set_dough("thin")
         .set_sauce("tomato")
         .add_cheese()
        .add_mushrooms()
         .build())
        return builder



# Структурные




# Поведенческие паттерны