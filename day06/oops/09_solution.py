# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fule_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 
    
    def fule_type(self):
        return "Electric charge"

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# print(my_car.model)
# Car("Tata", "Nexon")
# print(my_car.general_description())
# print(Car.general_description())
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
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