# -------------------------------
# INHERITANCE in Python
# -------------------------------
# Inheritance allows one class (child) to use attributes and methods 
# from another class (parent). This avoids code duplication.

# -------------------------------
# Parent Class (Animal)
# -------------------------------
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


# -------------------------------
# Child Classes (Dog, Cat, Mouse)
# -------------------------------
# These classes inherit from Animal.
# They automatically have name, is_alive, eat(), and sleep().
# But they can also define their own special methods (like speak()).

class Dog(Animal):
    def speak(self):
        print("WOOF!")   # Dog's own behavior

class Cat(Animal):
    def speak(self):
        print("MEOW!")   # Cat's own behavior

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!") # Mouse's own behavior


# -------------------------------
# Create objects (instances)
# -------------------------------
dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# -------------------------------
# Demonstrate inheritance
# -------------------------------
print("=== Dog ===")
dog.eat()     # from Animal
dog.sleep()   # from Animal
dog.speak()   # from Dog

print("\n=== Cat ===")
cat.eat()
cat.sleep()
cat.speak()

print("\n=== Mouse ===")
mouse.eat()
mouse.sleep()
mouse.speak()
