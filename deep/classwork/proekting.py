# Пораждающие
# Одиночка (Singletone) - гарантирует, что у класса есть только один экземпляр.
import copy


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

# # Builder
# class Pizza:
#     def __init__(self):
#         self.dough = None
#         self.sauce = None
#         self.toppings = []
#
#     def __str__(self):
#         return f"Pizza on {self.dough} dough, sauce: {self.sauce} suace, with: {' '.join(self.toppings) if self.toppings else 'empty'}"
#
# class PizzaBuilder:
#     def __init__(self):
#         self.pizza = Pizza()
#
#     def set_dough(self, dough):
#         self.pizza.dough = dough
#         return self
#
#     def set_sauce(self, sauce):
#         self.pizza.sauce = sauce
#         return self
#
#     def add_cheese(self):
#         self.pizza.toppings.append("cheese")
#         return self
#
#     def add_peperoni(self):
#         self.pizza.toppings.append("peperoni")
#         return self
#
#     def add_mushrooms(self):
#         self.pizza.toppings.append("mushrooms")
#         return self
#     def add_meat(self):
#         self.pizza.toppings.append("meat")
#         return self
#
#     def build(self):
#         return self.pizza
#
# margaritta = (PizzaBuilder()
#               .set_dough("thin")
#               .set_sauce("tomato")
#               .add_cheese()
#               .build())
# print(margaritta)
#
# class Director:
#     def __init__(self):
#         self.builder = None
#
#     def build_pepperoni(self):
#         builder = (PizzaBuilder()
#          .set_dough("thin")
#          .set_sauce("tomato")
#          .add_cheese()
#          .build())
#         return builder
#     def build_meat(self):
#         builder = (PizzaBuilder()
#          .set_dough("heavy")
#          .set_sauce("tomato")
#          .add_cheese()
#         .add_mushrooms()
#         .add_meat()
#          .build())
#         return builder
#     def build_mushrooms(self):
#         builder = (PizzaBuilder()
#          .set_dough("thin")
#          .set_sauce("tomato")
#          .add_cheese()
#         .add_mushrooms()
#          .build())
#         return builder


# Prototipe
# class Knight:
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon
#         self.achievements = []
#
#     def clone(self):
#         return copy.deepcopy(self)
#
#     def __str__(self):
#         return (f"Knight {self.name}\n"
#                 f"with spear {self.weapon}\n"
#                 f"Achievements {self.achievements}")
#
# # Эталонный рыцарь
# prototype_knight = Knight("Arthur", "Excalibur")
# prototype_knight.achievements.append("Dragon fighter")
#
# # Клоны для армии
# knight_clone = prototype_knight.clone()
# knight_clone.name = "Joe"
# knight_clone.achievements.append("Fire ball master")
#
# print(prototype_knight)
# print(knight_clone)


# Структурные

#@ decorator
# # 1- Базовый интерфейс
# class IterBaseEverage:
#     def get_cost(self):
#         pass
#
#     def get_description(self):
#         pass
#
# # 2 - Конкретный объект
# class SimpleCoffe(IterBaseEverage):
#     def get_cost(self):
#         return 100
#
#     def get_description(self):
#         return "Blackcoffee"
#
# # 3 - Базовый класс декоратора
# class CoffeDecorator(IterBaseEverage):
#     def __init__(self, coffe):
#         self._decorated_coffe = coffe # Хранение оборачиваемых в декораторе объектов
#
#     def get_cost(self):
#         return self._decorated_coffe.get_cost()
#
#     def get_description(self):
#         return self._decorated_coffe.get_description()
#
# # Конкретные декораторы
# class Milk(CoffeDecorator):
#     def get_cost(self):
#         return super().get_cost() + 50 # +50 за молоко
#
#     def get_description(self):
#         return super().get_description() + ", с молоком"
#
# class Sirope(CoffeDecorator):
#     def get_cost(self):
#         return  super().get_cost() + 30
#
#     def get_description(self):
#         return super().get_description() + ", с сиропом"
#
# class Sugar(CoffeDecorator):
#     def get_cost(self):
#         return super().get_cost() + 10
#
#     def get_description(self):
#         return super().get_description() + ", с сахаром"
#
#
# my_coffe = SimpleCoffe()
# print(f"{my_coffe.get_description()}: {my_coffe.get_cost()} рублей")
# my_coffe_with_milk = Milk(my_coffe)
# my_coffe_with_sirope = Sirope(my_coffe_with_milk)
# print(f"{my_coffe_with_sirope.get_description()}: {my_coffe_with_sirope.get_cost()} рублей")
#
# combo_coffe = Sugar(my_coffe_with_sirope)
#
# print(print(f"{combo_coffe.get_description()}: {combo_coffe.get_cost()} рублей"))

# Адаптер

class EmailNotifications:
    def send(self, title, text):
        print(f"Email: {title} --> {text}")

class SMSLib:
    def send_sms_message(self, phone, text_body):
        print(f"SMS on {phone}: {text_body}")


class SmsAdapter:
    def __init__(self, sms_service, phone_number):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send(self, title, text):
        text_body = f"{title}:{text}"
        self.sms_service.send_sms_message(self.phone_number, text_body) # вызов метода непонятной нам функции

def notify_user(notifier):
    notifier.send("Delivery status:", "Your dish is ready!")

email = EmailNotifications()
notify_user(email)

external_lib = SMSLib()
adapter = SmsAdapter(external_lib, "+0000000000")
notify_user(adapter)





# Поведенческие паттерны