# WAP to demonstrate the concept of method Overloading
class shape:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None and y==None:
            return x*x
        else:
            return 0
# Now we test the class
sh=shape()
print("Enter 1 to find the area of rectangle: ")
print("Enter 2 to find the area of sqaure: ")
ch=int(input())
if ch==1:
    l=int(input("Enter length of Rectangle: "))
    b=int(input("Enter Breadth of rectangle"))
    a1=sh.area(l,b)
    print("Area of Rectangle: ",a1)
elif ch==2:
    a=int(input("Enter side of square: "))
    a2=sh.area(a)
    print("Area of Saquare: ")
else:
    print("Invalid Choice")