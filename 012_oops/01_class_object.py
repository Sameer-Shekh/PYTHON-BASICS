# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car)
# <__main__.Car object at 0x000002078E857230>

class Car:
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car.model);