"""Abstraction - Exercise.

Abstraction means hiding the complex implementation details
and showing only the essential features to the user.
"""

# Step 1: Create a base class (like a blueprint) for all shapes
class Shape:
    """Base class for all shapes. Every shape should have area and perimeter."""

    def area(self):
        """Calculate the area of the shape. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        """Calculate the perimeter of the shape. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement perimeter()")

# Step 2: Create a Rectangle class that inherits from Shape
class Rectangle(Shape):
    """A rectangle has a width and a height."""

    def __init__(self, width, height):
        # Store the width and height of this rectangle
        self.width = width
        self.height = height

    def area(self):
        # Area of rectangle = width * height
        return self.width * self.height

    def perimeter(self):
        # Perimeter of rectangle = 2 * (width + height)
        return 2 * (self.width + self.height)

# Step 3: Create a Circle class that inherits from Shape
class Circle(Shape):
    """A circle has a radius."""

    def __init__(self, radius):
        # Store the radius of this circle
        self.radius = radius

    def area(self):
        # Area of circle = pi * radius^2
        # We use 3.141592653589793 as our value of pi
        pi = 3.141592653589793
        return pi * self.radius ** 2

    def perimeter(self):
        # Perimeter (circumference) of circle = 2 * pi * radius
        pi = 3.141592653589793
        return 2 * pi * self.radius

# Step 4: Demonstrate abstraction by creating shapes and calculating their properties
def abstraction():
    """Demonstrate how abstraction works with different shapes."""
    # Create a list of different shapes
    shapes = [Rectangle(5, 3), Circle(7)]

    # For each shape, calculate and print its area and perimeter
    for shape in shapes:
        # shape.__class__.__name__ gives us the class name (e.g., 'Rectangle' or 'Circle')
        print(f"{shape.__class__.__name__}:")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")

# This runs the demonstration when the file is executed directly
if __name__ == "__main__":
    abstraction()
