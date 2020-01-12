class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return self.base*self.height/2

a_Triangle=Triangle(5,35)
print(a_Triangle.area())
