# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fule_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 
    
    def fule_type(self):
        return "Electric charge"

my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")
print(my_car.general_description())
print(Car.general_description())
# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.fule_type())

# safari = Car("Tata", "Safari")
# print(safari.fule_type())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
# print(Car.total_car)