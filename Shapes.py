#Edgar Ruiz
#CS 299
#Lab 7
#November 10th, 2016

#!/usr/bin/python

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def setWidth(self, width):
        self.width = width
    def setLength(self, length):
        self.length = length
    def getArea(self):
        area = self.length * self.width
        return area
class Cube(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height
    def getVolume(self):
        volume = self.getArea() * self.height
        return volume
rect1 = Rectangle(4, 9)
cube1 = Cube(4, 9, 5)
cube2 = Cube(4, 3, 5)
print("Area of Rectangle 4 x 9: ", rect1.getArea())
print("Area of Cube 4 x 9 x 5: ", cube1.getVolume())
print("Area of Cube 4 x 3 x 5: ", cube2.getVolume())
