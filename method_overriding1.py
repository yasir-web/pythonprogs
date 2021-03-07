# This program will demonstrate concept of method overriding
class A:
    def m1(self):
        print("m1 of A")
    def m2(self):
        print("m2 of A")
class B(A):
    def m1(self): #Override m1() method of class A
        print("m1 of B")
    def m3(self):
        print("m3 of B")
#Now we test the class
obj1=A()
obj2=B()
obj1.m1()
obj1.m2()
obj2.m1()
obj2.m2()
obj2.m3()

