"""
shapes.py

In-class exercise: Circle and Rectangle (methods)
"""

class Circle:
    pi = 3.14 # class attribute (in real projects use math.pi)

    def __init__(self,radius: float)-> float:
        self.radius = radius # instance attribute

    def calculate_area(self):
        return self.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * self.pi * self.radius


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length  # fixed typo: was "lenght"
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    c1 = Circle(radius=5)
    print(f"Area: {c1.calculate_area():.2f}")            # 78.50
    print(f"Perimeter: {c1.calculate_perimeter():.2f}")  # 31.40

    r1 = Rectangle(length=4, width=2)
    print(f"Area: {r1.calculate_area():.2f}")            # 8.00
    print(f"Perimeter: {r1.calculate_perimeter():.2f}")  # 12.00
    