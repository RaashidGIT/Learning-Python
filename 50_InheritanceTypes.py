# -------------------------------
# INHERITANCE TYPES
# -------------------------------
# 1. Multiple inheritance = A class inherits from MORE THAN ONE parent class
#    Example: class Fish(Prey, Predator)
#
# 2. Multilevel inheritance = A class inherits from a parent,
#    which itself inherits from another parent
#    Example: Rabbit -> Prey -> Animal
# -------------------------------

# -------------------------------
# Base Parent Class
# -------------------------------
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# -------------------------------
# Child Classes (inherit from Animal)
# -------------------------------
class Prey(Animal):   # Prey is an Animal
    def flee(self):
        print(f"{self.name} is fleeing to survive!")


class Predator(Animal):  # Predator is an Animal
    def hunt(self):
        print(f"{self.name} is hunting for food!")


# -------------------------------
# Multilevel Inheritance
# -------------------------------
class Rabbit(Prey):   # Rabbit is a Prey, and Prey is an Animal
    pass


class Hawk(Predator): # Hawk is a Predator, and Predator is an Animal
    pass


# -------------------------------
# Multiple Inheritance
# -------------------------------
class Fish(Prey, Predator):  
    # Fish inherits from BOTH Prey and Predator
    # That means Fish can BOTH flee() and hunt()!
    pass


# -------------------------------
# Create objects (instances)
# -------------------------------
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# -------------------------------
# Demonstrate MULTILEVEL inheritance
# -------------------------------
print("=== Rabbit ===")
rabbit.eat()   # from Animal
rabbit.sleep() # from Animal
rabbit.flee()  # from Prey

print("\n=== Hawk ===")
hawk.eat()
hawk.sleep()
hawk.hunt()    # from Predator

# -------------------------------
# Demonstrate MULTIPLE inheritance
# -------------------------------
print("\n=== Fish ===")
fish.eat()
fish.sleep()
fish.flee()    # from Prey
fish.hunt()    # from Predator
