# -------------------------------
# ABSTRACT CLASSES in Python
# -------------------------------
# An abstract class:
#   - Cannot be instantiated directly (you can't make an object from it).
#   - Can define abstract methods (methods with NO implementation).
#   - Forces child classes to provide their OWN implementation of these methods.
#
# This is useful when you want all subclasses to follow the same "blueprint".
# -------------------------------

from abc import ABC, abstractmethod   # ABC = Abstract Base Class

# -------------------------------
# Abstract Parent Class
# -------------------------------
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        """Start moving (must be implemented by child)"""
        pass

    @abstractmethod
    def stop(self):
        """Stop moving (must be implemented by child)"""
        pass


# -------------------------------
# Concrete Child Classes
# -------------------------------
class Car(Vehicle):   # Inherits from Vehicle
    def go(self):     # Must implement abstract method
        print("🚗 You drive the car")

    def stop(self):
        print("🚗 You stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("🏍️ You ride the motorcycle")

    def stop(self):
        print("🏍️ You stop the motorcycle")


class Boat(Vehicle):
    def go(self):
        print("⛵ You sail the boat")

    def stop(self):
        print("⚓ You anchor the boat")


# -------------------------------
# Demonstration
# -------------------------------
# NOTE: You cannot do this:
# vehicle = Vehicle()   ❌ ERROR (abstract class cannot be instantiated)

# But you CAN create objects from subclasses that implemented all abstract methods:
car = Car()
motorcycle = Motorcycle()
boat = Boat()

# Each child class has its own version of go() and stop()
print("=== Car ===")
car.go()
car.stop()

print("\n=== Motorcycle ===")
motorcycle.go()
motorcycle.stop()

print("\n=== Boat ===")
boat.go()
boat.stop()
