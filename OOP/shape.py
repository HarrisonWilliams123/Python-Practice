class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius * self.radius)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height
    
circle = Circle(7)
square = Square(4)
triangle = Triangle(6, 8)

print("Circle area:", circle.area())
print("Square Area", square.area())
print("Triangle area:", triangle.area())

