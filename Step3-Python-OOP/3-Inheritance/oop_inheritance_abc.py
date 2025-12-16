"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


from abc import ABC, abstractmethod

# create abc class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius

    def perimeter(self):
        return 2*3.14*self.radius

square1 = Square(5)
print(square1.area())
print(square1.perimeter())

circle1 = Circle(2)
print(circle1.area())
print(circle1.perimeter())