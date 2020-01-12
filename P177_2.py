class square:
    square_list=[]
    def __init__(self,a):
        self.a=a
        self.b=a
        self.c=a
        self.d=a
        self.square_list.append(a)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.a,self.b,self.c,self.d)
square1=square(10)
square2=square(30)
print(square.square_list)
print(square(40))
