# program to:Implement a polymorphic function to calculate areas of different
# shapes (e.g., circle, rectangle, triangle) using method overriding.
import math
class Shape:
    def area(self):
        # to be define later
        raise NotImplementedError("This method should be overridden by subclasses.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    return shape.area()

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)

    print(f"Circle area: {calculate_area(circle):.2f}")
    print(f"Rectangle area: {calculate_area(rectangle):.2f}")
    print(f"Triangle area: {calculate_area(triangle):.2f}")
