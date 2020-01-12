class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

a=Test(4,5)
b=a
c=Test(4,5)

print(a is b)
print(a is c)
