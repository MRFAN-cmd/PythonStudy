class Horse:
    def __init__(self,name,rider):
        self.name=name
        self.rider=rider

class Rider:
    def __init__(self,name,age):
        self.name=name
        self.age=age


rider1=Rider("MrFan",30)
horse1=Horse("Tiny",rider1)

print(horse1.rider.age)
