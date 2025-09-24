# -------------------------------
# super() in Python
# -------------------------------
# super() is used in child classes to call methods from the parent (superclass).
# This allows:
#   1. Reusing code from the parent
#   2. Extending functionality instead of rewriting everything
# -------------------------------

# -------------------------------
# Parent Class
# -------------------------------
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


# -------------------------------
# Child Classes
# -------------------------------

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # Call Shape's __init__() to set color and is_filled
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        # Child-specific behavior
        area = 3.14 * self.radius * self.radius
        print(f"It is a circle with an area of {area} cm^2")
        # Call parent class describe() to reuse description
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        area = self.width * self.width
        print(f"It is a square with an area of {area} cm^2")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        area = (self.width * self.height) / 2
        print(f"It is a triangle with an area of {area} cm^2")
        super().describe()


# -------------------------------
# Demonstration
# -------------------------------
circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print("=== Circle ===")
circle.describe()

print("\n=== Square ===")
square.describe()

print("\n=== Triangle ===")
triangle.describe()
