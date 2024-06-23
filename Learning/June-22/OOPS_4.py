""""
4. Polymorphism
Question: Create a base class Shape with a method area. Create two derived classes Rectangle and Circle that implement the area method. Use polymorphism to calculate the area of different shapes.

Hint: Use the math module for calculating the area of a circle."""
import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


circle = Circle(23)
print(circle.area())

rectangle = Rectangle(20, 2)
print(rectangle.area())
