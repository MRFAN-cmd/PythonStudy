import math
class Circle:
    def __init__(self,r):
        self.radius=r

    def area(self):
        return self.radius * self.radius * math.pi

Circle1 = Circle(4)
print(Circle1.area())
    
