from abc import ABCMeta,abstractclassmethod
class Shape(metaclass=ABCMeta):
    @abstractclassmethod
    def area(self):
        return 0

class Square(Shape):
    side=4
    def area(self):
        print(self.side*self.side)
class Rectangle(Shape):
    length=5
    width=6
    def area(self):
        print(self.length*self.width)
sq=Square()
rect=Rectangle()
sq.area()
rect.area()