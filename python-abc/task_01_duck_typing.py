from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.141592653589793*self.radius*self.radius)

    def perimeter(self):
        return (2*3.141592653589793*self.radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width*self.height)

    def perimeter(self):
        return (2*self.width+2*self.height)


def shape_info(Shape):
    print("Area:", Shape.area())
    print("Petimeter:", Shape.perimeter())
