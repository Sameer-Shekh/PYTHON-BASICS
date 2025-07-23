class Car:
    def __init__(self,brand,model): 
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla","Model S","65kWh")
print(my_tesla.fuel_type())
my_safari = Car("tata","safari")
print(my_safari.fuel_type())