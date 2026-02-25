class Device:

    def __init__(self):
        self.__is_on = False
        self.brand = "The Greatest Nefrit Xi Xiaomi Gadgets inc"

    def turn_on(self):
        if not self.__is_on:
            self.__is_on = True
            print("Turned on!")
        else: print("Already on!")

    def turn_off(self):
        if self.__is_on:
            self.__is_on = False
            print("Turned off!")
        else: print("Already off!")

    @property
    def is_on(self):
        if self.__is_on:
            return True
        return False

    @property
    def show_info(self):
        print(f"State: {self.is_on}, brand: {self.brand}")




class Light(Device):
    def __init__(self, brightness = 0):
        Device.__init__(self)
        self.brightness = brightness

    def change_br(self, new_v):
        if self.is_on and 0 <= new_v <= 100:
            self.brightness = new_v
            print(f"Brightness set: {self.brightness}")
        else: print("Value is incorrect or a lamp turned off!")




class AirConditioner(Device):
    def __init__(self):
        Device.__init__(self)
        self.temp = 20

    def set_temp(self, new_val):
        if self.is_on and -273 < new_val < 273:
            print("OK" if 10 <= new_val <= 30 else "Everyone has their own fetish, right? Temp set." if -50 < new_val < 10 or 30 < new_val < 50 else "Absolute cinema!")
            self.temp = new_val
        else: print("No, I said no. Do it somewhere else.")

