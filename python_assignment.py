# Name: Pravir Mishra
# Roll no.: E22BCAU0143

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height, color):
        Shape.__init__(self, color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius, color):
        Shape.__init__(self, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

triangle = Triangle(10, 5, "red")
circle = Circle(7, "blue")

print("Triangle area: ", triangle.area())
print("Triangle color: ", triangle.color)
print("Circle area: ", circle.area())
print("Circle color: ", circle.color)
