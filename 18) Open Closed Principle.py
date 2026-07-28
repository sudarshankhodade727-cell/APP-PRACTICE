# Open/Closed Principle (OCP)

from abc import ABC, abstractmethod

# Base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function works for any Shape
def print_area(shape):
    print("Area:", shape.area())

# Main Program
rectangle = Rectangle(10, 5)
circle = Circle(7)

print_area(rectangle)
print_area(circle)
