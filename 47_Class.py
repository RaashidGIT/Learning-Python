#----------------------------------------------- car.py -------------------------------------------------------------
# This file contains the definition of the Car class

class Car:
    # The constructor (__init__) runs when we create a new Car object
    def __init__(self, model, year, color, for_sale):
        self.model = model        # name of the car model (string)
        self.year = year          # year the car was made (number)
        self.color = color        # color of the car (string)
        self.for_sale = for_sale  # True or False (is the car for sale?)

    # Method for "driving" the car
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    # Method for "stopping" the car
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    # Method to describe the car fully
    def describe(self):
        print(f"This is a {self.year} {self.color} {self.model}")

# ---------------------------------------- main.py ----------------------------------------------------------------
# This file uses the Car class from car.py

# Import the Car class
from car import Car

# Create car objects (instances of the Car class)
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

# Accessing object attributes
print("Car 1 details:")
print("Model:", car1.model)     # prints Mustang
print("Year:", car1.year)       # prints 2024
print("Color:", car1.color)     # prints red
print("For Sale:", car1.for_sale)  # prints False
print("------------------")

# Calling methods on the objects
car1.drive()       # simulate driving car1
car1.stop()        # simulate stopping car1
print("------------------")

car3.describe()    # describe car3
