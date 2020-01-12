class Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def calculate_perimeter(self):
        return self.width*2+self.len*2

class Square:
    def __init__(self,l):
        self.len=l

    def calculate_perimeter(self):
        return self.len*4

    def change_size(self,p):
        self.len+=p

class ShapeRectangle(Rectangle):
    def what_am_i(self):
        print("I am a shape")

class ShapeSquare(Square):
    def what_am_i(self):
        print("I am a shape")
    


shape1=ShapeRectangle(4,3)
shape1.what_am_i()

