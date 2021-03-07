#WAP to demonstrate concept of hierarchial Inheritence
class figure:
    def setvalue(self,s):
        self.s=s
class square(figure):
    def area(self):
        return self.s*self.s
class cube(figure):
    def volume(self):
        return self.s*self.s*self.s
#Now we test the class
sq=square()
cu=cube()
side=int(input("Enter side of square: "))
sq.setvalue(side)
a=sq.area()
print("Area of square=",a)
side=int(input("Enter side of cube: "))
cu.setvalue(side)
b=cu.volume()
print("Volume of cube=",b)