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

'rectangle1=Rectangle(4,3)'
square1=Square(8)

'print(rectangle1.calculate_perimeter())'
print(square1.calculate_perimeter())

square1.change_size(5)
print(square1.calculate_perimeter())
