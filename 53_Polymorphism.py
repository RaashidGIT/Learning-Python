# -------------------------------
# Polymorphism in Python
# -------------------------------
# Polymorphism = "many forms"
#   - Poly = Many
#   - Morphe = Form
#
# Ways to achieve polymorphism:
#   1. Inheritance (common parent class)
#   2. Duck typing (object just needs correct methods/attributes)
# -------------------------------

from abc import ABC, abstractmethod

# -------------------------------
# Abstract Base Class (ABC)
# -------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        """All shapes must implement an area method"""
        pass


# -------------------------------
# Child Classes
# -------------------------------
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# -------------------------------
# Another class that "is a" Circle
# -------------------------------
class Pizza(Circle):
    def __init__(self, topping, radius):
        # Reuse Circle's constructor for radius
        super().__init__(radius)
        self.topping = topping


# -------------------------------
# Demonstration of Polymorphism
# -------------------------------
shapes = [
    Circle(4),
    Square(5),
    Triangle(6, 7),
    Pizza("pepperoni", 15)
]

for shape in shapes:
    # Notice: We don't care what type of shape it is.
    # As long as it has an area() method, this works!
    print(f"{shape.__class__.__name__}: {shape.area()} cm²")
