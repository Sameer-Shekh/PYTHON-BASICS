class Car:
    def __init__(self,brand,model): 
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","Model S","65kWh")
# print(my_tesla.__brand)
print(my_tesla.get_brand())