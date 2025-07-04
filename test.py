class Square:

    def __init__(self, side):
        self.side = side

    def perimetr(self):
        return self.side * 4
    
class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimetr(self):
        return self.side1 + self.side2 + self.side3

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * 3.14 * self.radius
    

figure = [Circle(5), Square(5), Triangle(3, 4, 5)]

for x in figure:
    print(x.perimetr())