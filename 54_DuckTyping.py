# "Duck typing" = Another way to achieve polymorphism besides Inheritance
# In duck typing, an object just needs to have the required attributes/methods.
# "If it looks like a duck and quacks like a duck, it must be a duck."

# -----------------------------
# Parent-like class
# -----------------------------
class Animal:
    alive = True   # All animals (and even cars in this example) will have an "alive" attribute

# -----------------------------
# Child classes that inherit from Animal
# -----------------------------
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

# -----------------------------
# A completely different class (not related to Animal!)
# But it still has 'alive' and 'speak()'
# -----------------------------
class Car:
    alive = True   # Cars aren't alive in real life, but we add this so it "looks" like Animal

    def speak(self):
        print("HONK!")

# -----------------------------
# List of different objects
# -----------------------------
animals = [Dog(), Cat(), Car()]  # Notice Car is not an Animal, but still works

# -----------------------------
# Loop through each object
# -----------------------------
for animal in animals:
    animal.speak()          # As long as the object has speak(), this works
    print(animal.alive)     # As long as the object has alive, this works
