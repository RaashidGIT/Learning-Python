# ---------------------------------------------------
# Aggregation vs Composition
# ---------------------------------------------------
# Aggregation = A relationship where one object contains references
#               to other INDEPENDENT objects.
#               Example: A Library "has-a" Book.
#
# Composition = The composed object directly OWNS its components,
#               which cannot exist independently.
#               Example: A Car "owns" an Engine and Wheels.
# ---------------------------------------------------


# -----------------------------
# Engine Class
# -----------------------------
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


# -----------------------------
# Wheel Class
# -----------------------------
class Wheel:
    def __init__(self, size):
        self.size = size


# -----------------------------
# Car Class (Composition Example)
# -----------------------------
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model

        # Composition: A Car creates and OWNS its Engine and Wheels.
        self.engine = Engine(horse_power)                   # Car "owns" Engine
        self.wheels = [Wheel(wheel_size) for _ in range(4)] # Car "owns" 4 Wheels

    def display_car(self):
        # Example output: "Ford Mustang 500(hp) 18in"
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"


# -----------------------------
# Create Car objects
# -----------------------------
car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

# -----------------------------
# Display the Car info
# -----------------------------
print(car1.display_car())
print(car2.display_car())
