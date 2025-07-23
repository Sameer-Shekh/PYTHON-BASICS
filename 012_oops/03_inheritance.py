class Car:
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


# my_new_car = Car("Tata","Safari")
my_car = ElectricCar("Tesla","Model S","85kWh")
print(my_car.model)
print(my_car.full_name())
