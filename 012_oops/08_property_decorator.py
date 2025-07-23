class Car:
    total_car = 0

    def __init__(self,brand,model): 
        self.__brand = brand
        self.__model = model
        # self.total_car += 1
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def gerneral_description():
        return "cars are means for transport"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("TATA","sAFARI")
# my_car.model = "City"
Car("TATA","NEXON")

# print(my_car.model())
print(my_car.model)
